from flask import Blueprint, render_template

from app.boundary import role_required

platform_bp = Blueprint("platform", __name__, url_prefix="/platform")


@platform_bp.route("/")
@role_required("platform")
def home():
    return render_template("platform/home.html")
