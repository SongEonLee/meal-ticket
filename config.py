from controllers import RestaurantController, AccountController, MenuController, TimeController
from models import MealTime
from utils import Singleton


class AppConfig(Singleton):

    def __init__(self):
        self.restaurant_controller = RestaurantController()
        self.account_controller = AccountController()
        self.menu_controller = MenuController()
        self.meal_time = MealTime()

    def get_restaurant_controller(self):
        return self.restaurant_controller

    def get_account_controller(self):
        return self.account_controller

    def get_menu_controller(self):
        return self.menu_controller

    def get_meal_time(self):
        return self.meal_time

