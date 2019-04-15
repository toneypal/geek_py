# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:

    def __init__(self, speed, color, name, is_police):
        self.speed = 210
        self.color = 'blue'
        self.name = 'BMW'
        self.is_police = False

    def go(self):
        go = False

    def stop(self):
        stop = False

    def turn(self):
        turn = 'left'


class SportCar:

    def __init__(self, speed, color, name, is_police):
        self.speed = 350
        self.color = 'red'
        self.name = 'Mitsubishi'
        self.is_police = False

        def go(self):
            go = False

        def stop(self):
            go = False

        def turn(self):
            turn = 'left'


class WorkCar:

    def __init__(self, speed, color, name, is_police):
        self.speed = 90
        self.color = 'grey'
        self.name = 'Kia Rio'
        self.is_police = False

        def go(self):
            go = False

        def stop(self):
            stop = False

        def turn(self, turn):
            turn = 'left'

class PoliceCar:

    def __init__(self, speed, color, name, is_police):
        self.speed = 180
        self.color = 'white'
        self.name = 'VAZ Patriot'
        self.is_police = True

        def go(self):
            go = False

        def stop(self):
            stop = False

        def turn(self):
            turn = 'left'
