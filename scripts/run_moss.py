import os
import re
import time
import requests
import mosspy
from bs4 import BeautifulSoup
from typing import List


def run_moss(task_path: str, userid: int, base_file = "") -> List[float]:
    time.sleep(2)
    m = mosspy.Moss(userid, "python")
    m.setNumberOfMatchingFiles(400)
    if base_file != "":
        m.addBaseFile(base_file)
    
    files = [os.path.join(task_path, f) for f in os.listdir(task_path) if f.endswith('.py')]
    if not files:
        print("Błąd: Nie znaleziono plików .py w folderze.")
        return []

    for f in files:
        m.addFile(f)

    try:
        url = m.send()
        print(f"MOSS URL: {url}")
        with open("results/all_students/moss_urls_uhuhu.txt", "a") as file:
            file.write(f"{url}\n")

        response = requests.get(url)
        # Using 'lxml' is highly recommended for malformed HTML. 
        # If not installed, run: pip install lxml
        soup = BeautifulSoup(response.content, 'lxml')

        # Find the main table
        main_table = soup.find('table')
        if not main_table:
            return "No table found."

        # Find all rows directly under this table
        rows = main_table.find_all('tr', recursive=False)
        # If the table uses tbody, the rows might be one level deeper
        if not rows:
            tbody = main_table.find('tbody', recursive=False)
            rows = tbody.find_all('tr', recursive=False) if tbody else main_table.find_all('tr')

        results = []

        # Iterate skipping the first row (header)
        for i, row in enumerate(rows):
            if i == 0:
                continue

            # We only want the first 2 columns (td)
            cols = row.find_all('td', recursive=False)
            if len(cols) >= 2:
                # Combine the HTML of only the first TWO cells. 
                # This prevents searching into nested rows/tables.
                target_html = str(cols[0]) + str(cols[1])
                
                # Regex to find (xx%) - more flexible with potential spaces
                # This matches: ( followed by digits followed by % followed by )
                matches = re.findall(r'\((\d+)%\)', target_html)
                
                if matches:
                    # Formatting the match back to (xx%) as requested
                    formatted_matches = [str(int(m) / 100) for m in matches]
                    results.extend(formatted_matches)

        return results

    except Exception as e:
        print(f"Błąd krytyczny: {e}")
        return []