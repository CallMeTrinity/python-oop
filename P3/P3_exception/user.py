class User:
    username = ''
    password = ''
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.check_username()
        self.check_password()

    def check_username(self):
        if len(self.username) < 3:
            raise UsernameTooShortException

    def check_password(self):
        has_letter = False
        has_digit = False

        for l in self.password:
            if l.isdigit():
                has_digit = True
            if l.isalpha():
                has_letter = True
        if has_letter and has_digit:
            return True
        else:
            raise WeakPasswordException


class UsernameTooShortException(Exception):
    def __init__(self, message="Username trop court", *args):
        self.message = message
        super().__init__(self.message, *args)



class WeakPasswordException(Exception):
    def __init__(self, message="Password trop faible", *args):
        self.message = message
        super().__init__(self.message, *args)

try:
    user = User('toto', 'chef')
except WeakPasswordException as e:
   print(e.message)
