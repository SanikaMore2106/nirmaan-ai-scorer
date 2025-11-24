# Deployment Guide – Nirmaan AI Transcript Scorer

Follow these steps to run the project on your local system.

---

## 1️⃣ Install Python

Ensure Python 3.9+ is installed.

Check version:
```bash
python --version
```

---

## 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

Activate it:

### Windows
```bash
venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Prepare Rubric

Ensure the rubric file is placed in the same directory:

```
CaseStudyRubric.xlsx
```

And referenced in **load_rubric.py**:
```python
EXCEL_PATH = "CaseStudyRubric.xlsx"
```

---

## 5️⃣ Run Backend Server

```bash
uvicorn app:app --reload
```

Your server starts at:
```
http://127.0.0.1:8000/
```

---

## 6️⃣ Open Frontend

Open:
```
index.html
```

---

## 7️⃣ Troubleshooting

### ❗ Issue: CORS error
Backend already includes:
```python
allow_origins=["*"]
```

### ❗ Excel file not found
Ensure Excel file name is exactly:
```
CaseStudyRubric.xlsx
```

### ❗ Backend not responding
Restart:
```bash
Ctrl + C
uvicorn app:app --reload
```

---

# Deployment Complete 🎉
