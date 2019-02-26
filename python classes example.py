
class car():

    wheel=5  #class variable - static

    def __init__(self):
        self.brand='Toyoto'   # instance variable
        self.type='zeep'
        self.price=800000


c1=car()
c2=car()

c1.type='SUV'
car.wheel=3

print(c1.brand,c1.type,c1.price,c1.wheel)

print(c2.brand,c2.type,c2.price,c2.wheel)
