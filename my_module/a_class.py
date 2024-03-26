import numpy as np


class my_class:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def print(self):
        print(self._name,self._age)

class my_derived_class(my_class):
    def __init__(self,name,age,surname):
        self._name=name
        self._age=age
        self._surname=surname