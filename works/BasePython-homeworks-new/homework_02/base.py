from abc import ABC, abstractmethod
import exceptions

class Vehicle(ABC):
    weight=weightA()
    started= startedA()
    fuel=fuelA()
    fuel_consumption=fuel_consumptionA()

    @abstractmethod
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight=weight
        self.fuel=fuel
        self.fuel_consumption=fuel_consumption

    def move():
        if Vehicle.fuel > 8:
            remaining_fuel=Vehicle.fuel - Vehicle.fuel_consumption     
            print(remaining_fuel)  
        else:
            try:
                Vehicle.fuel > 8
            except exceptions.NotEnoughFuel:
                print("Error")


    def start():
        if Vehicle.started > 1:
            Vehicle.move()
        else: 
            try:
                Vehicle.started < 1
            except exceptions.LowFuelError:
                print('Error')
