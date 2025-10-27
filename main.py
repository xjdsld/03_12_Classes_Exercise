
# import random

# minefield = []
# user_field = []

# def create_minefield(field, size_a, size_b):
#     for a in range(11):
#         field.append([])
#         for b in range(11):
#             field[a].append('[_]')

# def create_user_field(field, size_n, size_m):
#     for n in range(11):
#         field.append([])
#         for m in range(11):
#             field[n].append('[_]')

# def show_user_field(field, size_n, size_m):
#     for m in range(11):
#         print('   ', end='')
#     print()
#     for n in range(11):
#         print(' ', ' ', end='')
#         for m in range(size_m):
#             print(field[n][m], ' ', end='')
#         print()

# def show_minefield(minefield, size_a, size_b):
#   for a in range(11):
#       print('   ', end='')
#   print()
#   for b in range(11):
#       print(' ', ' ', end='')
#       for a in range(size_a):
#           print(minefield[a][b], ' ', end='')
#       print()

# size_a = size_n = 10

# size_b = size_m = 10

# def placing_items(minefield, size_a, size_b, items_number):
#     for i in range(items_number):
#         while True:
#             rand_a = random.randint(0, size_a - 1)
#             rand_b = random.randint(0, size_b - 1)
#             if minefield[rand_a][rand_b] == '[_]':
#               minefield[rand_a][rand_b] = random.choice(['[C]', '[U]', '[D]', '[H]'])

#               break

# def user(user_n, user_m, user_choice):
#     user_choice = input("Please enter the directio in which you want to move (W,A,S,D):")
    
#   for i in range(len(minefield)):
#     if user_choice == 'W':
#       user_field[user_n][user_m] = user_field[i-1][0] = 'X'
#     if user_choice == 'S':
#       user_field[user_n][user_m] = user_field[i+1][0] = 'X'
#     if user_choice == 'D':
#       user_field[user_n][user_m] = user_field[0][i+1] = 'X'
#     if user_choice == 'S':
#       user_field[user_n][user_m] = user_field[0][i-1] = 'X'

# # def flag(user_field, size_n, size_m):
# #     user_n = int(input('Enter row of the cell you want to flag: '))
# #     user_m = int(input('Enter column the cell you want to flag: '))
# #     user_field[user_n][user_m] = '[#]'
# #     show_user_field(user_field, size_n, size_m)

# create_minefield(minefield, size_a, size_b)
# create_user_field(user_field, size_n, size_m)
# placing_items(minefield, size_a, size_b, 10)
# show_user_field(user_field, size_n, size_m)
# show_minefield(minefield, size_a, size_b)
# user(user_n, user_m, user_choice = input("Please enter the directio in which you want to move (W,A,S,D)"))

# ======================================================================
# def separate_date(start, stop, text):
#     param = ''
#     for i in range(start, stop):
#         param += text[i]
#     print(param)
#     return param

# def determining_month_time(period):
#     if int(period) >= 1 and int(period) <= 10:
#         print('beginnning')
#     elif int(period) > 10 and int(period) < 20:
#         print('middle')
#     elif int(period) >= 20 and int(period) < 31:
#         print('end')
#     else:
#         print('Error')
        
# def separator(symbol):
#     for i in range(len(date)):
#         if date[i] == symbol:
#             dot_location.append(i)
#     print(dot_location)

# date = input("Please enter your date following the correct format (xx.xx.xx):")
# dot_location = []
# day = ''
# month = ''
# year = ''
# months_names = ['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december']

# def month_determination(month, months_names):
#     for i in range(len(months_names)):
#         if int(month) == i+1:
#             print(f'it is {months_names[i]}')

# # for i in range(dot_location[0]):
# #     day += date[i]
# # print(day)

# # for i in range(dot_location[0]+1, dot_location[1]):
# #     month += date[i]
# # print(month)

# # for i in range(dot_location[1]+1, len(date)):
# #     year += date[i]
# # print(year)

# separator('.')
# day = separate_date(0, dot_location[0], date)
# month = separate_date(dot_location[0]+1, dot_location[1], date)
# year = separate_date(dot_location[1]+1, len(date), date)

# determining_month_time(month)
# month_determination(month, months_names)

# # if int(day) >= 1 and int(day) <= 10:
# #     print('beginnning')
# # elif int(day) > 10 and int(day) < 20:
# #     print('middle')
# # elif int(day) >= 20 and int(day) < 31:
# #     print('end')
# # else:
# #     print('Error')
# =====================================================================
# Teacher code
# import random


# def create_pole(pole, size_i, size_j, symbol_empty):
#   for i in range(size_i):
#     pole.append([])
#     for j in range(size_j):
#       pole[i].append(symbol_empty)


# def show_pole(pole, size_i, size_j):
#   for i in range(size_i):
#     for j in range(size_j):
#       print(pole[i][j], ' ', end='')
#     print()


# def fill_items(pole, size_i, size_j, count_items, symbol_items, symbol_empty):
#   for i in range(count_items):
#     while True:
#       rand_pos_i = random.randint(0, size_i - 1)
#       rand_pos_j = random.randint(0, size_j - 1)
#       if pole[rand_pos_i][rand_pos_j] == symbol_empty:
#         pole[rand_pos_i][rand_pos_j] = '[' + symbol_items + ']'
#         break


# def check_cell(cell, cell_user, symbol_armor, symbol_attack, symbol_hp,
#                symbol_coin, symbol_enemy, symbol_empty, user_armor,
#                user_attack, user_hp, user_coins, symbol_user):

