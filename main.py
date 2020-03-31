password_cracked = False
password = []
guess = []
level = 1
import pop
def generate_password():
  global password, level
  for i in range(level):
    import random
    passwordPart = random.randint(0, 9)
    password.append(passwordPart)
def ask_for_guess():
  global guess, level
  for i in range(level):
    user = input("chose a number from 0 to 9. ")
    num = int(user)
    guess.append(num)
  print(guess)
def password_check_if_any_is_incorect():
  global password, guess, level
  guessIndex = 0
  for i in range(level):
    gussNum = i + 1
    if guess[guessIndex] == password[guessIndex]:
      hint = "correct"
    else:
      hint = "incorect"
    print("guss number ", gussNum, hint)
    guessIndex += 1
  guessIndex = 0
  for i in range(level):
    guess.pop()
def password_check():
  global password, guess, password_check_if_any_is_incorect, password_cracked, level
  if password == guess:
    print("congrats you did it!")
    password_cracked = True
  else:
    password_check_if_any_is_incorect()
generate_password()
#gessing Time
while True:
  while password_cracked == False:
    ask_for_guess()
    password_check()
  password = []
  guess = []
  level += 1
  generate_password()
  password_cracked = False

  





