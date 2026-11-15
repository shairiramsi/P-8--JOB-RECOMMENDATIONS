import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/jobs.csv")

df["posted_date"] = pd.to_datetime(
    df["posted_date"],
    errors="coerce"
)

df = df.dropna(subset=["posted_date"])

df["month"] = df["posted_date"].dt.to_period("M")

monthly_counts = df.groupby("month").size()

plt.figure(figsize=(14, 6))

monthly_counts.plot(
    marker="o",
    linewidth=3
)

plt.title("Monthly Job Market Dynamics")

plt.xlabel("Month")
plt.ylabel("Number of Job Postings")

plt.grid(True)

plt.tight_layout()

plt.savefig("outputs/task6_monthly_trends.png")

plt.show()