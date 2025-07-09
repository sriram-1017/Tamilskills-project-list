import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from utils import checker

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    password = ""
    if request.method == "POST":
        password = request.form["password"]
        result = checker.evaluate_password(password)
        example = checker.generate_example_password(password) if result["strength"] != "Strong" else None
        result["example"] = example
    return render_template("index.html", result=result, password=password)

if __name__ == "__main__":
    app.run(debug=True)
