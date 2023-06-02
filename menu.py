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

        selected_menu_code = int(input())

        for m in cur_menu_in_selected_restaurant:
            if m.is_selected_menu(selected_menu_code):
                return m
        else:
            raise ValueError('메뉴코드가 올바르지 않습니다.')