class Restaurant:
    def __init__(self, code, name, menu):
        self.code = code
        self.name = name
        self.menu = menu

    def is_selected_restaurant(self, code):
        return self.code == code

    # 식당 선택
    @staticmethod
    def choose_restaurant(restaurants):
        for r in restaurants:
            print(r.code, '.', r.name)

        selected_restaurant_code = int(input())

        selected_restaurant = None
        for r in restaurants:
            if r.is_selected_restaurant(selected_restaurant_code):
                selected_restaurant = r
                break
        if selected_restaurant is None:
            raise ValueError('식당코드가 올바르지 않습니다.')
        return selected_restaurant
