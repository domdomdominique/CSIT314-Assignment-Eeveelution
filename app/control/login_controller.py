from app.entity.user_account import UserAccount


class LoginController:
    """Control: handles the 'Log in' use case for every actor."""

    def login(self, email, password):
        return UserAccount.login(email, password)
