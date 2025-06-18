from abc import ABC, abstractmethod

class AnimAkl(ABC):


    # abstract method:
    
    def move(self):
        pass

# sub class

class Human(AnimAkl):


    def move(self):
        print("I can walk and run")

class snake(AnimAkl):

    def move(self):
        print("I can crawl")

class lion(AnimAkl):

    def move(self):
        print("I can roar!")

class Dog():

    def move(self):
        print("I can bark")


# driver code:

R = Human()
R.move()

K = snake()
K.move()

R = Dog()
R.move()

K = lion()
K.move()