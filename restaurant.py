from error import WrongInput


class Restaurant:
    def __init__(self, code, name, menu):
        self.code = code
        self.name = name
        self.menu = menu

    def is_restaurant_by_code(self, code):
        return self.code == code


class Menu:
    def __init__(self, code, name, price, time):
        self.code = code
        self.name = name
        self.price = price
        self.time = time

    def is_selected_menu(self, code):
        return self.code == code
