import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/jobs.csv")

df["job_title"] = df["job_title"].fillna("")
df["job_description"] = df["job_description"].fillna("")

df["combined_text"] = (
    df["job_title"] + " " + df["job_description"]
)

vectorizer = TfidfVectorizer(
    stop_words="english"
)

tfidf_matrix = vectorizer.fit_transform(
    df["combined_text"]
)

user_skills = input(
    "Enter your skills: "
)

user_vector = vectorizer.transform(
    [user_skills]
)

similarity = cosine_similarity(
    user_vector,
    tfidf_matrix
).flatten()

top_indices = similarity.argsort()[-10:][::-1]

print("\nRecommended Jobs:")

for index in top_indices:

    print(
        df.iloc[index]["job_title"],
        "Match:",
        round(similarity[index] * 100, 2),
        "%"
    )