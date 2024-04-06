import os
from flask import Flask, render_template


app = Flask(__name__)


# route decorator for home page
@app.route("/")
def index():
    return render_template("index.html")


# route decorator for menu page
@app.route("/menu")
def menu():
    return render_template("menu.html")


# route decorator for review page
@app.route("/reviews")
def reviews():
    return render_template("post_review.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # Change to False on final deployment
        debug=True
    )