#   if cell == '[' + symbol_enemy + ']':
#     if fight(
#         parameters(user_armor, user_attack, user_hp),
#         parameters(random.randint(0, 5), random.randint(1, 5),
#                    random.randint(1, 5))) == 'user_win':
#       print('user_win')
#     elif fight(
#         parameters(user_armor, user_attack, user_hp),
#         parameters(random.randint(0, 5), random.randint(1, 5),
#                    random.randint(1, 5))) == 'bot_win':
#       print('bot_win')
#     else:
#       print('error fight')
#   else:
#     if cell == '[' + symbol_armor + ']':
#       user_armor += 1
#     elif cell == '[' + symbol_attack + ']':
#       user_attack += 1
#     elif cell == '[' + symbol_hp + ']':
#       user_hp += 1
#     elif cell == '[' + symbol_coin + ']':
#       user_coins += 1

#     cell = '[' + symbol_user + ']'
#     cell_user = symbol_empty

#   return user_armor, user_attack, user_hp, user_coins, cell, cell_user


# def user(pole, size_i, size_j, pos_user_i, pos_user_j, symbol_armor,
#          symbol_attack, symbol_hp, symbol_coin, symbol_enemy, symbol_empty,
#          user_armor, user_attack, user_hp, user_coins):

#   user_hod = input('user_hod: ').lower()

#   if user_hod == 's' and pos_user_i + 1 < size_i:
#     user_armor, user_attack, user_hp, user_coins, cell, cell_user = check_cell(
#         pole[pos_user_i + 1][pos_user_j], pole[pos_user_i][pos_user_j],
#         symbol_armor, symbol_attack, symbol_hp, symbol_coin, symbol_enemy,
#         symbol_empty, user_armor, user_attack, user_hp, user_coins,
#         symbol_user)
#     pole[pos_user_i + 1][pos_user_j] = cell
#     pole[pos_user_i][pos_user_j] = cell_user
#     return pos_user_i + 1, pos_user_j, user_armor, user_attack, user_hp, user_coins

#   if user_hod == 'w' and pos_user_i - 1 >= 0:
#     user_armor, user_attack, user_hp, user_coins, cell, cell_user = check_cell(
#         pole[pos_user_i - 1][pos_user_j], pole[pos_user_i][pos_user_j],
#         symbol_armor, symbol_attack, symbol_hp, symbol_coin, symbol_enemy,
#         symbol_empty, user_armor, user_attack, user_hp, user_coins,
#         symbol_user)
#     pole[pos_user_i - 1][pos_user_j] = cell
#     pole[pos_user_i][pos_user_j] = cell_user
#     return pos_user_i - 1, pos_user_j, user_armor, user_attack, user_hp, user_coins

#   if user_hod == 'a' and pos_user_j - 1 >= 0:
#     user_armor, user_attack, user_hp, user_coins, cell, cell_user = check_cell(
#         pole[pos_user_i][pos_user_j - 1], pole[pos_user_i][pos_user_j],
#         symbol_armor, symbol_attack, symbol_hp, symbol_coin, symbol_enemy,
#         symbol_empty, user_armor, user_attack, user_hp, user_coins,
#         symbol_user)
#     pole[pos_user_i][pos_user_j - 1] = cell
#     pole[pos_user_i][pos_user_j] = cell_user
#     return pos_user_i, pos_user_j - 1, user_armor, user_attack, user_hp, user_coins

#   if user_hod == 'd' and pos_user_j + 1 < size_j:
#     user_armor, user_attack, user_hp, user_coins, cell, cell_user = check_cell(
#         pole[pos_user_i][pos_user_j + 1], pole[pos_user_i][pos_user_j],
#         symbol_armor, symbol_attack, symbol_hp, symbol_coin, symbol_enemy,
#         symbol_empty, user_armor, user_attack, user_hp, user_coins,
#         symbol_user)
#     pole[pos_user_i][pos_user_j + 1] = cell
#     pole[pos_user_i][pos_user_j] = cell_user
#     return pos_user_i, pos_user_j + 1, user_armor, user_attack, user_hp, user_coins

#   return pos_user_i, pos_user_j, user_armor, user_attack, user_hp, user_coins


# def fight(avg_user, avg_bot):
#   if avg_user > avg_bot:
#     return 'user_win'
#   elif avg_user < avg_bot:
#     return 'bot_win'
#   else:
#     return 'user_win'


# def parameters(parameters_armor, parameters_attack, parameters_hp):
#   avg = 0
#   rand_crit_user = random.randint(1, 2)
#   if rand_crit_user == 1:
#     avg = (parameters_armor + parameters_attack + parameters_hp +
#            (parameters_attack * random.randint(50, 100) / 100 +
#             parameters_attack)) / 4
#   elif rand_crit_user == 2:
#     avg = (parameters_armor + parameters_attack + parameters_hp) / 4
#   else:
#     print('Error critical')

#   return avg


# pole = []
# size_i = 10
# size_j = 10

# symbol_armor = 'A'
# count_armor = 5
# user_armor = 0

# symbol_attack = 'D'
# count_attack = 5
# user_attack = 1

# symbol_hp = 'H'
# count_hp = 5
# user_hp = 1

# symbol_coin = 'C'
# count_coin = 5
# user_coins = 0

# symbol_enemy = 'E'
# count_enemy = 5

# symbol_empty = '[_]'

# create_pole(pole, size_i, size_j, symbol_empty)

# symbol_user = '*'
# pos_user_i = 0
# pos_user_j = 0
# pole[pos_user_i][pos_user_j] = '[' + symbol_user + ']'

