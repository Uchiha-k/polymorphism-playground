# Base class
class Mover:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Animal class
class Dog(Mover):
    def move(self):
        print("Running on all fours 🐾")

class Bird(Mover):
    def move(self):
        print("Flying in the sky 🕊️")

# Vehicle class
class Car(Mover):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Mover):
    def move(self):
        print("Flying through the air ✈️")

# Create instances and call move()
movers = [Dog(), Bird(), Car(), Plane()]

for mover in movers:
    mover.move()
