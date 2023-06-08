from exception import check_input_have_value


class Account:

    def __init__(self, name):
        self.name = name

    # 사용자 객체 생성
    @staticmethod
    def input_user():
        username = input()
        while True:
            try:
                check_input_have_value(username)
                user = Account(username)
                break
            except Exception as e:
                print(e)
        return user
