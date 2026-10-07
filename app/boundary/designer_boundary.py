from flask import Blueprint, render_template

from app.boundary import role_required

designer_bp = Blueprint("designer", __name__, url_prefix="/designer")


@designer_bp.route("/")
@role_required("designer")
def home():
    return render_template("designer/home.html")
