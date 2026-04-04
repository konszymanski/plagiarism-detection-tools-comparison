import seaborn as sns
import matplotlib.pyplot as plt
import os
import pandas as pd
import json


def plot_similarity_distributions(all_data, output_dir, filename):
    """Generates a Histogram comparing similarity counts across tasks."""
    plt.figure(figsize=(12, 7))
    sns.set_style("whitegrid")

    df = pd.DataFrame(all_data)

    if df.empty:
        print("No similarity data found to plot.")
        return

    # Create the histogram
    # bins=20 divides the 0.0-1.0 range into 5% increments
    # element="step" makes it easier to see overlapping distributions for 8 tasks
    plot = sns.histplot(
        data=df,
        x="score",
        hue="tool",
        bins=20,
        element="step",
        common_norm=False,
        palette="tab10",
        alpha=0.6,
    )

    plt.title("Number of Matching Pairs per Similarity Level", fontsize=15)
    plt.xlabel("Similarity Score (0.0 to 1.0)", fontsize=12)
    plt.ylabel("Count (Number of Pairs)", fontsize=12)
    plt.xlim(0, 1.0)

    plot_path = os.path.join(output_dir, filename)
    plt.savefig(plot_path)
    print(f"\n[Success] Count-based chart saved to {plot_path}")


def plot_similarity_distributions_KDE(all_data, output_dir, filename, title=""):
    """Generates a smooth KDE plot comparing similarity distributions."""
    plt.figure(figsize=(12, 7))
    sns.set_style("whitegrid")

    df = pd.DataFrame(all_data)

    if df.empty:
        print("No similarity data found to plot.")
        return

    # Use kdeplot for smooth curves
    # fill=True mimics the alpha-filled area of your histogram
    plot = sns.kdeplot(
        data=df,
        x="score",
        hue="tool",
        fill=True,
        common_norm=False,
        palette="tab10",
        alpha=0.4,
        linewidth=2,
    )

    plt.title(f"Distribution of similarity scores for {title}.", fontsize=15)
    plt.xlabel("Similarity score", fontsize=12)
    plt.ylabel("Density", fontsize=12)  # KDE measures density, not raw counts
    plt.xlim(0, 1.0)

    plot_path = os.path.join(output_dir, filename)
    plt.savefig(plot_path)
    plt.close()  # Good practice to close the plot to free memory
    print(f"\n[Success] Smooth KDE chart saved to {plot_path}")


def plot_cases_chart(tool_files, output_dir, filename, title=""):
    """
    tool_files: A dictionary mapping Tool Name to its JSON file path
    e.g. {"JPlag": "jplag_results.json", "Dolos": "dolos_results.json"}
    """
    all_data = []

    # 1. Load and process each file
    for tool_name, file_path in tool_files.items():
        with open(file_path, "r") as f:
            data = json.load(f)

        for case_name, scores in data.items():
            for score in scores:
                all_data.append(
                    {"Case": case_name, "Similarity Score": score, "Tool": tool_name}
                )

    df = pd.DataFrame(all_data)

    # 2. Setup Plot
    plt.figure(figsize=(14, 8))
    sns.set_style("whitegrid")

    # 3. Create a Violin Plot (Smooth distribution per case)
    # Split=True allows comparing two tools side-by-side inside one "violin"
    # sns.violinplot(
    # data=df,
    # x="Case",
    # y="Similarity Score",
    # hue="Tool",
    # inner=None,       # Remove default inner markings
    # cut=0,
    # alpha=0.3         # Make violins lighter so dots stand out
    # )

    # 2. Add the dots manually using stripplot
    # 'size' controls the dot size here
    # 'dodge=True' ensures dots align with the specific Tool's violin
    sns.stripplot(
        data=df,
        x="Case",
        y="Similarity Score",
        hue="Tool",
        dodge=False,       # Crucial: aligns dots with the split violins
        size=15,          # ADJUST THIS for bigger dots
        jitter=False,
        linewidth=1.2,    # Thickness of the edge
        edgecolor="black", # Color of the edge
        alpha=0.5,
        legend=True      # Hide extra legend from the dots
    )

    # 4. Styling
    plt.title("Comparison of Detection Tools Across Cases", fontsize=16)
    plt.xticks(rotation=45, ha="right")
    plt.ylim(0, 1.05)
    plt.ylabel("Similarity Score (0.0 - 1.0)")

    plt.tight_layout()
    plot_path = os.path.join(output_dir, filename)
    plt.savefig(plot_path)
    print(f"Comparison chart saved to {plot_path}")


# --- Example Usage ---
# Replace these with your actual filenames
files = {"Tool_A": "tool_a_data.json", "Tool_B": "tool_b_data.json"}

# For demonstration purposes, if you are running this in a script:
#
