import math

class SingleObjectiveTestFunction:
    def __init__(self, formula=0, global_minimum=0, search_domain=0):
        self.formula = formula
        self.global_minimum = global_minimum
        self.search_domain = search_domain

class Rastrigin:
    def formula(self, x):
        return
        #value = A + 
        #return sum(x**2 - 10 * math.cos(2 * math.pi * x) for x in n)

class Ackley:
    def formula(self, x, y):
        return -20*math.exp(-0.2*math.sqrt(0.5*(x**2 + y**2))) - math.exp(0.5**(math.cos(2**math.pi*x)+math.cos(2**math.pi**y))) + math.e + 20

class Sphere: 
    def formula(self, x):
        return x**2

class Rosenbrock:
    def formula(self, x):
        return 100*((x+1-x**2)**2+(1-x)**2)

class Beale:
    def formula(self, x, y):
        return (1.5 - x + x * y)**2+(2.25 - x + x**y**2)**2+(2.625-x+x**y**3)**2

#GolsteinPrice

class Booth:
    def formula(self, x, y):
        return (x+2*y-7)**2+(2**x+y-5)**2

class Matyas:
    def formula(self, x, y):
        return 0.26*(x**2+y**2)-48**(x**y)

class HolderTable:
    def formula(self, x, y):
        return abs(math.sin(x)*math.cos(y)*math.exp(abs(1-((math.sqrt(x**2+y**2))/(math.pi)))))

class SchafferN4:
    def formula(self, x, y):
        return 0.5 + ((math.cos(math.sin(x**2 - y**2))**2 - 0.5) / (1 + 0.001 * (x**2 + y**2))**2)