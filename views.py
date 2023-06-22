import datetime

from exception import InvalidCodeException
from utils import Util
from config import AppConfig


class MainView:

    # 기능 출력
    @staticmethod
    def print_main_menu():
        print('--------식권대장---------\n'
              '1. 식사하기\n'
              '2. 식사 시간대 변경하기')
        input_num = input('원하는 번호를 선택하세요. : ')
        Util.check_is_digit(input_num)
        return int(input_num)

    # 메인프로그램 시작
    @staticmethod
    def start_service():
        time = app_config.get_meal_time()
        account_controller = app_config.get_account_controller()
        restaurant_controller = app_config.get_restaurant_controller()
        menu_controller = app_config.get_menu_controller()

        try:
            current = time.get_current_meal_time(current_time)
        except Exception as e:
            print(e)
            main()

        print(current, '식사시간, 당신의 이름을 입력하세요')
        user = account_controller.input_user()

        print(user.name, '님, 식당번호를 선택하세요')
        restaurants = restaurant_controller.get_all_restaurant()
        for r in restaurants:
            print(r.code, '.', r.name)
        selected_restaurant_code = input()
        selected_restaurant = restaurant_controller.choose_restaurant(selected_restaurant_code)  # 식당 선택 로직
        cur_menu_in_selected_restaurant = menu_controller.get_cur_menu_list(current, selected_restaurant)
        print(current, '메뉴 번호를 선택하세요.')
        for m in cur_menu_in_selected_restaurant:
            print(m.code, '.', m.name, m.price, '원')
        selected_menu = menu_controller.choose_menu(cur_menu_in_selected_restaurant)  # 메뉴 선택 로직
        print(selected_menu.price, '원이 결제되었습니다.')
        quit()


class AdminView:

    @staticmethod
    def check_password():
        account_controller = app_config.get_account_controller()
        input_pw = input('관리자 비밀번호를 입력하세요. ')
        account_controller.check_admin_password(input_pw)

    @staticmethod
    def meal_time_change():
        print('변경할 시간대의 번호를 입력해주세요.\n'
              '1. breakfast_start\n'
              '2. breakfast_end\n'
              '3. lunch_start\n'
              '4. lunch_end\n'
              '5. dinner_start\n'
              '6. dinner_end')

        app_config.get_meal_time().change_meal_time()


def main():
    while True:
        try:
            input_num = MainView.print_main_menu()
            if input_num == 1:  # 메인프로그램 시작
                MainView.start_service()
            elif input_num == 2:  # 시간대 변경
                AdminView.check_password()
                AdminView.meal_time_change()
                main()
            else:
                raise InvalidCodeException()
            break
        except Exception as e:
            print(e)


if __name__ == "__main__":
    current_time = datetime.datetime.now().time()
    app_config = AppConfig()
    main()
