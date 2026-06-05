class Pet:
    VALID_TYPES = ['Dog', 'Cat', 'Bird', 'Rabbit', 'Fish', 'Hamster', 'Turtle']
    MAX_AGE = 100

    def __init__(self, name='Unknown', animal_type='Unknown', age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        self.__tricks = []
        self.__health_status = 'Healthy'

    # ── Setters ──────────────────────────────────────────────
    def set_name(self, name):
        if not name or not name.strip():
            print("  ⚠️  Name cannot be empty.")
            return
        self.__name = name.strip().title()

    def set_animal_type(self, animal_type):
        formatted = animal_type.strip().title()
        if formatted not in self.VALID_TYPES:
            print(f"  ⚠️  '{animal_type}' is not a recognized type.")
            print(f"      Valid types: {', '.join(self.VALID_TYPES)}")
            return
        self.__animal_type = formatted

    def set_age(self, age):
        if not isinstance(age, int) or age < 0:
            print("  ⚠️  Age must be a non-negative whole number.")
            return
        if age > self.MAX_AGE:
            print(f"  ⚠️  Age cannot exceed {self.MAX_AGE}.")
            return
        self.__age = age
        # ── Getters ──────────────────────────────────────────────
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def get_tricks(self):
        return list(self.__tricks)

    def get_health_status(self):
        return self.__health_status

    # ── Extra Features ───────────────────────────────────────
    def teach_trick(self, trick):
        if not trick.strip():
            print("  ⚠️  Trick name cannot be empty.")
            return
        trick = trick.strip().lower()
        if trick in self.__tricks:
            print(f"  🐾 {self.__name} already knows '{trick}'!")
            return
        self.__tricks.append(trick)
        print(f"  🎉 {self.__name} learned a new trick: '{trick}'!")

    def visit_vet(self):
        if self.__age >= 10:
            self.__health_status = 'Needs Check-up'
        else:
            self.__health_status = 'Healthy'
        print(f"  🏥 Vet visit complete. Status: {self.__health_status}")

    def birthday(self):
        self.__age += 1
        print(f"  🎂 Happy Birthday, {self.__name}! Now {self.__age} year(s) old.")


