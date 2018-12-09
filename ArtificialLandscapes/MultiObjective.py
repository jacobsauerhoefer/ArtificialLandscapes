class BinhAndKorn:
    def __init__(self):
        self.functions = []
        self.functions.append(self.f1)
        self.functions.append(self.f2)

        self.constraints = []
        self.constraints.append(self.g1)
        self.constraints.append(self.g2)

        self.search_domain_x = [0, 5]
        self.search_domain_y = [0, 3]

    def f1(self, x, y):
        return 4*(x**2)+4*(y**2)
    
    def f2(self, x, y):
        return (x - 5)**2+(y-5)**2

    def g1(self, x, y):
        return (x-5)**2+y**2 <= 25

    def g2(self, x, y):
        return (x-8)**2+(y+3)**2 >= 7.7



class Schaffer:
    def f1(self, x):
        return -x**2
    def f2(self, x):
        return -(x-2)**2