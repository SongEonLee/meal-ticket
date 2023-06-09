class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return '**' + self.msg + '**' + '\n'


class NotIntegerException(CustomException):
    def __init__(self, msg='정수만 입력해주세요'):
        super().__init__(msg)


class NotMealTimeException(CustomException):
    def __init__(self, msg='식사시간이 아닙니다'):
        super().__init__(msg)


class BlankException(CustomException):
    def __init__(self, msg='공백일 수 없습니다'):
        super().__init__(msg)


class NoInputException(CustomException):
    def __init__(self, msg='값을 입력해주세요'):
        super().__init__(msg)


class InvalidCodeException(CustomException):
    def __init__(self, msg='유효하지 않은 번호입니다'):
        super().__init__(msg)


class InvalidPasswordException(CustomException):
    def __init__(self, msg='비밀번호가 틀렸습니다'):
        super().__init__(msg)


def check_input_have_value(value):
    if not value:
        raise NoInputException()
    elif value.isspace():
        raise BlankException()


def check_is_digit(value):
    check_input_have_value(value)
    if not value.isdigit():
        raise NotIntegerException()
