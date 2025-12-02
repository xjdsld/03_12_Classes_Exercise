import random
from abc import ABC, abstractmethod


class HERO(ABC):

    def __init__(self):
        self.name = ''
        self.hero_money = random.randint(1, 100)
        self.hero_strength = 0
        self.hero_dextrexity = 0
        self.hero_magic_skills = 0

    def hero_name(self):
        self.name = input('Please enter the hero name:')

    @abstractmethod
    def hero_stats(self):
        pass


class Strengh(HERO):

    def hero_stats(self):
        self.hero_strenght = random.randint(0, 100)
        print(f"{self.name}'s strenght is {self.hero_strenght}")

class Dextrexity(HERO):

    def hero_stats(self):
        self.hero_dextrexity = random.randint(0, 100)
        print(f"Your Hero's dextrexity is {self.hero_dextrexity}")


class Magic_skills(HERO):

    def hero_stats(self):
        self.hero_magic_skills = random.randint(0, 100)
        print(f"{self.name}'s magic skills level is { self.hero_magic_skills}")


class Magic(HERO):

    def magic_power(self, hero):
        hero.magic_skills += 15
        print(
            f"{self.name}'s magic skills were boosted and now are {hero.magic.skills}"
        )