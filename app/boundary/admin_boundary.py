from flask import Blueprint, render_template

from app.boundary import role_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/")
@role_required("admin")
def home():
    return render_template("admin/home.html")
