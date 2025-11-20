from functions import user_choice, list_1

word = user_choice(list_1)
with open ('new.txt', 'w') as file:
  file.write(word)