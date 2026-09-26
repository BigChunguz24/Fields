from pathlib import Path

from flask import Flask, render_template, request
from matplotlib import pyplot as plt

from forces import acc_gravity
from numerical_methods import perform_euler
from p001_planet_trajectory_euler import plot_trajectory

app = Flask(__name__)

problem_sets_junior = [
    {"title": "Junior Physics Olympiad 17", "file": "junior_17.pdf"},
]

problem_sets_senior = [
    {"title": "Senior Physics Olympiad 21", "file": "senior_21.pdf"},
]


@app.route("/")
def home():
    return render_template(
        template_name_or_list="index.html",
        problem_sets_junior=problem_sets_junior,
        problem_sets_senior=problem_sets_senior,
    )


@app.route("/planet-trajectory", methods=["GET", "POST"])
def planet_trajectory():

    if request.method == "POST":

        x = float(request.form["x"])
        y = float(request.form["y"])
        vx = float(request.form["vx"])
        vy = float(request.form["vy"])

        delta_t = float(request.form["delta_t"])
        iterations = int(request.form["iterations"])

        df = perform_euler(
            initial_x=x,
            initial_y=y,
            initial_vx=vx,
            initial_vy=vy,
            acc_function=acc_gravity,
            iterations=iterations,
            delta_t=delta_t,
        )

        fig, ax = plot_trajectory(
            df=df,
            delta_t=delta_t,
            iterations=iterations,
        )

        output_path = (
            Path(app.root_path) / "static" / "planet_trajectory" / "trajectory.svg"
        )

        fig.savefig(output_path, format="svg")

        plt.close(fig)

    return render_template("planet_trajectory.html")


if __name__ == "__main__":
    app.run(debug=True)
