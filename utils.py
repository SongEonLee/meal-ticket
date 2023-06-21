import threading

from exception import NoInputException, BlankException, NotIntegerException


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Util(Singleton):
    @staticmethod
    def check_input_have_value(value):
        if not value:
            raise NoInputException()
        elif value.isspace():
            raise BlankException()

    @staticmethod
    def check_is_digit(value):
        Util.check_input_have_value(value)
        if not value.isdigit():
            raise NotIntegerException()