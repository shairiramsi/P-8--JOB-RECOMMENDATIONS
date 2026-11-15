import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

df = pd.read_csv("dataset/jobs.csv")

df["posted_date"] = pd.to_datetime(
    df["posted_date"],
    errors="coerce"
)

df = df.dropna(subset=["posted_date"])

df["month"] = df["posted_date"].dt.month
df["year"] = df["posted_date"].dt.year

print(df.head())