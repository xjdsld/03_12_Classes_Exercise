def indexes(lst):
  indexes_list = []
  for i in range(len(lst)):
      indexes_list.append(i)
  return indexes_list

with open ('part_1', 'r') as file:
  file_1 = file.read()
  list_1 = []
  tmp = ''
  for i in file_1:
      if i != '\n':
       tmp += i
      else:
          list_1.append(tmp)
          tmp= ''
  if tmp:
           list_1.append(tmp)
  for i in indexes(list_1):
      print(list_1[i], '-', i+1)


def user_choice(list_1):
  selected = []
  word = ''
  bad_words = ['jerk', 'darn', 'heck']


  while True:
      user_input = input('Select the part want to join or press 0 to exit:')
      if not user_input.isdigit():
          print('!')
      else:
          user_input = int(user_input) - 1
          if user_input == -1:
              break
          selected.append(list_1[user_input])

  for i in selected:
      word += i
  print(word, end = '')
  if word in bad_words:
      print("\n!")
  return word