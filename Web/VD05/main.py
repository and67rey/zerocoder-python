from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    context = {
        "homepage": "active",
        "aboutpage": None
    }
    return render_template("home.html", **context)

@app.route("/about/")
def contact_page():
    context = {
        "homepage": None,
        "aboutpage": "active"
    }
    return render_template("about.html", **context)

if __name__ == "__main__":
    app.run()