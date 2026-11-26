import csv
import glob
import os
import subprocess
import tempfile
import zipfile
from typing import List

# Path to the JPlag CLI jar (download "jplag-x.y.z-jar-with-dependencies.jar"
# from https://github.com/jplag/JPlag/releases). Can be set in .env as JPLAG_JAR.
DEFAULT_JPLAG_JAR = "tools/jplag.jar"


def _read_similarities(csv_path: str) -> List[float]:
    """Read pairwise similarities from the CSV exported by JPlag (--csv-export)."""
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames or []
        # prefer the average similarity, fall back to any "similarity" column
        sim_cols = [c for c in columns if "similarity" in c.lower()]
        avg_cols = [c for c in sim_cols if "avg" in c.lower() or "average" in c.lower()]
        col = (avg_cols or sim_cols or [None])[0]
        if col is None:
            raise RuntimeError(f"No similarity column in {csv_path}: {columns}")
        scores = [float(row[col]) for row in reader if row[col] not in ("", None)]

    # some JPlag versions report percentages, keep everything in 0.0-1.0
    if scores and max(scores) > 1.0:
        scores = [s / 100 for s in scores]
    return scores


def run_jplag(task_path: str) -> List[float]:
    """Run JPlag on one task folder (each .py file is one submission)
    and return the similarity of every pair as floats in 0.0-1.0."""
    jplag_jar = os.getenv("JPLAG_JAR", DEFAULT_JPLAG_JAR)
    with tempfile.TemporaryDirectory() as tmpdir:
        result_file = os.path.join(tmpdir, "result")
        subprocess.run(
            [
                "java", "-jar", jplag_jar,
                "-l", "python3",
                "-r", result_file,
                "--mode", "RUN",      # do not open the report viewer
                "--csv-export",
                "--overwrite",
                task_path,
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        # JPlag writes a .jplag/.zip archive and the CSV next to it or inside it
        for archive in glob.glob(os.path.join(tmpdir, "result*")):
            if zipfile.is_zipfile(archive):
                with zipfile.ZipFile(archive) as z:
                    z.extractall(os.path.join(tmpdir, "unpacked"))

        csv_files = glob.glob(os.path.join(tmpdir, "**", "*.csv"), recursive=True)
        if not csv_files:
            raise RuntimeError("JPlag did not produce a CSV file")
        return _read_similarities(csv_files[0])