# fill_items(pole, size_i, size_j, count_coin, symbol_coin, symbol_empty)
# fill_items(pole, size_i, size_j, count_armor, symbol_armor, symbol_empty)
# fill_items(pole, size_i, size_j, count_attack, symbol_attack, symbol_empty)
# fill_items(pole, size_i, size_j, count_hp, symbol_hp, symbol_empty)
# fill_items(pole, size_i, size_j, count_enemy, symbol_enemy, symbol_empty)

# while True:
#   show_pole(pole, size_i, size_j)
#   print(
#       f'user_coins:{user_coins}, user_hp:{user_hp}, user_armor:{user_armor}, user_attack:{user_attack}'
#   )
#   pos_user_i, pos_user_j, user_armor, user_attack, user_hp, user_coins = user(
#       pole, size_i, size_j, pos_user_i, pos_user_j, symbol_armor,
#       symbol_attack, symbol_hp, symbol_coin, symbol_enemy, symbol_empty,
#       user_armor, user_attack, user_hp, user_coins)
 

# MAZE HARDCODED ===========================================================

# labyrinth = [
#     "███████████████",
#     "█    █        █",
#     "█ ███ █ ███ █ █",
#     "█ █    █    █ █",
#     "█ █ █████ ███ █",
#     "█ █       █   █",
#     "█ █████ ███ ███",
#     "█         █   █",
#     "█ ███ █ █ ███ █",
#     "█   █ █ █ █ █ █",
#     "█ █ █ ███ █ █ █",
#     "█ █       █ █ █",
#     "█ █████████ █ █",
#     "█           █E█",
#     "███████████████"
# ]
    
# labyrinth_2d = []
# for row in labyrinth:
#     new_row = list(row)
#     labyrinth_2d.append(new_row)

# def print_labyrinth(lab):
#     for row in lab:
#         print("".join(row))
        
# labyrinth_2d[1][1] = '*'
# user_m = 1
# user_n = 1

# for row in labyrinth_2d:
#     print("".join(row))

# def move_user(user_n, user_m, command, labyrinth_2d):
#     new_n = user_n
#     new_m = user_m 
#     if command == 's':
#         new_n += 1
#     elif command == 'w':
#         new_n -= 1
#     elif command == 'a':
#         new_m -= 1
#     elif command == 'd':
#         new_m += 1
#     else:
#         print("Error Try again.")
#     if labyrinth_2d[new_n][new_m] == '█':
#         print("WALL!!!")
#         return user_n, user_m
#     else:
#         return new_n, new_m
        
    
# while True:
#     command = input("Move (W,A,S,D): ").lower()
#     labyrinth_2d[user_n][user_m] = ' '
#     user_n, user_m = move_user(user_n, user_m, command, labyrinth_2d)
#     labyrinth_2d[user_n][user_m] = '*'
#     print_labyrinth(labyrinth_2d)
    
# MAZE AUTOMATED ========================================================== 
# import random
# size_a = size_b = 10

# damage_user = 0
# armour_user = 0
# health_user = 0
# user_coins = 0
# user_health = 0
# uron = 1
# result = ''
# check = 0

# minefield = []

# def enemy_power():
#     damage_enemy = random.randint(0, 5)
#     armour_enemy = random.randint(0, 5)
#     health_enemy = random.randint(0, 5)
#     enemy_stats = int((damage_enemy + armour_enemy + health_enemy) / 3)
#     return enemy_stats


# def create_minefield(field, size_a, size_b):
#     for a in range(size_a):
#         field.append([])
#         for b in range(size_b):
#             field[a].append('[_]')


# def placing_items(minefield, size_a, size_b, items_number, item_type):
#     for i in range(items_number):
#         while True:
#             rand_a = random.randint(0, size_a - 1)
#             rand_b = random.randint(0, size_b - 1)
#             if minefield[rand_a][rand_b] == '[_]':
#                 minefield[rand_a][rand_b] = item_type
#                 break
              
# def show_minefield(minefield, size_a, size_b):
#   for a in range(10):
#       print('   ', end='')
#   print()
#   for b in range(10):
#       print(' ', ' ', end='')
#       for a in range(size_a):
#           print(minefield[a][b], ' ', end='')
#       print()

# def move_user(user_n, user_m, command):
#     if command == 'W' or command == 'w' and user_m > 0:
#         user_m -= 1
#     elif command == 'S' or command == 's' and user_m < size_a - 1:
#         user_m += 1
#     elif command == 'A' or command == 'a' and user_n > 0:
#         user_n -= 1
#     elif command == 'D' or  command == 'd' and user_n < size_b - 1:
#         user_n += 1
#     else:
#         print("Error Try again.")
#     return user_n, user_m

# def game(minefield, user_n, user_m, user_coins, damage_user, armour_user, health_user, user_health, uron, result, check):
  
#     user_stats = int(((damage_user + armour_user + health_user) / 3)*uron)
#     if minefield[user_n][user_m] == '[C]':
#         minefield[user_n][user_m] = '[C]'
#         user_coins += 1
#         print(f"Collected a Coin, your coins:{user_coins}")
#     elif minefield[user_n][user_m] == '[D]':
#         minefield[user_n][user_m] = '[D]'
#         damage_user += 1
#         print(f"Damage!:{damage_user}")
#     elif minefield[user_n][user_m] == '[H]':
#         minefield[user_n][user_m] = '[H]'
#         health_user += 1
#         print(f"Collected a Heart!, your health:{health_user}")
#     elif minefield[user_n][user_m] == '[A]':
#         minefield[user_n][user_m] = '[A]'
#         armour_user += 1
#         print(f"Armour!, your armour:{armour_user}")
#     elif minefield[user_n][user_m] == '[E]':
#         enemy_stats = enemy_power()
#         if user_stats <= enemy_stats:
#             print("You lost")
#             minefield[user_n][user_m] = '[_]'
#             user_n, user_m = 0,0
#             result = 'reset'
#             check = 0
#         else:
#             print("You won")
#             check += 1
#             if check == 5:
#              result = 'new level'
#         minefield[user_n][user_m] = '[E]'
#     elif minefield[user_n][user_m] == '[U]':
#         uron = random.randint(0,10) / 100

