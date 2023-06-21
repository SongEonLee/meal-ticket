import datetime
import json

from exception import NotMealTimeException
from utils import Singleton


class Account:
    def __init__(self, name):
        self.name = name


class Restaurant:
    def __init__(self, code, name, menu):
        self.code = code
        self.name = name
        self.menu = menu

    def is_selected_restaurant(self, code):
        return self.code == code


class Menu:
    def __init__(self, code, name, price, time):
        self.code = code
        self.name = name
        self.price = price
        self.time = time

    def is_selected_menu(self, code):
        return self.code == code


menu = []
restaurants = []

with open('./resource/menu.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for item in data:
        menu.append(Menu(item['code'], item['name'], item['price'], item['time']))

with open('./resource/restaurants.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for item in data:
        restaurant_menu = [m for m in menu if m.code in item['menu_id']]
        restaurants.append(Restaurant(item['code'], item['name'], restaurant_menu))


class MealTime(Singleton):
    breakfast_start = datetime.time(7, 0)
    breakfast_end = datetime.time(10, 0)
    lunch_start = datetime.time(11, 0)
    lunch_end = datetime.time(14, 0)
    dinner_start = datetime.time(18, 0)
    dinner_end = datetime.time(20, 0)

    def get_current_meal_time(self, current_time):
        if self.breakfast_start <= current_time <= self.breakfast_end:
            return "아침"
        elif self.lunch_start <= current_time <= self.lunch_end:
            return "점심"
        elif self.dinner_start <= current_time <= self.dinner_end:
            return "저녁"
        else:
            raise NotMealTimeException()
