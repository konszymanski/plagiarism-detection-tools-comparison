import os
from run_copydetect import run_copydetect
from generate_charts import plot_similarity_distributions

# --- CONFIGURATION ---
DATA_SOURCE = "./data"  # Path to your 8 task folders
OUTPUT_DIR = "./results"
EXTENSIONS = ["py"]      # Change to ["cpp", "java", etc.] as needed
BOILERPLATE_DIR = None   # Path to template code if available

all_scores = []
    
# Get all task directories
tasks = [d for d in os.listdir(DATA_SOURCE) if os.path.isdir(os.path.join(DATA_SOURCE, d))]
tasks.sort()
os.makedirs(OUTPUT_DIR, exist_ok=True)
for task in tasks:
    task_path = os.path.join(DATA_SOURCE, task)
    print(task_path)

    try:
        scores = run_copydetect(task_path)
        for s in scores:
            all_scores.append({"task": task, "tool": "copydetect", "score": s})
    except Exception as e:
        print(f"Error processing {task} with Copydetect: {e}")
    
plot_similarity_distributions(all_scores, OUTPUT_DIR)

