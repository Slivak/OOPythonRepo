# DIP (Dependency Inversion Principle) - Принцип инверсии зависимостей
# Не нужно создавать зависимости в классе
# Вот и всё, а код внизу кал
"""
class Authorization():
    def __init__(self, connector):
        self.connection = connector.connect()

    def authentification(self, credentials):
        pass
    def is_authentificated(self):
        pass
    def last_login(self):
        pass

class AnonumousAuth(Authorization):
    pass

class GitHubAuth(Authorization):
    def last_login(self):
        pass

class FacebookAuth(Authorization):
    pass

class Permisson():
    def __init__(self, auth: Authorization):
        self.auth = auth

    def has_permission(self):
        pass

class IsLoggedInPermission(Permisson):
    def last_login(self):
        pass

"""