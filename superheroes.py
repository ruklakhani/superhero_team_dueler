from random import randint,choice
import random

class Ability:
    def __init__(self, name, max_damage):
        '''Create Instance Variables:
        name: str
        max_damage: int'''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        random_value = random.randint(0,self.max_damage)
        return random_value

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        pass

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer'''
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)
 
    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
            return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors Armor: Armor Object'''
        self.armors.append(armor)

    def defend(self, damage_amt):
        '''Calculate the total block amount from all armor blocks. return: total_block:Int'''
        total_damage = 0 
        for armor in self.armors:
            block_int = int(armor.block())
            total_damage += block_int 
        return total_damage + damage_amt

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minue the defense'''
        hp = self.current_health
        defense = self.defend(damage)
        self.current_health = hp - defense 

    def is_alive(self):
        if self.current_health < 0:
            print(f"{self.name} is dead!")
            return False
        else:
            return True
        pass

    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.'''
        attacking = True
        while attacking:
            if self.is_alive():
                damage = self.attack()
                opponent.take_damage(damage)
                print(f"{self.name} has {self.current_health} health left.")

            else:
                break

            if opponent.is_alive():
                enemy_damage = opponent.attack()
                self.take_damage(enemy_damage)
                print(f"{opponent.name} has {opponent.current_health} health left.")

            else:
                break

class Team(Hero):
    def __init__(self, name, heroes):
        super.__init__(name)
        self.heroes = heroes

    def remove_hero(self, name):
        '''Remove hero from heroes list. If Hero isn't found return 0.'''
        # TODO: Implement this method to remove the hero from the list given their name.
        pass

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman", 500)
    hero2 = Hero("Dumbledore", 500)
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 200)
    ability4 = Ability("Wizard Beard", 350)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)