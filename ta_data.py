from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/TA/")
@app.route("/TA/<section>")
def section(section=None):
    return render_template("section.html", section=section)

if (__name__ == '__main__'):
    app.run(debug=True)
