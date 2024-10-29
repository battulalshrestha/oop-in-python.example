# function based polymerphism in python 
# consider two distinct class Bear and the dog . each of this class has a method that produce a unique sound.
# using polymerphism , we can invoke the respective sound method for any object 
# of these classes though a common function 

# class Bear(object):
#     def sound(self):
#         print("ghoor")
# class Dog(object):
#     def sound(self):
#         print("woof woof")
     
# def makesound(animaltype):
#     animaltype.sound()
# bearobj = Bear()
# dogobj = Dog()
# print(bearobj.sound())
# print(dogobj.sound())



# class Document:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         raise NotImplementedError("subclass must implement this abstract method:")
# class pdf(Document):
#     def show(self):
#         return "show pdf file"
# class Word(Document):
#     def show(self):
#         return "show word file"
# documents = [pdf("document1"),pdf("document2"),Word("document3")]
# for document in documents:
#     print(document.name + ":" +document.show())








# class Grandpa:
#     def __init__(self,name,):
#         self.name = name
#         # self.age =age
    
#     def call_grandpa(self):
#         raise NotImplementedError("The subclass of the grandpa is son and daughter below")
        
# class Son(Grandpa):
#     def call_grandpa(self):
#         return "can i call you, hi my grandpa son"
# class Daughter(Grandpa):
#     def call_grandpa(self):
#         return "can i call you , hi my grandpa daughter"
# grandpapa = [Son("grandpapa1"), Son("grandapapa2"),Daughter("grandpapa3")]
# for i in grandpapa:
#     print(i.name + ":" + i.call_grandpa())

# print(i.name)
    

'''
an abstract  class car , could be define methods like 
drive() and stop() . the implimentation of these method can 
then differ based on the specific type of car (like Sportscar or truck)

'''
class Car:
    def __init__(self,name):
        self.name = name
# call_name = Car(name = "nishan")
# print(call_name.name)
# print(Car) <class '__main__.Car'>

def drive(self):
    raise NotImplementedError("dont raise the any error .it cannnot be implemented")

def stop(self):
    raise NotImplementedError("it can also be implemented")


class Sportscar(Car):
    def drive(self):
        return 'Sportscar driving!'

    def stop(self):
        return 'Sportscar braking!'

class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'

    def stop(self):
        return 'Truck braking!'

cars = [Truck('Bananatruck'), Truck('Orangetruck'), Sportscar('Z3')]

for car in cars:
    print(car.name + ': ' + car.drive())