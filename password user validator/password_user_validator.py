import string


class UsernameTooShort(Exception):
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "The username is too short"


class UsernameTooLong(Exception):
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "The username is too long"


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, n, idx):
        self.n = n
        self.idx = idx

    def __str__(self):
        return f'The username contains an illegal character "{self.n[self.idx]}" at index {self.idx}'


class PasswordTooShort(Exception):
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "The password is too short"


class PasswordTooLong(Exception):
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "The password is too long"


class PasswordMissingCharacter(Exception):
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "The password is missing a character"


class Uppercase(PasswordMissingCharacter):
    def __init__(self, n):
        PasswordMissingCharacter.__init__(self, n)

    def __str__(self):
        return f'{PasswordMissingCharacter.__str__(self)} ({Uppercase.__name__})'


class Lowercase(PasswordMissingCharacter):
    def __init__(self, n):
        PasswordMissingCharacter.__init__(self, n)

    def __str__(self):
        return f'{PasswordMissingCharacter.__str__(self)} ({Lowercase.__name__})'


class Digit(PasswordMissingCharacter):
    def __init__(self, n):
        PasswordMissingCharacter.__init__(self, n)

    def __str__(self):
        return f'{PasswordMissingCharacter.__str__(self)} ({Digit.__name__})'


class Special(PasswordMissingCharacter):
    def __init__(self, n):
        PasswordMissingCharacter.__init__(self, n)

    def __str__(self):
        return f'{PasswordMissingCharacter.__str__(self)} ({Special.__name__})'


def digits(password):
    flag = -1
    for i in range(len(password)):
        if password[i].isdigit():
            flag = i
            break
    return flag

def special_note(password):
    flag = -1
    for i in range(len(password)):
        if password[i] in set(string.punctuation):
            flag = i
            break
    return flag


def isupper(password):
    flag_up = False
    for i in set(password):
        if str(i).isupper():
            flag_up = True
            break
    return flag_up


def islower(password):
    flag_lw = False
    for i in set(password):
        if str(i).islower():
            flag_lw = True
            break
    return flag_lw


def islegal(username):
    flag = -1
    for c in range(len(username)):
        if not username[c].isalnum() and username[c] != '_':
            flag = c
    return flag


def check_uname(u_name):
    try:
        if len(u_name) < 3:
            raise UsernameTooShort(u_name)
        elif len(u_name) > 16:
            raise UsernameTooLong(u_name)
        elif islegal(u_name) >= 0:
            raise UsernameContainsIllegalCharacter(u_name, islegal(u_name))
    except Exception as error:
        print(error)
    else:
        return True


def check_pass(password):
    try:
        if len(password) < 8:
            raise PasswordTooShort(password)
        elif len(password) > 40:
            raise PasswordTooLong(password)
        elif not isupper(password):
            raise Uppercase(password)
        elif not islower(password):
            raise Lowercase(password)
        elif digits(password) < 0:
            raise Digit(password)
        elif special_note(password) < 0:
            raise Special(password)

    except Exception as error:
        print(error.__str__())
    else:
        return True


def check_input(username, password):
    if check_uname(username) and check_pass(password):
        print('OK')


def main():
    input_list = [
        ("1", "2"),
        ("0123456789ABCDEFG", "2"),
        ("A_a1.", "12345678"),
        ("A_1", "2"),
        ("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary"),
        ("A_1", "abcdefghijklmnop"),
        ("A_1", "ABCDEFGHIJLKMNOP"),
        ("A_1", "ABCDEFGhijklmnop"),
        ("A_1", "4BCD3F6h1jk1mn0p"),
        ("A_1", "4BCD3F6.1jk1mn0p")
    ]
    for param1, param2 in input_list:
        check_input(param1, param2)


main()
