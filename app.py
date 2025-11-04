from flask import Flask, render_template, request, redirect, url_for

from Recipe import Recipe
from Cookbook import Cookbook
from User import User

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)