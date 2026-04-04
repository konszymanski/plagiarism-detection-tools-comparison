# Plagiarism Detection Tools Comparison — CSEDU 2026

This repository contains the source code, datasets, and experimental scripts used for the research paper: **"Comparative Analysis of Non-Commercial Plagiarism Detectors for Computer Science Education"**. The paper was accepted to the **18th International Conference on Computer Supported Education (CSEDU 2026)** in Benidorm, Spain (https://csedu.scitevents.org/Home.aspx).

---

### **Authors**
* Paulina Gacek
* Bartosz Gdowski
* Konrad Szymański
* Wojciech Żmuda

(*AGH University of Krakow, Faculty of Electrical Engineering, Automatics, IT and Biomedical Engineering*)

---
### **Original respository (private)**

https://github.com/sprawdzarka-aisd/plagiarism-detection-tools-comparison

---

### **Setup & Installation**

#### **1. Python Environment**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

#### **2. Dolos Setup**
Dolos requires a specific version of Node.js (v20). Newer versions may not be compatible. For OS-specific instructions, visit the [official download page](https://nodejs.org/en/download).

```bash
# Install and use the correct Node.js version via nvm
nvm install 20
nvm use 20

# Install Dolos globally
npm install -g @dodona/dolos

# Verify the installation
dolos --version
```
*If you encounter issues, please refer to the [Dolos installation guide](https://dolos.ugent.be/docs/installation.html).*

---

### **Execution**
To run the main comparison script and reproduce the analysis:
```bash
python3 scripts/main.py
```

---

### **About the Research**
This project provides a qualitative and quantitative evaluation of four widely used non-commercial detection systems: **MOSS, JPlag, DOLOS,** and **copydetect**. Our analysis was conducted using three distinct experimental protocols:

1.  **Dataset A (Academic Corpus):** 102 genuine student submissions used to measure boilerplate filtering efficiency.
2.  **Dataset B (Algorithmic Discrimination):** 252 LeetCode problems (comparing naive vs. optimal solutions) to establish false-positive rates.
3.  **Dataset C (Obfuscation Resilience):** A synthetic dataset featuring 4 levels of adversarial transformations (Formatting, Lexical, Structural, and Semantic).

**Key Findings:**
* **JPlag & MOSS:** Demonstrated the highest resilience against false positives but showed vulnerability to structural obfuscation.
* **copydetect:** Offered exceptional robustness against obfuscation attacks, though it requires careful calibration to manage false-positive rates.
* **DOLOS:** Distinguished by superior cluster-based visualizations and network graphs, making it the most effective tool for identifying complex collusion groups.
