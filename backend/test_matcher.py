from matcher import analyze_resume

resume = """
Python developer with experience in data analysis, SQL, and machine learning.
Worked with Pandas, NumPy, and scikit-learn.
"""

job_description = """
Looking for a Python developer with experience in machine learning,
data analysis, SQL, FastAPI, and cloud deployment.
"""

result = analyze_resume(resume, job_description)
print(result)
