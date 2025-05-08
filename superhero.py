# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self._power = power  # Protected attribute
        self.city = city

    def introduce(self):
        return f"I am {self.name}, protector of {self.city}!"

    def use_power(self):
        return f"{self.name} uses {self._power}!"

# Subclass
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} flies at {self.flight_speed} km/h!"

    # Polymorphism: override use_power
    def use_power(self):
        return f"{self.name} soars through the skies using {self._power}!"
    
    #Example
    hero1 = Superhero("ShadowBlade", "Invisibility", "Gotham")
    hero2 = FlyingSuperhero("Skyhawk", "Wind Gust", "Metropolis", 500)

    print(hero1.introduce())
    print(hero1.use_power())

    print(hero2.introduce())
    print(hero2.fly())
    print(hero2.use_power())

#Activity 2: Polymorphism Challenge! 🎭
class Vehicle:
    def move(self):
        print("The vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

#Example
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each one prints its own move style
