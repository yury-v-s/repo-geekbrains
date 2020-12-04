# Task 1

from time import sleep


class TrafficLight:
    __color = ""

    def running(self):
        while True:
            print('Red')
            sleep(7)
            print('Yellow')
            sleep(2)
            print('Green')
            sleep(7)


trafficLight = TrafficLight()
trafficLight.running()
