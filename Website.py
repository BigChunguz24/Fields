from flask import Flask, render_template

app = Flask(__name__)

problem_sets_junior = [
    {
        "title": "Junior Physics Olympiad 17",
        "file": "junior_17.pdf"
    },
]

problem_sets_senior = [
{
        "title": "Senior Physics Olympiad 21",
        "file": "senior_21.pdf"
    },
]

@app.route("/")
def home():
    return render_template(
        template_name_or_list="index.html",
        problem_sets_junior=problem_sets_junior,
        problem_sets_senior=problem_sets_senior,
    )


if __name__ == "__main__":
    app.run(debug=True)