import os
import json
from enum import Enum
import time
from typing import List
from dotenv import load_dotenv

from run_copydetect import run_copydetect
from run_dolos import run_dolos
from run_moss import run_moss
from run_jplag import run_jplag

from generate_charts import plot_similarity_distributions_KDE, plot_cases_chart

SOURCE_DIR_LEETCODE = "data_leetcode"
SOURCE_DIR_LEETCODE_TXT = "leetcode_problems.txt"
SOURCE_DIR_ALL_STUDENTS = "data/solutions/all_students"
SOURCE_DIR_SPECIFIC_CASES = "data/solutions/specific_cases"
RESULTS_DIR = "results"
MOSS_BASE_FILE= "data/boilerplate/1_root_system.py"

class PlagiarismDetectionTool(Enum):
    COPY_DETECT = "copy_detect"
    JPLAG = "jplag"
    MOSS = "moss"
    DOLOS = "dolos"

load_dotenv()
mossid = os.getenv("MOSSID")
if not mossid:
    print("Error: MOSSID in .env file is missing")
    exit(1)

def run_moss_with_pause(path):
    result = run_moss(path, int(mossid), MOSS_BASE_FILE)
    print(f"Waiting 5s after MOSS request for {path}...")
    time.sleep(5)
    return result

tool_to_runner = {
    # PlagiarismDetectionTool.COPY_DETECT: run_copydetect,
    # PlagiarismDetectionTool.JPLAG: run_jplag,
    PlagiarismDetectionTool.MOSS: run_moss_with_pause,
    # PlagiarismDetectionTool.DOLOS: run_dolos,
}

def get_leetcode_problems():
    problems = []
    with open(SOURCE_DIR_LEETCODE_TXT, 'r') as file:
        problems = [line.strip() for line in file]
    return problems


def generate_leetcode_stats(tool: PlagiarismDetectionTool) -> List[float]:
    filename = os.path.join(RESULTS_DIR, "leetcode", f"{tool.value}.txt")
    if os.path.exists(filename):
        print(f"😮‍💨 File {filename} already exists. To re-generate delete it first.")
    else:
        problems = get_leetcode_problems()
        for id, problem_dir in enumerate(problems):
            print(id, " ", problem_dir)
            full_path = os.path.join(SOURCE_DIR_LEETCODE, problem_dir)
            results = tool_to_runner[tool](full_path)
            with open(filename, "a") as file:
                for result in results:
                    file.write(f"{result}\n")

    scores = []
    with open(filename, 'r') as file:
        # float(line) automatically handles the newline characters (\n)
        scores = [float(line) for line in file]
    return scores

def generate_students_stats(tool: PlagiarismDetectionTool) -> List[float]:
    filename = os.path.join(RESULTS_DIR, "all_students", f"{tool.value}.txt")
    if os.path.exists(filename):
        print(f"😮‍💨 File {filename} already exists. To re-generate delete it first.")
    else:
        results = tool_to_runner[tool](SOURCE_DIR_ALL_STUDENTS)
        with open(filename, "a") as file:
            for result in results:
                file.write(f"{result}\n")
    
    scores = []
    with open(filename, 'r') as file:
        # float(line) automatically handles the newline characters (\n)
        scores = [float(line) for line in file]
    return scores


def generate_specific_cases_stats(tool: PlagiarismDetectionTool):
    filename = os.path.join(RESULTS_DIR, "specific_cases", f"{tool.value}.json")
    if os.path.exists(filename):
        print(f"😮‍💨 File {filename} already exists. To re-generate delete it first.")
    cases = {}
    for problem_dir in os.listdir(SOURCE_DIR_SPECIFIC_CASES):
        full_path = os.path.join(SOURCE_DIR_SPECIFIC_CASES, problem_dir)
        results = tool_to_runner[tool](full_path)
        cases[problem_dir] = results
        
    with open(filename, "w") as file:
        json.dump(cases, file, indent=4, sort_keys=True)

    return filename


if __name__ == "__main__":
    all_scores_leetcode = []
    for tool in tool_to_runner.keys():
        scores = generate_leetcode_stats(tool)
        for s in scores:
            all_scores_leetcode.append({"task": "leetcode", "tool": tool.value, "score": s})
    plot_similarity_distributions_KDE(all_scores_leetcode, RESULTS_DIR, "leetcode.png", "Leetcode original solutions (within the same tasks)")
    
    all_scores_students = []
    for tool in tool_to_runner.keys():
        scores = generate_students_stats(tool)
        for s in scores:
            all_scores_students.append({"task": "students", "tool": tool.value, "score": s})
    plot_similarity_distributions_KDE(all_scores_students, RESULTS_DIR, "students_moss.png", "students solutions")
    
    files = {}
    for tool in tool_to_runner.keys():
        files[tool.value] = generate_specific_cases_stats(tool)
    plot_cases_chart(files, RESULTS_DIR, "specific_cases.png", "specific cases pairs.")