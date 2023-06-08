from exception import InvalidCodeException, check_is_digit


class Menu:
    def __init__(self, code, name, price, time):
        self.code = code
        self.name = name
        self.price = price
        self.time = time

    def is_selected_menu(self, code):
        return self.code == code

    # 메뉴 선택
    @staticmethod
    def choose_menu(current, cur_menu_in_selected_restaurant):
        print(current, '메뉴 번호를 선택하세요.')
        for m in cur_menu_in_selected_restaurant:
            print(m.code, '.', m.name, m.price, '원')

        while True:
            selected_menu_code = input()
            try:
                check_is_digit(selected_menu_code)
                selected_menu = next(
                    (m for m in cur_menu_in_selected_restaurant if m.is_selected_menu(int(selected_menu_code))), None)
                if selected_menu is None:
                    raise InvalidCodeException()
                break
            except Exception as e:
                print(e)
        return selected_menu
