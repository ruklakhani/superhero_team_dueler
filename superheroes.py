import random
import os

class Ability:
    def __init__(self, name, attack_power):
        '''Create Instance Variables:
        name: str
        max_damage: int'''
        self.name = name
        self.attack_power = attack_power

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0, self.attack_power)


class Weapon(Ability):
    def __init__(self, name, attack_power):
        super().__init__(name, attack_power)

    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use what you learned to complete this method.
        damage = random.randint(0, self.attack_power)
        return damage // 2


class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)


class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer'''
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        '''add ability to list'''
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int'''
        count = 0
        for ability in self.abilities:
            count += ability.attack()
            return count

    def add_armor(self, armor):
        '''Add armor to self.armors Armor: Armor Object'''
        self.armors.append(armor)

    def defend(self, damage_amount):
        count = 0
        for armor in self.armors:
            block_int = int(armor.block())
            count += block_int
        return count + damage_amount

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
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

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

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

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            my_hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            my_hero.fight(opponent)

            if my_hero.is_alive():
                living_opponents.remove(opponent)
            else:
                living_heroes.remove(my_hero)

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        ability_name = input("Ability Name:")
        ability_damage = int(input("Ability Damage:"))
        return Ability (ability_name, ability_damage)

    def create_weapon(self):
        weapon_name = input("Weapon Name:")
        weapon_damage = int(input("Weapon Damage:"))
        return Weapon(weapon_name, weapon_damage)

    def create_armor(self):
        armor_name = input("Armor name:")
        armor_amount = int(input("Armor block amount:"))
        return Armor(armor_name, armor_amount)

    def create_hero(self):
        name = input("Enter a Hero name: ")
        new_Hero = Hero(name, starting_health = 100)
        equip_ability = input("Do you want a random ability? y or no: ")
        equip_weapon = input("Do you want a random weapon? y or no: ")
        equip_armor = input("Do you want random armor? y or no: ")
        if equip_ability == "y":
            new_Hero.add_ability(self.create_ability())
        if equip_weapon == "y":
            new_Hero.add_weapon(self.create_weapon())
        if equip_armor == "y":
            new_Hero.add_armor(self.create_armor())
        return new_Hero

    def build_team_one(self):
        team_name = input("Enter a Team 1 name:")
        team_one = Team(team_name)
        num_of_heroes = int(input("Enter a number of heroes:"))
        for i in range(num_of_heroes):
             hero = self.create_hero()
             team_one.add_hero(hero)
        self.team_one = team_one
    def build_team_two(self):
        team_name = input("Enter a Team 2 name:")
        team_two = Team(team_name)
        num_of_heroes = int(input("Enter a number of heroes:"))
        for i in range(num_of_heroes):
             hero = self.create_hero()
             team_two.add_hero(hero)
        self.team_two = team_two

    def team_battle(self):
            self.team_one.attack(self.team_two)


    def if_team_dead(self, TeamAlive):
        TeamDeaths = 0
        for hero in TeamAlive:
            if hero.current_health == 0:
                TeamDeaths += 1
        if TeamDeaths == len(TeamAlive):
            return True
        else:
            return False

    def show_stats(self):
        teamA = self.if_team_dead(self.team_one.heroes)
        teamB = self.if_team_dead(self.team_two.heroes)

        if teamA == False:
            print(f"Victor is Team {self.team_two.name}")
            print("The Survivors are: ")
            for hero in self.team_one.heroes:
                if hero.is_alive():
                    print(hero.name)
        elif teamB == False:
            print(f"Victor is Team {self.team_one.name}")
            print("The Survivors are: ")
            for hero in self.team_two.heroes:
                if hero.is_alive():
                    print({hero.name})
                else:
                    print("uh yikes... nobody")
        elif teamA == False and teamB == False:
            print("DRAW!")

        print(f'Team One KDR: {self.team_one.stats()}')
        print(f'Team Two KDR: {self.team_two.stats()}')

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()