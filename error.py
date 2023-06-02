class WrongInput(Exception):
    def __init__(self):
        super().__init__('잘못된 입력입니다.')
