from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mentors")
def mentors():
    return render_template("mentors.html")

@app.route("/curriculum")
def curriculum():
    return render_template("curriculum.html")

@app.route("/different")
def different():
    return render_template("different.html")

if __name__ == "__main__":
    app.run(debug=True)
