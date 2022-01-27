class Creature:
    name = None
    age = None
    energy = None
    frozen = False

    def check_energy(self):
        print(f"{self.name} has {self.energy} energy.")

    def freeze(self, creature):
        if(self.energy >= 150):
            creature.frozen = True
            print(f"{self.name} has frozen {creature.name}")
            self.energy -= 150
        else:
            print("Not enough energy!")

    def restore(self, creature):
        creature.frozen = False
        print(f"{self.name} has restored {creature.name}")
        

    def __init__(self, name, age, energy):
        self.name = name
        self.age = age
        self.energy = energy

    def introduce(self):
        if not self.frozen:
            print(f"Hey, my name is {self.name}, I am {self.age} years old.")
        else:
            print(f"{self.name} is frozen")

human = Creature("Anna", 15, 0)
human.introduce()

skolens = Creature("Miks", 16, 0)
skolens.introduce()

wizard = Creature("Gandalfs", 24000, 1000)
wizard.introduce()
wizard.check_energy()

witch = Creature("Medusa", 400, 200)
witch.freeze(human)
witch.check_energy()
human.introduce()
wizard.restore(human)
human.introduce()
witch.freeze(human)
