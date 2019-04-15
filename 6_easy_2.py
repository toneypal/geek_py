# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = 210
        self.color = ''
        self.name = ''
        self.is_police = False

        def go(self):
            go = False

        def stop(self):
            stop = False

        def turn(self):
            turn = 'left'




class TownCar(Car):
    super().speed = 210
    super().color = 'blue'
    super().name = 'BMW'
    super().is_police = False

    def go(self):
        go = True


class SportCar(Car):
    super().speed = 350
    super().color = 'red'
    super().name = 'Mitsubishi'
    super().is_police = False

    def stop(self):
        go = True



class WorkCar(Car):
    super().speed = 90
    super().color = 'grey'
    super().name = 'Kia Rio'
    super().is_police = False

    def turn(self, turn):
        turn = 'Wright'


class PoliceCar(Car):
    super().speed = 180
    super().color = 'white'
    super().name = 'VAZ Patriot'
    super().is_police = True

    def turn(self):
        turn = 'Wright'