#     if minefield[user_n][user_m] != '[#]':
#         minefield[user_n][user_m] = '[_]'

#     return user_coins, damage_user, armour_user, health_user, user_health, uron, user_n, user_m, result, check

# def clear_field(minefield, size_a, size_b):
#         for a in range(size_a):
#             for b in range(size_b):
#                 if minefield[a][b] != '[E]':
#                     minefield[a][b] = '[_]'
#                     user_n, user_m = 0,0
#         placing_items(minefield, size_a, size_b, 5, '[C]')
#         placing_items(minefield, size_a, size_b, 5, '[D]')
#         placing_items(minefield, size_a, size_b, 5, '[H]')
#         placing_items(minefield, size_a, size_b, 5, '[A]')
#         placing_items(minefield, size_a, size_b, 5, '[E]')
#         placing_items(minefield, size_a, size_b, 5, '[U]')


# def portal(minefield, size_a, size_b):
#     for a in range(size_a):
#         for b in range(size_b):
#             if minefield[a][b] == '[#]':
#                 minefield[a][b] = '[_]'
#     while True:
#         rand_a = random.randint(0, size_a - 1)
#         rand_b = random.randint(0, size_b - 1)
#         if minefield[rand_a][rand_b] == '[_]':
#             minefield[rand_a][rand_b] = '[#]'
#             print("Go to #!")
#             break

# create_minefield(minefield, size_a, size_b)
# placing_items(minefield, size_a, size_b, 5, '[C]')
# placing_items(minefield, size_a, size_b, 5, '[D]')
# placing_items(minefield, size_a, size_b, 5, '[H]')
# placing_items(minefield, size_a, size_b, 5, '[A]')
# placing_items(minefield, size_a, size_b, 5, '[E]')
# placing_items(minefield, size_a, size_b, 5, '[U]')

# user_n = 0
# user_m = 0
# minefield[user_n][user_m] = '[*]'

# while True:
#     show_minefield(minefield, size_a, size_b)

#     move = input("Move (W,A,S,D): ").lower()

#     minefield[user_n][user_m] = '[_]'

#     user_n, user_m = move_user(user_n, user_m, move)


#     user_coins, damage_user, armour_user, health_user, user_health, uron, user_n, user_m, result, check = game(minefield, user_n, user_m, user_coins, damage_user, armour_user, health_user, user_health, uron, result, check)


#     if result == 'reset':
#         clear_field(minefield, size_a, size_b)
#         result = ''
#     elif result == 'new level':
#         portal(minefield, size_a, size_b)
#         result = ''

#     if minefield[user_n][user_m] == '[#]':
#         print("\nWelcome to the Labyrinth!\n")
#         break

#     minefield[user_n][user_m] = '[*]' 
    
# # LEVEL 2

# def create_labyrinth(width, height):
#     labyrinth_width = width * 2 + 1
#     labyrinth_height = height * 2 + 1

#     labyrinth = [['█' for _ in range(labyrinth_width)] for _ in range(labyrinth_height)]

#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#     def create_passages(cx, cy):
#         directions_shuffled = directions[:]
#         random.shuffle(directions_shuffled)

#         for dy, dx in directions_shuffled:
#             nx, ny = cx + dx, cy + dy
#             if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx]:
#                 visited[ny][nx] = True
#                 wall_y = cy * 2 + 1 + dy 
#                 wall_x = cx * 2 + 1 + dx
#                 labyrinth[cy * 2 + 1][cx * 2 + 1] = ' '
#                 labyrinth[wall_y][wall_x] = ' '
#                 labyrinth[ny * 2 + 1][nx * 2 + 1] = ' '
#                 create_passages(nx, ny)

#     visited = [[False for _ in range(width)] for _ in range(height)]

#     start_x, start_y = 0, 0
#     visited[start_y][start_x] = True
#     create_passages(start_x, start_y)

#     labyrinth[1][0] = '*'  
#     labyrinth[labyrinth_height - 2][labyrinth_width - 1] = 'E' 

#     return labyrinth

# def print_labyrinth(labyrinth):
#     for row in labyrinth:
#         print("".join(row))

# def move_user2(user_n, user_m, command, labyrinth):
#     new_n = user_n
#     new_m = user_m 
#     if command == 's':
#         new_n += 1
#     elif command == 'w':
#         new_n -= 1
#     elif command == 'a':
#         new_m -= 1
#     elif command == 'd':
#         new_m += 1
#     else:
#         print("Error Try again.")
#     if new_n < 0 or new_n >= len(labyrinth) or new_m < 0 or new_m >= len(labyrinth[0]):
#         print("Out of bounds!")
#         return user_n, user_m
#     if labyrinth[new_n][new_m] == '█':
#         print("WALL!!!")
#         return user_n, user_m
#     else:
#         return new_n, new_m
        
# labyrinth = create_labyrinth(10, 5)
# user_n, user_m = 1, 0

# while True:
#     print_labyrinth(labyrinth)
#     command = input("Move (W,A,S,D): ").lower()
#     labyrinth[user_n][user_m] = ' '
#     user_n, user_m = move_user2(user_n, user_m, command, labyrinth)
#     labyrinth[user_n][user_m] = '*'


# ======================================================================

# import random


