class Circle:

    def setRadius(self, r):
        self.radius = r

    def create(self, r):
        # c = Circle()
        self.radius = r
        # return c

    def circumference(self):
        return 2*22/7*self.radius

x = Circle()
x.create(7)

print(x.circumference())








