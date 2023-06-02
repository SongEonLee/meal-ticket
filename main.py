import datetime
import json

from func import *
from mealtime import MealTime, Singleton
from restaurant import Menu, Restaurant

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


class MainService(Singleton):
    @staticmethod
    def start_service():
        try:
            current = time.get_current_meal_time(current_time)
            user = input_user(current)
            selected_restaurant = choose_restaurant(user, restaurants)
            cur_menu_in_selected_restaurant = [m for m in selected_restaurant.menu if m.time == current]
            choose_menu(current, cur_menu_in_selected_restaurant)
        except Exception as e:
            print(e)
            quit()


def main():
    try:
        input_num = print_main_menu()
        if input_num == 1:
            MainService.start_service()
        elif input_num == 2:
            time.change_meal_time()
            main()
        else:
            raise WrongInput
    except Exception as e:
        print(e)


if __name__ == "__main__":
    time = MealTime()
    current_time = datetime.datetime.now().time()
    main()
