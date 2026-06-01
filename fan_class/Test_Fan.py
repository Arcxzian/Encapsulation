from fan import Fan

def Testfan():
    fan1 = Fan(speed=Fan.FAST, radius=10.0, color='yellow', on=True)
    fan2 = Fan(speed=Fan.MEDIUM, radius=5.0, color='blue', on=False)

    fan1.display_properties("Fan 1")
    fan2.display_properties("Fan 2")

if __name__ == "__main__":
    Testfan()