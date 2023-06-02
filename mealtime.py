import datetime


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MealTime(Singleton):
    admin_password = 'admin'

    def __init__(self):
        self.breakfast_start = datetime.time(7, 0)
        self.breakfast_end = datetime.time(10, 0)
        self.lunch_start = datetime.time(11, 0)
        self.lunch_end = datetime.time(14, 0)
        self.dinner_start = datetime.time(18, 0)
        self.dinner_end = datetime.time(20, 0)

    def get_current_meal_time(self, current_time):
        if self.breakfast_start <= current_time <= self.breakfast_end:
            return "아침"
        elif self.lunch_start <= current_time <= self.lunch_end:
            return "점심"
        elif self.dinner_start <= current_time <= self.dinner_end:
            return "저녁"
        else:
            raise Exception('식사시간이 아닙니다.')

    def change_meal_time(self):
        input_pw = input('관리자 비밀번호를 입력하세요. ')

        if input_pw != self.admin_password:
            raise ValueError('비밀번호가 틀렸습니다.')

        print('변경할 시간대의 번호와 변경할 시간(정시기준)을 숫자만 입력해주세요.\n'
              '1. breakfast_start\n'
              '2. breakfast_end\n'
              '3. lunch_start\n'
              '4. lunch_end\n'
              '5. dinner_start\n'
              '6. dinner_end')

        time_num, hour = input().split()
        if int(time_num) == 1:
            self.breakfast_start = datetime.time(int(hour), 0)
        elif int(time_num) == 2:
            self.breakfast_end = datetime.time(int(hour), 0)
        elif int(time_num) == 3:
            self.lunch_start = datetime.time(int(hour), 0)
        elif int(time_num) == 4:
            self.lunch_end = datetime.time(int(hour), 0)
        elif int(time_num) == 5:
            self.dinner_start = datetime.time(int(hour), 0)
        elif int(time_num) == 6:
            self.dinner_end = datetime.time(int(hour), 0)
        else:
            raise ValueError('입력이 올바르지 않습니다.')


