class User:

    def __init__(self, name, contact_method):
        self.name = name
        self.contact_method = contact_method

    def send(self, message):
        self.contact_method.send(message)
