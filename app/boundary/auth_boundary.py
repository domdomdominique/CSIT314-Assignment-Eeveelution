from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from app.control.login_controller import LoginController

auth_bp = Blueprint("auth", __name__)

HOME_BY_ROLE = {
    "admin": "admin.home",
    "designer": "designer.home",
    "customer": "customer.home",
    "platform": "platform.home",
}


@auth_bp.route("/")
def index():
    return redirect(url_for("auth.login"))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Boundary: LoginPage."""
    if request.method == "POST":
        account = LoginController().login(request.form["email"], request.form["password"])
        if account:
            session["user_id"] = account.id
            session["role"] = account.role
            return redirect(url_for(HOME_BY_ROLE[account.role]))
        flash("Invalid email or password.")
    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
