class Fan:
    SLOW = 1 
    MEDIUM = 2
    FAST = 3
    
    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed = speed
        self.__radius = float(radius)
        self.__color = str(color).lower()
        self.__on = bool(on)
    
    @property
    def speed(self):return self.__speed
    @speed.setter
    def speed(self, value): self.__speed = value

    @property
    def on(self):return self.__on
    @on.setter
    def on(self, value): self.__on = bool(value)

    @property
    def radius(self): return self.__radius
    @radius.setter
    def radius(self, value): self.__radius = float(value)

    @property
    def color(self):return self.__color
    @color.setter
    def color(self, value): self.__color = str(value).lower()
    
    def display_properties(self, fan_name):
        YELLOW = "\033[93m"
        BLUE = "\033[94m"
        VIOLET = "\033[95m"
        RESET = "\033[0m"
        BOLD = "\033[1m"

        text_color = RESET
        if self.__color == "yellow":
            text_color = YELLOW
        elif self.__color == "blue":
            text_color = BLUE
        elif self.__color == "violet":
            text_color = VIOLET

        print(f"{text_color}{BOLD}--- {fan_name} properties ---{RESET}")
        print(f"{text_color}speed: {self.__speed}{RESET}")
        print(f"{text_color}radius: {self.__radius}{RESET}")
        print(f"{text_color}color: {self.__color}{RESET}")
        print(f"{text_color}status: {'ON' if self.__on else 'OFF'}{RESET}")
        print(f"{text_color}---------------------------------------------{RESET}\n")