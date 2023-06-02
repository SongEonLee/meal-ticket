from account import Account
from error import WrongInput


def print_main_menu():
    print('--------식권대장---------\n'
          '1. 식사하기\n'
          '2. 식사 시간대 변경하기')
    input_num = input('원하는 번호를 선택하세요. : ')
    return int(input_num)


def input_user(cur_time):
    print(cur_time, '식사시간, 당신의 이름을 입력하세요')

    username = input()
    return Account(username)


def choose_restaurant(user, restaurants):
    print(user.name, '님, 식당번호를 선택하세요')
    for r in restaurants:
        print(r.code, '.', r.name)

    selected_restaurant_code = int(input())

    # 선택한 식당 객체 찾기
    selected_restaurant = None
    for r in restaurants:
        if r.is_restaurant_by_code(selected_restaurant_code):
            selected_restaurant = r
            break
    if selected_restaurant is None:
        raise WrongInput
    return selected_restaurant


def choose_menu(current, cur_menu_in_selected_restaurant):
    print(current, '메뉴 번호를 선택하세요.')
    for m in cur_menu_in_selected_restaurant:
        print(m.code, '.', m.name, m.price, '원')

    selected_menu_code = int(input())

    for m in cur_menu_in_selected_restaurant:
        if m.is_selected_menu(selected_menu_code):
            print(m.price, '원이 결제되었습니다.')
            break
    else:
        raise WrongInput
