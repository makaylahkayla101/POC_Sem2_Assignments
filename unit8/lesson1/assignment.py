class Car():
    def __init__(self, model, colour, initial_speed=0):
        self.__model = model
        self.colour = colour
        if initial_speed < 0:
            self.__speed = 0
        else:
            self.__speed = initial_speed

    def speed_up(self):
        self.__speed += 5

    def slow_down(self):
        if self.__speed < 5:
            self.__speed = 0
        else:
            self.__speed -= 5

    def show_speed(self):
        print('Current speed:', self.__speed)


my_lovely_cat = Cat('T-Roc', 'red', -50)
my_lovely_cat.show_speed()

my_lovely_car.__speed = 10
print(my_lovely_cat.__speed)

my_lovely_cat.show_speed()