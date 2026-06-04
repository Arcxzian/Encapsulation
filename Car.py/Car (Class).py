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
        self.__check_fuel_warnings()

    def brake(self):
        if self.__speed == 0:
            print("The car is already stopped.")
            return
        self.__speed = max(self.__speed, - 5, 0)
        self.__speed -= self.FUEL_PER_BREAK
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

    def __check_speed_warnings(self):
        if self.__speed > self.SPEED_LIMIT:
            excess = self.__speed - self.SPEED_LIMIT
            print(f"  🚨 SPEED WARNING! {self.__speed} mph — {excess} mph over the {self.SPEED_LIMIT} mph limit!")
        elif self.__speed == self.SPEED_LIMIT:
            print(f"  ⚠️  At speed limit ({self.SPEED_LIMIT} mph). Don't go faster!")
    
    def __check_fuel_warnings(self):
        pct = (self.__fuel / self.FUEL_CAPACITY) * 100
        if self.__fuel == 0:
            print("FUEL EMPTY! Refuel immediately.")
        elif pct <= 20 and "low_fuel" not in self.__warnings:
            print(f"LOW FUEL WARNING! Only {self.__fuel:.1f}L remaining ({pct:.0f}%).")
            self.__warnings.append("low_fuel")
        elif pct > 20 and "low_fuel" in self.__warnings:
            self.__warnings.remove("low_fuel")
    
    def status(self):
        fuel_bar = self.__fuel_bar()
        speed_indicator = "🚨 OVER LIMIT" if self.__speed > self.SPEED_LIMIT else "✅ OK"
        print(f"""
  ┌─────────────────────────────────┐
  │  {self.__year_model} {self.__make:<22}│
  │  Speed : {self.__speed:>3} mph  [{speed_indicator}]   │
  │  Fuel  : {fuel_bar} {self.__fuel:>5.1f}L  │
  └─────────────────────────────────┘""")
    def __fuel_bar(self): 
            filled = int((self.__fuel / self.FUEL_CAPACITY) * 10)
            return "[" + "█" * filled + "░" * (10 - filled) + "]"
