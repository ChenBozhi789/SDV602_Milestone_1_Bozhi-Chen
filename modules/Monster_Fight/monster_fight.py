class Player:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self):
        pass

    def heal(self):
        pass

    def run(self):
        print("You have escape successfully")

    def is_alive(self):
        pass

class Monster:
    def __init__(self, name, type, health, power):
        self.name = name
        self.type = type
        self.health = health
        self.damage = power

    def attack(self):
        print(f"This Monster attack power is: {self.damage}")

    def getting_attack(self):
        print(f"You just attack monster, the rest of health is {self.health}")

    def is_alive(self):
        return self.health > 0

Tiger = Monster("Tester1", "Dogface", 100, 20)
Lion = Monster("Tester", "General", 500, 50)

Tiger.attack()
Tiger.getting_attack()

if __name__ == "__main__":
    pass