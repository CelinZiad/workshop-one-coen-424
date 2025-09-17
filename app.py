from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = "dev-only-change-me"

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/success')
def success():
    return render_template("success.html") 

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    if username == "admin":
        return redirect(url_for("success"))
    flash("You cannot log in because you are not an admin. Please enter an admin username.")
    return redirect(url_for('index'))
