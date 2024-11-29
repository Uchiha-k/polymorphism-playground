# Base class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"Calling {number} using {self.brand} {self.model}...")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")

# Derived class (inheritance)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, is_water_resistant):
        super().__init__(brand, model, price)
        self.is_water_resistant = is_water_resistant

    def track_steps(self, steps):
        print(f"Tracking {steps} steps on {self.brand} {self.model}.")
    
    def info(self):
        super().info()
        print(f"Water Resistant: {'Yes' if self.is_water_resistant else 'No'}")

# Create instances
phone = Smartphone("Apple", "iPhone 15", 1200)
watch = Smartwatch("Samsung", "Galaxy Watch 6", 400, True)

# Call methods
phone.info()
phone.call("123456789")
watch.info()
watch.track_steps(5000)