# def create_deck(deck, meaning, suit):
#   for i in suit:
#     for j in meaning:
#       deck.append(i + j)


# def fill_cards_players(player, deck, count_cards):
#   if len(deck) > 0:
#     for i in range(count_cards):
#       tmp_cards = random.choice(deck)
#       player.append(tmp_cards)
#       deck.remove(tmp_cards)


# def user_hod(player, table):
#   if len(player) > 0:
#     while True:
#       user = input('user:')
#       if user in player:
#         table.append(user)
#         player.remove(user)
#         break
#   else:
#     print('no cards user')


# def bot_hod(player, table):
#   if len(player) > 0:
#     tmp = random.choice(player)
#     table.append(tmp)
#     player.remove(tmp)

# def trump_count(player, player_name, count):
#     count = []
#     for i in range(len(player)):
#         if player[i][0] == trump:
#             count.append(trump)
#     print(f"Player {player_name} has {len(count)} trump cards")
#     return count
  

# # def trump_check(user, bot1, bot2, bot3, meaning, values):
# #   general = user + bot1 + bot2 + bot3
# #   trump_cards = []
# #   for i in general:
# #       suit = i[0]
# #       if suit == trump: 
# #           trump_cards.append(i)
# #   value = i[1]

# def min_max_trump(player, player_name, meaning, values):
#   min_card = ''
#   max_card = ''
#   min_value = 1000
#   max_value = -1
#   trump_count = 0

#   i = 0
#   while i < len(player):
#       card = player[i]

#       # find suit and value by checking all possible cards
#       j = 0
#       suit_of_card = ''
#       value_str = ''
#       found = 0
#       while j < len(suit):
#           k = 0
#           while k < len(meaning):
#               possible_card = suit[j] + meaning[k]
#               if card == possible_card:
#                   suit_of_card = suit[j]
#                   value_str = meaning[k]
#                   found = 1
#               k = k + 1
#           j = j + 1

#       # if card found and suit matches trump
#       if found == 1 and suit_of_card == trump:
#           # find the value in values list
#           v = 0
#           card_value = -1
#           while v < len(meaning):
#               if meaning[v] == value_str:
#                   card_value = values[v]
#               v = v + 1

#           if card_value != -1:
#               if trump_count == 0:
#                   min_value = card_value
#                   max_value = card_value
#                   min_card = card
#                   max_card = card
#               else:
#                   if card_value < min_value:
#                       min_value = card_value
#                       min_card = card
#                   if card_value > max_value:
#                       max_value = card_value
#                       max_card = card

#               trump_count = trump_count + 1
#       i = i + 1

#   if trump_count > 0:
#       print(f"Player {player_name} - Min trump: {min_card}, Max trump: {max_card}")
#   else:
#       print(f"Player {player_name} has no trump cards.")
            

    
# meaning = ['6', '7', '8', '9', '10', 'B', 'Д', 'К', 'Т']
# suit = ['♥', '♦', '♣', '♠']
# values = [0, 1, 2, 3, 4, 5, 6, 7, 8]


# deck = []
# table = []

# user = []
# bot1 = []
# bot2 = []
# bot3 = []

# standart_count_cards = 6

# create_deck(deck, meaning, suit)

# random.shuffle(deck)

# trump = random.choice(suit)

# print('trump:', trump)

# fill_cards_players(user, deck, standart_count_cards)
# fill_cards_players(bot1, deck, standart_count_cards)
# fill_cards_players(bot2, deck, standart_count_cards)
# fill_cards_players(bot3, deck, standart_count_cards)

# while True:
#     print('user:', user)
#     print('bot1:', bot1)
#     print('bot2:', bot2)
#     print('bot3:', bot3)
#     trump_count(user, 'User', count)
#     trump_count(bot1, 'bot1', count)
#     trump_count(bot2, 'bot2', count)
#     trump_count(bot3, 'bot3', count)

#     min_max_trump(user, 'User', meaning, values)
#     min_max_trump(bot1, 'Bot1', meaning, values)
#     min_max_trump(bot2, 'Bot2', meaning, values)
#     min_max_trump(bot3, 'Bot3', meaning, values)
    
#     print('table:', table)
    
#     user_hod(user, table)
#     bot_hod(bot1, table)
#     bot_hod(bot2, table)
#     bot_hod(bot3, table)
    
#     fill_cards_players(user, deck, standart_count_cards - len(user))
#     fill_cards_players(bot1, deck, standart_count_cards - len(bot1))
#     fill_cards_players(bot2, deck, standart_count_cards - len(bot2))
#     fill_cards_players(bot3, deck, standart_count_cards - len(bot3))

# import random


# def create_deck(deck, meaning, suit):
#   for i in suit:
#     for j in meaning:
#       deck.append(i + j)


# def fill_cards_players(player, deck, count_cards):
#   if len(deck) > 0:  
#     for i in range(min(count_cards, len(deck))):
#       tmp_cards = random.choice(deck)
#       player.append(tmp_cards)
#       deck.remove(tmp_cards)


# def user_hod(player, table):
#   if len(player) > 0:
#     while True:
#       user = input('user:')
#       if user in player:
#         table.append(user)
#         player.remove(user)
#         cover_card(table, player)
#         break
#   else:
#     print('no cards user')

# def bot_hod(player, table, name):
#   if len(player) > 0:
#     tmp = random.choice(player)
#     print(f'{name} played: {tmp}')
#     table.append(tmp)
#     player.remove(tmp)
#     cover_card(table, player)
#   else:
#     print('Bot has no cards.')


# def find_min_trump(player, symbol_trump, meaning):
#   tmp_mss = []
#   tmp_mss_index = []
#   tmp_res = ''
#   for item in player:
#     if symbol_trump == item[0]:
#       tmp_mss.append(item)

