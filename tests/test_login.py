from app.control.login_controller import LoginController
from app.entity.user_account import UserAccount


def test_login_succeeds_with_correct_password(app):
    UserAccount.create("amy@test.com", "pass123", "customer")
    account = LoginController().login("amy@test.com", "pass123")
    assert account is not None
    assert account.role == "customer"


def test_login_fails_with_wrong_password(app):
    UserAccount.create("amy@test.com", "pass123", "customer")
    assert LoginController().login("amy@test.com", "wrong") is None


def test_suspended_account_cannot_log_in(app):
    account = UserAccount.create("bob@test.com", "pass123", "designer")
    account.is_suspended = True
    assert LoginController().login("bob@test.com", "pass123") is None


def test_login_page_redirects_customer_to_customer_home(client):
    UserAccount.create("amy@test.com", "pass123", "customer")
    response = client.post("/login", data={"email": "amy@test.com", "password": "pass123"})
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/customer/")


def test_customer_cannot_open_admin_pages(client):
    UserAccount.create("amy@test.com", "pass123", "customer")
    client.post("/login", data={"email": "amy@test.com", "password": "pass123"})
    assert client.get("/admin/").status_code == 403
