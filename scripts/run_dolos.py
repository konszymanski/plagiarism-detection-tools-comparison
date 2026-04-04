import subprocess
import pandas as pd
import tempfile
import os
import zipfile

def run_dolos(task_path):
    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, "task.zip")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(task_path):
                for file in files:
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, task_path)
                    zipf.write(full_path, arcname)

        subprocess.run(
            [
                "dolos",
                "run",
                "-f", "csv",
                "-l", "python",
                zip_path,
            ],
            cwd=tmpdir,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )


        result_dirs = [
            d for d in os.listdir(tmpdir)
            if os.path.isdir(os.path.join(tmpdir, d))
            and d != "__pycache__"
        ]

        if not result_dirs:
            raise RuntimeError("Dolos did not create a result directory")

        result_dir = os.path.join(tmpdir, result_dirs[0])
        pairs_csv = os.path.join(result_dir, "pairs.csv")

        if not os.path.exists(pairs_csv):
            raise RuntimeError("pairs.csv not found in Dolos output")

        df = pd.read_csv(pairs_csv, usecols=["similarity"])
        return df["similarity"].tolist()
