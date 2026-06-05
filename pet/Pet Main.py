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

    print("\n🎓 Teach your pet some tricks!")
    print("   (Enter a trick name, or press Enter to skip)\n")
    for i in range(1, 4):
        trick = input(f"  Trick #{i}: ")
        if not trick.strip():
            break
        my_pet.teach_trick(trick)
 
    # Vet visit
    print("\n🏥 Taking your pet to the vet...")
    my_pet.visit_vet()
 
    # Birthday simulation
    print("\n🎂 Simulating a birthday...")
    my_pet.birthday()
 
    # Final profile using getters
    print("\n📊 Final summary (via getters):")
    print(f"  Name   : {my_pet.get_name()}")
    print(f"  Type   : {my_pet.get_animal_type()}")
    print(f"  Age    : {my_pet.get_age()} year(s)")
    print(f"  Health : {my_pet.get_health_status()}")
    print(f"  Tricks : {', '.join(my_pet.get_tricks()) if my_pet.get_tricks() else 'None'}")
 
    my_pet.display_profile()
    print("\n✅ Program complete!")
 
 
main()

