from pathlib import Path
from matplotlib import pyplot as plt
from flask import Flask, render_template, request

from classes.NumericalMethods import NumericalMethods
from to_refactor.forces import acc_gravity
from utils.pdf_metadata import extract_pdf_metadata

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        template_name_or_list="index.html",
        problem_sets_junior=extract_pdf_metadata(
            Path(app.root_path, "static", "problem_sets_junior")
        ),
        problem_sets_senior=extract_pdf_metadata(
            Path(app.root_path, "static", "problem_sets_senior")
        ),
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

        planet = NumericalMethods(
            initial_x=x, initial_y=y, initial_vx=vx, initial_vy=vy
        )

        fig, ax = planet.plot_trajectory(
            numerical_method=NumericalMethods.perform_euler,
            acc_function=acc_gravity,
            iterations=iterations,
            delta_t=delta_t,
        )

        output_path = (
            Path(app.root_path) / "static" / "planet_trajectory" / "trajectory.svg"
        )

        fig.savefig(output_path, format="svg")

        plt.close(fig)

    return render_template("planet_trajectory.html")


if __name__ == "__main__":
    app.run(debug=True)
