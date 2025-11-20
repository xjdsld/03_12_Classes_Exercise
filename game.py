import random

def create_field(field, cell):
  for a in range(3):              
      field.append([])            
      for b in range(3):
          field[a].append(cell) 

def show_field(field):
  for row in field:
      for p in row:
          print(p, end='')
      print()

def bot_move(field):
  while True:
      bot_x = random.randint(0,2)
      bot_y = random.randint(0,2)
      if field[bot_x][bot_y] != '[X]':
         field[bot_x][bot_y] = '[O]'
         break
      return bot_x, bot_y

def winner(field):
  options = {
      (field[0][0], field[0][1], field[0][2]),
      (field[1][0], field[1][1], field[1][2]),
      (field[2][0], field[2][1], field[2][2]),
      (field[0][0], field[1][0], field[2][0]),
      (field[0][1], field[1][1], field[2][1]),
      (field[0][2], field[1][2], field[2][2]),
      (field[0][0], field[1][1], field[2][2]),
      (field[0][2], field[1][1], field[2][0])
  }


  for i in options:
      if i == ('[O]', '[O]', '[O]'):
          print('Bot wins')
          return True
      elif i == ('[X]', '[X]', '[X]'):
          print('User wins')
          return True
  return False

def user_hod(field):
    user_x = int(input('Enter the x (0-2): '))
    if user_x > 2:
        print('!')
    user_y = int(input('Enter the y (0-2): ')) 
    if user_y > 2:
        print('!')
    field[user_x][user_y] = '[X]'
