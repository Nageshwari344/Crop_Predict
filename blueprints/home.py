from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from src.Auth import Auth

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def home():
    return render_template("index.html", session=session)


@bp.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html", session=session)


@bp.route("/login", methods=["POST","GET"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    if Auth.login_user(email, password):
        session["user"] = email
        flash("Login successful!")
        return redirect(url_for("home.dashboard"))
    else:
        flash("Invalid email or password.")
        return redirect(url_for("home.home"))


@bp.route("/register", methods=['POST'])
def register():
    if all(key in request.form for key in ['full_name', 'email', 'password']):
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']

        result = Auth.register(full_name, email, password)
        if result == "Registration successful":
            session['authenticated'] = True
            return redirect(url_for('home.dashboard'))
        else:
            return str(result)
    return "Invalid request"