import datetime

from exception import NotMealTimeException, InvalidCodeException, check_input_have_value, InvalidPasswordException


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
            raise NotMealTimeException()

    def change_meal_time(self):
        input_pw = input('관리자 비밀번호를 입력하세요. ')

        if input_pw != self.admin_password:
            raise InvalidPasswordException()

        print('변경할 시간대의 번호를 입력해주세요.\n'
              '1. breakfast_start\n'
              '2. breakfast_end\n'
              '3. lunch_start\n'
              '4. lunch_end\n'
              '5. dinner_start\n'
              '6. dinner_end')

        time_num = input()
        check_input_have_value(time_num)
        if int(time_num) == 1:
            hour = int(input(f'{self.breakfast_start} 변경할 시간을 정시 숫자로 입력해주세요. '))
            self.breakfast_start = datetime.time(hour, 0)
        elif int(time_num) == 2:
            hour = int(input(f'{self.breakfast_end} 변경할 시간을 정시 숫자로 입력해주세요. '))
            self.breakfast_end = datetime.time(hour, 0)
        elif int(time_num) == 3:
            hour = int(input(f'{self.lunch_start} 변경할 시간을 정시 숫자로 입력해주세요. '))
            self.lunch_start = datetime.time(hour, 0)
        elif int(time_num) == 4:
            hour = int(input(f'{self.lunch_end} 변경할 시간을 정시 숫자로 입력해주세요. '))
            self.lunch_end = datetime.time(hour, 0)
        elif int(time_num) == 5:
            hour = int(input(f'{self.dinner_start} 변경할 시간을 정시 숫자로 입력해주세요. '))
            self.dinner_start = datetime.time(hour, 0)
        elif int(time_num) == 6:
            hour = int(input(f'{self.dinner_end} 변경할 시간을 정시 숫자로 입력해주세요. '))
            self.dinner_end = datetime.time(hour, 0)
        else:
            raise InvalidCodeException()
