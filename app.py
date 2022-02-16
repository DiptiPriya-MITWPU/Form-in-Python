from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='template')

subscribers = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/subscribe")
def subscribe():
    return render_template("subscribe.html")

@app.route("/form", methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    subscribers.append(f"{first_name} {last_name} | {email}")

    return render_template("form.html", subscribers=subscribers)