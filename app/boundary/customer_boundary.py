from flask import Blueprint, render_template, request

from app.boundary import role_required
from app.control.search_idp_controller import SearchIDPController

customer_bp = Blueprint("customer", __name__, url_prefix="/customer")


@customer_bp.route("/")
@role_required("customer")
def home():
    """Boundary: SearchIDPPage (customer home)."""
    keyword = request.args.get("q", "")
    results = SearchIDPController().search(keyword)
    return render_template("customer/search_idp.html", results=results, keyword=keyword)
