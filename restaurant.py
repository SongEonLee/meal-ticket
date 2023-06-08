from exception import InvalidCodeException, check_is_digit


class Restaurant:
    def __init__(self, code, name, menu):
        self.code = code
        self.name = name
        self.menu = menu

    def is_selected_restaurant(self, code):
        return self.code == code

    # 식당 선택
    @staticmethod
    def choose_restaurant(user, restaurants):
        while True:
            print(user.name, '님, 식당번호를 선택하세요')
            for r in restaurants:
                print(r.code, '.', r.name)
            selected_restaurant_code = input()
            try:
                check_is_digit(selected_restaurant_code)
                selected_restaurant = next(
                    (r for r in restaurants if r.is_selected_restaurant(int(selected_restaurant_code))), None)
                if selected_restaurant is None:
                    raise InvalidCodeException()
                break
            except Exception as e:
                print(e)
        return selected_restaurant


