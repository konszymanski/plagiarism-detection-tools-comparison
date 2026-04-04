from copydetect import CopyDetector
from typing import List

def run_copydetect(task_path) -> List[float]:
    # task path - sciezka do folderu z zdadaniami
    # funkcja ma policzyc similarity kazdy z kazdym i zwrocic tablice floatow (0.0-1.0)
    # subprocess.run(["dolos", "-l"])

    detector = CopyDetector(test_dirs=[task_path], extensions=["py"], display_t=0.0, 
                            force_language="python", silent=True)
    detector.run()
    
    # The matrix shape is (num_test_files, num_ref_files, 2)
    # [:, :, 0] gets the similarity of test file vs ref file
    matrix = detector.similarity_matrix
    
    # Flatten the matrix and filter out the diagonal (self-comparisons)
    # and any zero-matches to keep the chart clean
    scores = matrix[:, :, 0].flatten()
    scores = scores[scores >= 0] 
    
    return scores.tolist()
