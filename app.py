import os

from flask import Flask, render_template, request, jsonify

from src.data_utils import load_jobs, prepare_jobs
from src.analysis import build_dashboard
from src.recommender import recommend_jobs

app = Flask(__name__)

DATA_PATH = "data/jobs.csv"


def get_data():

    df = load_jobs(DATA_PATH)

    df = prepare_jobs(df)

    return df


@app.route("/", methods=["GET", "POST"])
def home():

    try:

        df = get_data()

        dashboard = build_dashboard(df)

        recommendations = []

        if request.method == "POST":

            profile = request.form.get("profile", "")

            location = request.form.get("location", "")

            recommendations = recommend_jobs(
                df,
                profile,
                location,
                top_n=10
            )

        return render_template(
            "index.html",
            dashboard=dashboard,
            recommendations=recommendations,
            total=len(df),
            error=None
        )

    except Exception as e:

        return render_template(
            "index.html",
            dashboard=None,
            recommendations=[],
            total=0,
            error=str(e)
        )


@app.route("/api/jobs")
def api_jobs():

    try:

        df = get_data()

        return jsonify(
            df.head(100).fillna("").to_dict(orient="records")
        )

    except Exception as e:

        return jsonify({"error": str(e)}), 400


@app.route("/api/recommend", methods=["POST"])
def api_recommend():

    try:

        data = request.get_json(force=True)

        df = get_data()

        results = recommend_jobs(
            df,
            data.get("profile", ""),
            data.get("location", ""),
            top_n=10
        )

        return jsonify(results)

    except Exception as e:

        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )