class Superhero:
    def __init__(self, name, alias):
        self.name = name
        self.alias = alias
        self.__power_level = 100  # private attribute

    def get_power_level(self):
        return self.__power_level

    def train(self):
        self.__power_level += 10
        print(f"{self.alias} trains hard! Power level is now {self.__power_level}.")

    def use_power(self):
        print(f"{self.alias} uses a generic superpower!")

class FlyingHero(Superhero):
    def __init__(self, name, alias, flight_speed):
        super().__init__(name, alias)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.alias} soars through the skies at {self.flight_speed} km/h!")

class StrengthHero(Superhero):
    def __init__(self, name, alias, max_lift):
        super().__init__(name, alias)
        self.max_lift = max_lift

    def use_power(self):
        print(f"{self.alias} lifts {self.max_lift} tons effortlessly!")