#   if len(tmp_mss) > 0:
#     for i in tmp_mss:
#       for j in range(len(meaning)):
#         if i[1] == meaning[j]:
#           tmp_mss_index.append(j)

#   if len(tmp_mss_index) > 0:
#     tmp_mss_index.sort()
#     tmp_res = symbol_trump + meaning[tmp_mss_index[0]]

#   if tmp_res != None:
#     return tmp_res

# def first_move(user, bot1, bot2, bot3, trump, meaning):
#         players = [user, bot1, bot2, bot3]
#         names = ['user', 'bot1', 'bot2', 'bot3']
#         cards = []

#         for i in range(4):
#             min_card = find_min_trump(players[i], trump, meaning)
#             cards.append(min_card)

#         lowest_rank = None
#         first_player_index = None

#         # Step 2: Find the player with the lowest-ranked trump card
#         for i in range(4):
#             card = cards[i]
#             if card != '':
#                 # Get rank manually (without index())
#                 rank = -1
#                 for j in range(len(meaning)):
#                     if card[1] == meaning[j]:
#                         rank = j
#                         break
#                 if rank != -1:
#                     if lowest_rank is None or rank < lowest_rank:
#                         lowest_rank = rank
#                         first_player_index = i

#         if first_player_index is not None:
#             return names[first_player_index]
#         else:
#             return None  # No one has trump cards

# def play_round(first_player, players, player_names, deck, table, max_hand_size=6):
#     order = []

#     if first_player == 'user':
#         order = [0, 1, 2, 3] 
#     elif first_player == 'bot1':
#         order = [1, 2, 3, 0]
#     elif first_player == 'bot2':
#         order = [2, 1, 3, 0]
#     elif first_player == 'bot3':
#         order = [3, 1, 2, 0]

#     for i in order:
#         name = player_names[i]
#         if name == 'user':
#             user_hod(players[i], table)
#             print(table)
#         else:
#             bot_hod(players[i], table, name)
#             print(table)

#     for i in range(len(players)):
#         missing_cards = max_hand_size - len(players[i])
#         fill_cards_players(players[i], deck, missing_cards)

#     print('user:', players[0])

# # def all_trump_cards(player, trump):
# #     all_player_trump_cards = []
# #     for i in player:
# #         if i[0] == trump:
# #             all_player_trump_cards.append(i)
# #     return all_player_trump_cards


# def cover_card(table, player):
#         tmp_player_index = []

#         # Step 1: Sort player by meaning rank
#         if len(player) > 0:
#             for card in player:
#                 for i in range(len(meaning)):
#                     if card[1] == meaning[i]:
#                         tmp_player_index.append(card)

#             for i in range(len(player)):
#                 for j in range(len(player)):
#                     rank_i = 0
#                     for k in range(len(meaning)):
#                         if player[i][1] == meaning[k]:
#                             rank_i = k
#                             break
#                     rank_j = 0
#                     for k in range(len(meaning)):
#                         if player[j][1] == meaning[k]:
#                             rank_j = k
#                             break

#                     if rank_i > rank_j:
#                         player[i], player[j] = player[j], player[i]

#         # Step 2: Compare last table card with player's cards
#         if len(table) > 0 and len(player) > 0:
#             table_card_value = table[-1][1]  # e.g., '9'
#             table_card_suit = table[-1][0]   # e.g., '♥'

#             table_rank = 0
#             for i in range(len(meaning)):
#                 if table_card_value == meaning[i]:
#                     table_rank = i
#                     break

#             # Instead of True/False, we print and exit inside the loop
#             for card in player:
#                 if card[0] == table_card_suit:
#                     card_rank = 0
#                     for j in range(len(meaning)):
#                         if card[1] == meaning[j]:
#                             card_rank = j
#                             break

#                     if card_rank > table_rank:
#                         print("YES — player can cover the card.")
#                         break
#             else:
#                 # The else block of a for loop runs only if the loop wasn't broken
#                 print("NO — player cannot cover the card.")
    

# meaning = ['6', '7', '8', '9', '10', 'B', 'Д', 'К', 'Т']
# suit = ['♥', '♦', '♣', '♠']

# deck = []
# table = []

# user = []
# bot1 = []
# bot2 = []
# bot3 = []

# standart_count_cards = 6

# create_deck(deck, meaning, suit)

# random.shuffle(deck)

# trump = random.choice(suit)
# print('trump:', trump)

# fill_cards_players(user, deck, standart_count_cards - len(user))
# fill_cards_players(bot1, deck, standart_count_cards - len(bot1))
# fill_cards_players(bot2, deck, standart_count_cards - len(bot2))
# fill_cards_players(bot3, deck, standart_count_cards - len(bot3))

# print('user:', user)
# print('bot1:', bot1)
# print('bot2:', bot2)
# print('bot3:', bot3)

# print('table:', table)

# a = find_min_trump(user, trump, meaning)
# print('1 ', a)
# b = find_min_trump(bot1, trump, meaning)
# print('2 ', b)
# c = find_min_trump(bot2, trump, meaning)
# print('3 ', c)
# d = find_min_trump(bot3, trump, meaning)
# print('4 ', d)

# first = first_move(user, bot1, bot2, bot3, trump, meaning)

# if first:
#     print(f'\nFirst to move: {first}')
# else:
#     print('\nNo player has a trump card.')

# while len(user) > 0 or len(bot1) > 0 or len(bot2) > 0 or len(bot3) > 0 or len(deck) > 0:
#     players = [user, bot1, bot2, bot3]
#     player_names = ['user', 'bot1', 'bot2', 'bot3']
#     play_round(first, players, player_names, deck, table, standart_count_cards)

