from Car import Car  # Imports the Car class from Car.py

def main():

    car = Car(2024, "Toyota Supra")
 
    print("=" * 45)
    print("      🚗   ENHANCED CAR SIMULATOR")
    print("=" * 45)
 
    # Using getters to display car info (demonstrating encapsulation)
    print(f"\n   Car  : {car.get_year_model()} {car.get_make()}")
    print(f"   Speed: {car.get_speed()} mph")
    print(f"   Fuel : {car.get_fuel()}L")
    car.status()
 
    print("\n📌 Accelerating 10 times (speed limit: 60 mph)...")
    for i in range(1, 11):
        print(f"\n  [Accelerate #{i}]")
        car.accelerate()
        print(f"     Speed: {car.get_speed()} mph | Fuel: {car.get_fuel()}L")
 
    car.status()
 
    print("\n📌 Braking back to stop...")
    for i in range(1, 11):
        print(f"\n  [Brake #{i}]")
        car.brake()
        print(f"     Speed: {car.get_speed()} mph | Fuel: {car.get_fuel()}L")
 
    car.status()
 
    print("\n📌 Burning through remaining fuel...")
    while car.get_fuel() > 0:
        print(f"\n  [Accelerate]")
        car.accelerate()
        print(f"     Speed: {car.get_speed()} mph | Fuel: {car.get_fuel()}L")
 

    print("\n  [Trying to accelerate with no fuel...]")
    car.accelerate()
 
    print("\n📌 Refueling 30 liters...")
    car.refuel(30)
    car.status()
 
    print("\n  [Accelerating after refuel]")
    car.accelerate()
    print(f"     Speed: {car.get_speed()} mph | Fuel: {car.get_fuel()}L")
    car.status()
 

    print("\n📌 Updating car info using setters...")
    car.set_year_model(2025)
    car.set_make("Nissan GT-R")
    print(f"   Updated Car: {car.get_year_model()} {car.get_make()}")
    car.status()
 
    print("\n✅ Simulation complete!")

if __name__ == "__main__":
    main()