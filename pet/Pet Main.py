from pet import Pet


def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("  ⚠️  Please enter a whole number.")


def main():
    print("=" * 45)
    print("       🐾  PET PROFILE CREATOR")
    print("=" * 45)

   
    my_pet = Pet()

    print("\n📋 Enter your pet's details:\n")

    name = input("  Pet's name       : ")
    my_pet.set_name(name)

    print(f"  Valid types: {', '.join(Pet.VALID_TYPES)}")
    animal_type = input("  Animal type      : ")
    my_pet.set_animal_type(animal_type)

    age = get_valid_int("  Age (in years)   : ")
    my_pet.set_age(age)

    # Display profile using getters
    print("\n✅ Pet registered! Here is your pet's profile:")
    my_pet.display_profile()

