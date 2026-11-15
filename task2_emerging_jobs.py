import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset/jobs.csv")

df["posted_date"] = pd.to_datetime(
    df["posted_date"],
    errors="coerce"
)

df = df.dropna(subset=["posted_date"])

df["month"] = df["posted_date"].dt.to_period("M")

monthly_jobs = (
    df.groupby(["month", "job_title"])
    .size()
    .reset_index(name="postings")
)

print(monthly_jobs.head())