# person = {
#   'name': 'qwerty',
#   'age' : 25,
#   'name1': 'qwerty2',
# }

# print(person)
# # print(person['name'])
# # print(person['age'])
# print('=====')
# # print(person['qwerty'])
# # print(person['name'])
# person['name'] = 'poni'
# # print(person['name'])
# print('=====')
# person['city'] = 'Dnipro'
# print(person)
# print('=====')
# del person['name1']
# print(person)

# for jsdhvfjds, sdfklskdfs in person.items():
#     print(f'{jsdhvfjds}: {sdfklskdfs}')

# print(person.keys())
# print(person.values())


# print(person.get('asd', 'error keys'))

# def uniq(user_cat, user_value):
#     if user_cat in dictionary:
#         print('Enter something else')

# def change_value():
#     user_cat = input('Please enter the CAR of the value:')
#     new_value = input('Please enter the NEW value:')
#     dictionary[user_cat] = new_value
#     return new_value

# def delete_value(dictionary):
#     to_delete = input('What would u like to delete:')
#     del dictionary[to_delete]

# def safe_show(dictionary, element_name):
#     print(dictionary.get(element_name))
#     return element_name
        

# dictionary = {}

# while True:
#     user_cat = input('Please enter the category:')
#     user_value = input('Please enter the value:')
#     uniq(user_cat, user_value)
#     dictionary[user_cat] = user_value
#     print(dictionary)
#     if user_cat == 'break' or user_value == 'break':
#         break
#     user_change = input('Do you want to change the dictionary: Y -fir yes; N -no:').lower()
#     if user_change == 'yes':
#          change_value()
#     else:
#         continue
#     user_delet = input('Do you want to delete an element: Y -fir yes; N -no:').lower()
#     if user_change == 'yes':
#          delete_value(dictionary)
#     else:
#         continue
#     print(dictionary)
#     element_name = input('What element u want to see: ')
#     safe_show(dictionary, element_name)

# import random

# cell = '[_]'
# field = []

# def create_field(field):
#     for a in range(3):              
#         field.append([])            
#         for b in range(3):
#             field[a].append(cell) 

# def show_field(field):
#     for row in field:
#         for cell in row:
#             print(cell, end='')
#         print()

# def bot_move():
#     while True:
#         bot_x = random.randint(0,2)
#         bot_y = random.randint(0,2)
#         if field[bot_x][bot_y] != '[X]':
#             field[bot_x][bot_y] = '[O]'
#             break
#         return bot_x, bot_y
    
# def winner():
#     options = {
#                 'r1': [field[0][0], field[0][1], field[0][2]],
#                 'r2': [field[1][0], field[1][1], field[1][2]],
#                 'r3': [field[2][0], field[2][1], field[2][2]],
#                 'c1': [field[0][0], field[1][0], field[2][0]],
#                 'c2': [field[0][1], field[1][1], field[2][1]],
#                 'c3': [field[0][2], field[1][2], field[2][2]],
#                 'd1': [field[0][0], field[1][1], field[2][2]],
#                 'd2': [field[0][2], field[1][1], field[2][0]]
#             }
#     for i in options:
#         row = options[i]
#         if row == ['[O]','[O]','[O]']:
#             print('Bot wins')
#             return True
#         elif row == ['[X]','[X]','[X]']:
#             print('User wins')
#             return True
#     return False


# create_field(field)
# show_field(field)

# while True:
#     user_x = int(input('Enter the x (0-2): '))
#     if user_x > 2:
#         print('!')
#     user_y = int(input('Enter the y (0-2): ')) 
#     if user_y > 2:
#         print('!')
#     field[user_x][user_y] = '[X]'
#     bot_move()
#     show_field(field)
#     if winner():
#         break
    
#===========================(tuple)
# point = (10,20)
# print(point)
#
# # print(type(point))
# print(point[0])
#
# x, y = point
# print(x,y)
#===========================(set)

# nums = {1,2,3,4,3,2, 5}
# print(nums)
#
# nums.add(6)
# print(nums)
# nums.add(1)
# print(nums)
#
# nums.remove(1)
# print(nums)

# nums1 = {1,2,3}
# nums2 = {3,4,5}

# print(nums1, nums2)
# print(nums1 | nums2)
# print(nums1 & nums2)
# print(nums1 ^ nums2)
# print(nums1 - nums2)

# tuple_1 = ('d', 'b', 'c', 'd')
# tuple_2 = ('c', 'e', 'f', 'b')

# new_tuple = tuple_1 + tuple_2

# for i in range(3):
#     print(new_tuple[i])

# tuple_1 = (1, 2, 3)
# tuple_2 = (4, 5, 6)
# tmp = []

# new_tuple = tuple_1 + tuple_2
# for i in new_tuple:
#     tmp.append(i)
# tmp.remove(2)
# tmp.append(10)
# print(tmp)

# nums = (2, 45, 3, 654, 425, 563, 42, 246, 9090)

# while True:
#     user_num = int(input('Ur num?:'))
#     if user_num in nums:
#         print('+')
#         break
#     elif user_num == 'break':
#         break
#     else:
#         print('-')

# TRY AGAIN ======================================================================================
# alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',]
# my_tuple = ()
# tmp = []

# nums = input("Ur nums, using a comma(e.g. 4,5):")

# for i in nums:
#     if i != ',' and i !=' ':
#         tmp.append(i)
# print(tmp)
# for i in tmp:
#     my_tuple += (i,)
# print(my_tuple)
# ===============================================================================================

