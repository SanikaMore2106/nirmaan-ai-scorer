import pandas as pd

EXCEL_PATH = "CaseStudyRubric.xlsx"   # Place your Excel file here

def load_rubric():
    df = pd.read_excel(EXCEL_PATH)

    rubric = []
    for _, row in df.iterrows():
        keywords = []
        if not pd.isna(row.get("keywords")):
            keywords = [k.strip() for k in row["keywords"].split(",")]

        rubric.append({
            "criterion_id": str(row.get("criterion_id")),
            "description": str(row.get("description")),
            "keywords": keywords,
            "weight": float(row.get("weight")),
            "min_words": int(row["min_words"]) if not pd.isna(row.get("min_words")) else None,
            "max_words": int(row["max_words"]) if not pd.isna(row.get("max_words")) else None
        })

    return rubric
