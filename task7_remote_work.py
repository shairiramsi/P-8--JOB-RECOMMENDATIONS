import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset/jobs.csv")

print(df["work_mode"].value_counts())