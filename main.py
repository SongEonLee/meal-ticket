import datetime
import json

from account import Account
from exception import InvalidCodeException, check_is_digit
from mealtime import MealTime, Singleton
from restaurant import Restaurant
from menu import Menu

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

    # 기능 출력
    @staticmethod
    def print_main_menu():
        print('--------식권대장---------\n'
              '1. 식사하기\n'
              '2. 식사 시간대 변경하기')
        input_num = input('원하는 번호를 선택하세요. : ')
        check_is_digit(input_num)
        return int(input_num)

    # 메인프로그램 시작
    @staticmethod
    def start_service():
        try:
            current = time.get_current_meal_time(current_time)  # NotMealTimeException -> main()
        except Exception as e:
            print(e)
            main()

        print(current, '식사시간, 당신의 이름을 입력하세요')
        user = Account.input_user()
        selected_restaurant = Restaurant.choose_restaurant(user, restaurants)
        cur_menu_in_selected_restaurant = [m for m in selected_restaurant.menu if m.time == current]
        selected_menu = Menu.choose_menu(current, cur_menu_in_selected_restaurant)
        print(selected_menu.price, '원이 결제되었습니다.')


def main():
    while True:
        try:
            input_num = MainService.print_main_menu()
            if input_num == 1:  # 메인프로그램 시작
                MainService.start_service()
            elif input_num == 2:  # 시간대 변경
                time.change_meal_time()
                main()
            else:
                raise InvalidCodeException()
            break
        except Exception as e:
            print(e)


if __name__ == "__main__":
    time = MealTime()
    current_time = datetime.datetime.now().time()
    main()
