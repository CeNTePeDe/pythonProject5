import AuthException as Ex


class Authorizor:

    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permission = {}

    def add_permission(self, perm_name):
        """Create a new permssion that users can be added"""
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            self.permission[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        """Grant the given permission to the user"""
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            raise PermissionError("Permission doesn't exist")
        else:
            if username not in self.authenticator.users:
                raise Ex.InvalidUsername(username)
            perm_set.add(username)
