
class Account:

    def __init__(self, name):
        self.name = name

    # 사용자 객체 생성
    @staticmethod
    def input_user():
        username = input()
        return Account(username)
