class Car:
    SPEED_LIMIT = 60
    FUEL_CAPACITY = 50.0
    FUEL_PER_ACCEL = 2.0
    FUEL_PER_BREAK = 0.5

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        self.__fuel = self.FUEL_CAPACITY
        self.__warnings = []

    def get_year_model(self):
        return self.__year_model
    
    def get_make(self):
        return self.__make
    
    def get_speed(self):
        return self.__speed
    
    def get_fuel(self):
        return round(self.__fuel, 1)
    

    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    def accelerate(self):
        if self.__fuel <= 0:
            print("OUT OF FUEL! cannot accelerate, Please refuel.")
            return
        self.__speed += 5
        self.__fuel -= self.FUEL_PER_ACCEL
        self.__fuel = max(self.__fuel, 0)
        self.__check_fuel_warings()

    def brake(self):
        if self.__speed == 0:
            print("The car is already stopped.")
            return
        self.__speed = max(self.__speed, - 5.0)
        self.speed -= self.FUEL_PER_BREAK
        self.__fuel = max(self.__fuel, 0)
        self.__check_fuel_warnings()
    
    def refuel(self, liters):
        if liters <= 0:
            print("Enter a positive amount of fuel")
            return
        space = self.FUEL_CAPACITY - self.__fuel
        added = min(liters, space)
        self.__fuel += added
        print(f"Refueled {added:.1f} L - Tank: {self.__fuel:.1f}/{self.FUEL_CAPACITY}L")

        
