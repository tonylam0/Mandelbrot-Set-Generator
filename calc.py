import numpy
import matplotlib

class Bounds:
    def __init__(self, initial, complex_num, iterations) -> None:
        self.initial = initial
        self.complex_num = complex_num
        self.iterations = iterations
    
    # Iterative formula
    # c represents a complex number 
    def calc(initial, complex_num):
       return initial**2 + complex_num
    
    def draw(points: list):
        pass
