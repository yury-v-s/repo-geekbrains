# Task 1

from time import sleep


class TrafficLight:
    __color = "Multicolor"

    def running(self):
        i = 0
        while i < 3:
            print('Red')
            sleep(7)
            print('Yellow')
            sleep(2)
            print('Green')
            sleep(7)
            i += 1


trafficLight = TrafficLight()
trafficLight.running()


# Task 2


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def summary(self):
        return (self._length * self._width * 25 * 5) / 1000


road_1 = Road(5000, 20)
print(road_1.summary())


# Task 3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_proffit(self):
        return f'{sum(self._income.values())}'


staff = Position('Святослав', 'Безфамильный', 'Грузчик', 13000, 3299)
print(f'{staff.position} - {staff.get_full_name()} получит {staff.get_full_proffit()} р.')


# Task 4


class Car:
    """General class car"""

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Car: {self.name}({self.color}) is Police - {self.is_police}')

    def run(self):
        print(f'{self.name}: car went')

    def stop(self):
        print(f'{self.name}: car stop')

    def show_speed(self):
        print(f'{self.name}: car speed {self.speed}')


class TownCar(Car):
    """TownCar"""

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Over Speed!' \
            if self.speed > 60 else f'{self.name}: Car speed {self.speed}'


class WorkCar(Car):
    """WorkCar"""

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Over Speed!' \
            if self.speed > 40 else f'{self.name}: Car speed {self.speed}'


class SportCar(Car):
    """SportCar"""

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Over Speed!' \
            if self.speed > 140 else f'{self.name}: Car speed {self.speed}'


class PoliceCar(Car):
    """Police Car"""

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Over Speed!' \
            if self.speed > 80 else f'{self.name}: Car speed {self.speed}'


town_car = TownCar('Towncar', 'Gray', 60)
town_car.run()
print(town_car.show_speed())
town_car.stop()
print()

work_car = WorkCar('Workcar', 'Black', 60)
work_car.run()
print(work_car.show_speed())
work_car.stop()
print()

sport_car = SportCar('Sportcar', 'Red', 120)
sport_car.run()
print(sport_car.show_speed())
sport_car.stop()
print()

police_car = PoliceCar('Police car', 'MultiColor', 160)
police_car.run()
print(police_car.show_speed())
police_car.stop()
print()

# Task 5

# Раскоментировать строку с импортом если будет закомментирован импорт в первом задании
"""from time import sleep"""


class Stationery:
    def __init__(self, title='Color brushes'):
        self.title = title

    def draw(self):
        print(f'Drawing {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'drawing sphere with {self.title} pen!')


class Pencil(Stationery):
    def draw(self):
        print(f'drawing square with {self.title} pencil!')


class Handle(Stationery):
    def draw(self):
        print(f'drawing circle with {self.title} handle!')


drawing = Stationery()
drawing.draw()
sleep(3)
pen = Pen('Black')
pen.draw()
sleep(3)
pencil = Pencil('Red')
pencil.draw()
sleep(3)
handle = Handle('Gold')
handle.draw()
