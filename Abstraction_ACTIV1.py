from abc import ABC, abstractmethod

class Absclass(ABC):


    def print(self,x):
        print("passed value: ", x)

    @abstractmethod 
    def task(self):
        print("We are inside absclass task")

# create a sub class:

class test_class(Absclass):
    
    def task(self):
        print("we are inside test_class task")

# obj creation:

test_obj = test_class()
test_obj.task()
test_obj.print(70-2+1)