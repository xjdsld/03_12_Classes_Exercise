
class Items():

    def sword(self, hero):
        if hero.hero_money < 10:
            print("U do not have the necessary amount, return ")
        else:
            hero.hero_strenght += 10
            hero.hero_money -= 10

    def mushroom(self, hero):
        if hero.hero_money < 15:
            print("U do not have the necessary amount, return ")
        else:
            hero.hero_magic_skills += 15
            hero.hero_money -= 15

    def flower(self, hero):
        if hero.hero_money < 30:
            print("U do not have the necessary amount, return ")
        else:
            hero.hero_dextrexity -= 20
            hero.hero_money -= 30


class Shop(Items):

    def shoping(self, hero):
        user_choice_shop = input(
            "Select the item you want to buy: 1- sword (10 coins), 2 - mushroom(15 coins), 3 - flower(30 coins): "
        )
        if user_choice_shop == "1":
            self.sword(hero)
        elif user_choice_shop == "2":
            self.mushroom(hero)
        elif user_choice_shop == "3":
            self.flower(hero)
        else:
            print("Try again")
