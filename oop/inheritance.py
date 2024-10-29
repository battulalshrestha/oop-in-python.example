class Car:
    def __init__(self,age,brand):
        print("nice you bought the car:")
        self.age = age
        self.brand= brand
    def start(self):
        print("Brand:",self.brand,"owwww","you can drive now")
# inheritance the car by taking above class (Car):
# parent saga vayeko saman sabbai children le lagne
class Brandcar(Car):
    def start(self):
       # super().start()
        print("start with the your brand new car:")
    

class ElectricCar(Car):
    def start(self):
     super().start()
     print("start with the your electric car")
     
    
# your_car= Brandcar(age =12,brand= "toyata")
# print(your_car.start())
# your_friend_car = ElectricCar(age = 49,brand="tesla")
# print(your_friend_car.start())
# your_car = ElectricCar(age=12,brand="bolero")
# print(your_car.start())

your_new_car =Brandcar(age = 30,brand="newbrand")
print(your_new_car.start())