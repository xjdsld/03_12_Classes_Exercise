import random
from characters import Strengh, Dextrexity, Magic_skills


def user_choice():
    user_hero_choice = input(
        "Chose the core characteristics of the plaery: 1 - for strenght 2 - for dexterxity, 3 - for magix skills:"
    )
    if user_hero_choice == '1':
        return Strengh()
    elif user_hero_choice == '2':
        return Dextrexity()
    elif user_hero_choice == '3':
        return Magic_skills()
    else:
        print("Try again")


player_hero = user_choice()
player_hero.hero_name()
player_hero.hero_stats()

# ==================================================================================
bot_class = random.choice([Strengh, Dextrexity, Magic_skills])
bot_hero = bot_class()
bot_hero.name = "X"
bot_hero.hero_stats()
