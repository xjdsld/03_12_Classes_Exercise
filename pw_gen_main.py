# import secrets


# welcome_word = "Welcome to the random password generator. You can select the lenght and the type of charachers used. If you want to use only symbols for your password - press 'S', if you want to use only letters - press 'L', for numbers - 'N'. Press 'C' for the combination of all the above."

# print(welcome_word)


# symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
#  ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
# alphabet = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
# ]
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# def pw_gen(numbers, symbols, alphabet):

#   try: 
#     user_lenght = int(input("Please select the lenght of your password:"))
#     user_choice = (input("Please select one: symbols - 'S', letters - 'L', numbers - 'N', or combination of them all - 'C':")).lower()
    
#     if user_choice == 's':
#       result = secrets.choice(symbols) * user_lenght
#       return result
#     elif user_choice == 'l':
#       result = secrets.choice(alphabet) * user_lenght
#       return result
#     elif user_choice == 'n':
#       result = secrets.choice(numbers) * user_lenght
#       return result
#     elif user_choice == 'c':
#       result = secrets.choice(symbols and numbers and alphabet) * user_lenght
#       return result
#   except ValueError:
#     print("Please enter a number!")
#   except IndexError:
#     print("Please enter N, C, or L")

# pw_gen(numbers, symbols, alphabet)
  