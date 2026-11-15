import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset/jobs.csv")

df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)

country_salary = (
    df.groupby("country")["salary"]
    .mean()
    .sort_values(ascending=False)
    .head(15)
)

print(country_salary)