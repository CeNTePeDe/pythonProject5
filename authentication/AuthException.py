class AuthException(Exception):
    def __init__(self, username, user=None):
        super.__init__(username, user)
        self.username = username
        self.user = user


class UserNameAlredyExist(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


class PermissionError(Exception):
    pass


class NotLoggedInError(AuthException):
    pass


class NotPermissionError(AuthException):
    pass