# bet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',]
# my_tuple = (tuple(range(1, 100)))


# for i in my_tuple:
#     print(f"Coordinate is {my_tuple[i]} = {bet[i]}")
# ===============================================================================================

# user_word = input('Enter one word:')
# tmp_list = []
# tmp = {1,2}
# for i in user_word:
#     tmp_list.append(i)
# for i in tmp_list:
#     tmp.add(i)
# for i in tmp(range(len(1))):
#     tmp.remove(i)
# print(tmp)
# ===============================================================================================

# import random

# cell = '[_]'
# field = []

# def create_field(field):
#     for a in range(3):              
#         field.append([])            
#         for b in range(3):
#             field[a].append(cell) 

# def show_field(field):
#     for row in field:
#         for cell in row:
#             print(cell, end='')
#         print()

# def bot_move():
#     while True:
#         bot_x = random.randint(0,2)
#         bot_y = random.randint(0,2)
#         if field[bot_x][bot_y] != '[X]':
#             field[bot_x][bot_y] = '[O]'
#             break
#         return bot_x, bot_y

# def winner():
#     options = {
#         (field[0][0], field[0][1], field[0][2]),
#         (field[1][0], field[1][1], field[1][2]),
#         (field[2][0], field[2][1], field[2][2]),
#         (field[0][0], field[1][0], field[2][0]),
#         (field[0][1], field[1][1], field[2][1]),
#         (field[0][2], field[1][2], field[2][2]),
#         (field[0][0], field[1][1], field[2][2]),
#         (field[0][2], field[1][1], field[2][0])
#     }



#     for i in options:
#         if i == ('[O]', '[O]', '[O]'):
#             print('Bot wins')
#             return True
#         elif i == ('[X]', '[X]', '[X]'):
#             print('User wins')
#             return True
#     return False



# create_field(field)
# show_field(field)

# while True:
#     user_x = int(input('Enter the x (0-2): '))
#     if user_x > 2:
#         print('!')
#     user_y = int(input('Enter the y (0-2): ')) 
#     if user_y > 2:
#         print('!')
#     field[user_x][user_y] = '[X]'
#     bot_move()
#     show_field(field)
#     if winner():
#         break
# ===============================================================================================


# def fav_color():
#     user_color = input("What is their favourite color:").lower()
#     if user_color == "blue":
#         print("Correct")
#         return 1
#     else:
#         print("Incorrect")
#         return 0


# while True:
#     result = fav_color()
#     if result == 0:
#        continue
#     elif result == 1:
#        break
# ===============================================================================================
# def make_coffee(size, flavor = "regular"):
#     print(f"Making a {size} {flavor} coffee...")

# make_coffee("large")
# make_coffee("small", "macciato")
# ===============================================================================================

import random


def create_deck(deck, meaning, suit):
  for i in suit:
    for j in meaning:
      deck.append(i + j)
  print(deck)

def fill_cards_players(player, deck, count_cards):
  if len(deck) > 0:
    for i in range(count_cards):
      tmp_cards = random.choice(deck)
      player.append(tmp_cards)
      deck.remove(tmp_cards)

def game_order():
  order = [0, 1, 2]

def user_choice_function(user, bot, chosen_card):
  if chosen_card in bot:
      bot.remove(chosen_card)
      user.append(chosen_card)
      print("You took", chosen_card, "from bot!")
  else:
      print("Not a card.")


def bot_choice_function(player, deck):
  bot_cards = []
  for i in range(len(player)):
      rank1 = ""
      for c in player[i]:
          if c not in ['♥', '♦', '♣', '♠']:
              rank1 = rank1 + c

      for j in range(i + 1, len(player)):
          rank2 = ""
          for c in player[j]:
              if c not in ['♥', '♦', '♣', '♠']:
                  rank2 = rank2 + c

          if rank1 == rank2:
              if player[i] not in bot_cards:
                  bot_cards.append(player[i])
              if player[j] not in bot_cards:
                  bot_cards.append(player[j])
                
  if len(bot_cards) > 0:
    chosen_card = random.choice(bot_cards)
    rank = ""
    for c in chosen_card:
        if c not in ['♥', '♦', '♣', '♠']:
            rank += c
    bot_suite = random.choice(['♥', '♦', '♣', '♠'])
    bot_choice = rank + bot_suite
    print("Bot chose", bot_choice)
    
    if bot_choice in user:
      user.remove(bot_choice)
      player.append(bot_choice)
      print("Bot took", bot_choice, "from u!")
    else:
        print("Wrong guess.")

  
    

meaning = ['6', '7', '8', '9', '10', 'B', 'Д', 'К', 'Т']
suit = ['♥', '♦', '♣', '♠']


deck = []
table = []

user = []
bot1 = []
bot2 = []
bot3 = []

standart_count_cards = 4

create_deck(deck, meaning, suit)

random.shuffle(deck)


fill_cards_players(user, deck, standart_count_cards)
fill_cards_players(bot1, deck, standart_count_cards)
fill_cards_players(bot2, deck, standart_count_cards)
fill_cards_players(bot3, deck, standart_count_cards)

while True:
  print('user:', user)
  user_choice = input("Enter the card u want: ")
  user_choice_function(user, bot1, user_choice)
  user_choice_function(user, bot2, user_choice)
  fill_cards_players(user, deck, standart_count_cards - len(user))
  fill_cards_players(bot1, deck, standart_count_cards - len(bot1))
  fill_cards_players(bot2, deck, standart_count_cards - len(bot2))
  fill_cards_players(bot3, deck, standart_count_cards - len(bot3))
  bot_choice_function(bot1, deck)
  bot_choice_function(bot2, deck)




        
        

    
