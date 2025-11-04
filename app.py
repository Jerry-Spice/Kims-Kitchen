from flask import Flask, render_template, request, redirect, url_for

from Recipe import Recipe
from Cookbook import Cookbook
from User import User

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
