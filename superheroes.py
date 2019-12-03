from random import randint,choice
import random

class Ability:
    def __init__(self, name, attack_strength, max_damage):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
      return random.randint(0,self.attack_strength)

class Weapon(Ability):

if __name__ == "__main__":
    pass 