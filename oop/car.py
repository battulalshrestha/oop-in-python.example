# class Car:
#     uncle_age = 17
#     def start(self):
#       print("oe hllo ")
# your_uncle_car = Car()
# print(your_uncle_car.uncle_age)
# your_uncle_car.start()
# # class Car:
# #     age = 17
# # print(Car.age)






# class World:
#     world_age = 100
#     def start(self):
#         print("start the world")
# worldstart = World()
# # print(worldstart.world_age())  when i called it by making funtion it obviously show the 'int' object is not callable
# # print(World.start) when it print it gives just the location of function of world class
# print(worldstart.start())


# class School:
#     # the life of the school is
#     life = 17
#     brand = "tata"
#     color = "red"
#     def __init__(self,life,brand,color):
#         print("congratulation your life is going on")
#         self.life = life
#         self.brand = brand
#         self.color = color
#     def start_life(self):
#         print("start!","your car is start for ",self.life)
# your_life = School(life=100,brand="pretty",color="green")
# print(your_life.life)
# print(your_life.color)
# #print(your_life.start_life())
# # when the initialization value in the brand is change in the returning value in the self then the printing value in the output is also self value even it also ignore the value of instance initialization 
# your_friend = School(life=60,brand="yoho",color="white")
# print(your_friend.life)

''' Q) suppose a class having the person it has two child class having name 
1) is ram  --> proprties age:24 , college:ncit, address:laitpur
2) is hari --> properties age:12, college:pulchok, address:gorkha 
   '''
# class Person:
#         def __init__(self,name,age,add):
#             self.name = name
#             self.age = age
#             self.add =add
# class Hari(Person):
#     def __init__(self):
#          super().__init__(name="hari", age="22", add="rautepani")
# class Ram(Person):
#     def __init__(self):
#          super().__init__(name ="ram", age ='20', add= "gorkha")
# hello_hari = Hari()
# hello_ram = Ram()
# print(hello_hari.name)
# print(hello_hari.age)
# print(hello_hari.add)
# print(hello_ram.name)
# print(hello_ram.age)
# print(hello_ram.add)


print()
print()

class Person:
   def __init__(self,name,age,address):
     self.name = name
     self.age = age
     self.address = address
   def eat(self):
    print(f"{self.name} is eating")
   def walk(self):
    print(f"{self.age} is walking")
   def run(self):
    print(f'{self.address} is running')
o_ram = Person(name= "ram",age = 22,address = "gorkha")
o_hari = Person(name="hari",age= 12,address="ktm")
print(o_ram.eat)
print(o_hari.run())

