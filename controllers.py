from datetime import time

from exception import InvalidCodeException, InvalidPasswordException, NotIntegerException
from models import Account, MealTime, Restaurant
from utils import Util, Singleton


class AccountController(Singleton):
    admin_password = 'admin'

    # 사용자 객체 생성
    @staticmethod
    def input_user():
        username = input()
        while True:
            try:
                Util.check_input_have_value(username)
                user = Account(username)
                break
            except Exception as e:
                print(e)
        return user

    @staticmethod
    def check_admin_password(input_pw):
        if input_pw != AccountController.admin_password:
            raise InvalidPasswordException()


class RestaurantController(Singleton):
    # 식당 선택
    @staticmethod
    def choose_restaurant(selected_restaurant_code):
        while True:
            try:
                Util.check_is_digit(selected_restaurant_code)
                selected_restaurant = next(
                    (r for r in RestaurantController.get_all_restaurant() if r.is_selected_restaurant(int(selected_restaurant_code))), None)
                if selected_restaurant is None:
                    raise InvalidCodeException()
                break
            except Exception as e:
                print(e)
        return selected_restaurant

    @staticmethod
    def get_all_restaurant():
        return Restaurant.get_all()


class MenuController(Singleton):
    # 메뉴 선택
    @staticmethod
    def choose_menu(cur_menu_in_selected_restaurant):
        while True:
            selected_menu_code = input()
            try:
                Util.check_is_digit(selected_menu_code)
                selected_menu = next(
                    (m for m in cur_menu_in_selected_restaurant if m.is_selected_menu(int(selected_menu_code))), None)
                if selected_menu is None:
                    raise InvalidCodeException()
                break
            except Exception as e:
                print(e)
        return selected_menu

    @staticmethod
    def get_cur_menu_list(current, selected_restaurant):
        return [m for m in selected_restaurant.menu if m.time == current]


class TimeController(Singleton):
    @staticmethod
    def change_meal_time():
        meat_time = MealTime()
        print(meat_time)
        breakfast_start = meat_time.breakfast_start
        breakfast_end = meat_time.breakfast_end
        lunch_start = meat_time.lunch_start
        lunch_end = meat_time.lunch_end
        dinner_start = meat_time.dinner_start
        dinner_end = meat_time.dinner_end

        time_num = input()
        Util.check_input_have_value(time_num)
        try:
            if int(time_num) == 1:
                hour = int(input(f'{breakfast_start} 변경할 시간을 정시 숫자로 입력해주세요. '))
                meat_time.breakfast_start = time(hour, 0)
            elif int(time_num) == 2:
                hour = int(input(f'{breakfast_end} 변경할 시간을 정시 숫자로 입력해주세요. '))
                meat_time.breakfast_end = time(hour, 0)
            elif int(time_num) == 3:
                hour = int(input(f'{lunch_start} 변경할 시간을 정시 숫자로 입력해주세요. '))
                meat_time.lunch_start = time(hour, 0)
            elif int(time_num) == 4:
                hour = int(input(f'{lunch_end} 변경할 시간을 정시 숫자로 입력해주세요. '))
                meat_time.lunch_end = time(hour, 0)
            elif int(time_num) == 5:
                hour = int(input(f'{dinner_start} 변경할 시간을 정시 숫자로 입력해주세요. '))
                meat_time.dinner_start = time(hour, 0)
            elif int(time_num) == 6:
                hour = int(input(f'{dinner_end} 변경할 시간을 정시 숫자로 입력해주세요. '))
                meat_time.dinner_end = time(hour, 0)
            else:
                raise InvalidCodeException()
        except ValueError:
            raise NotIntegerException
