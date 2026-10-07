from functools import wraps

from flask import abort, redirect, session, url_for


def role_required(role):
    """Only let logged-in users with this role open the page."""

    def decorator(view):
        @wraps(view)
        def wrapped(*args, **kwargs):
            if "user_id" not in session:
                return redirect(url_for("auth.login"))
            if session.get("role") != role:
                abort(403)
            return view(*args, **kwargs)

        return wrapped

    return decorator
