password_cracked = False
password = []
guess = []
def generate_password():
  global password
  for i in range(5):
    import random
    passwordPart = random.randint(0, 9)
    password.append(passwordPart)
def ask_for_guess():
  global guess
  for i in range(5):
    user = input("chose a number from 0 to 9. ")
    num = int(user)
    guess.append(num)
  print(guess)
def password_check_if_any_is_incorect():
  global password, guess
  guessIndex = 0
  for i in range(5):
    gussNum = i + 1
    if guess[guessIndex] == password[guessIndex]:
      hint = "correct"
    else:
      hint = "incorect"
    print("guss number ", gussNum, hint)
    guessIndex += 1
  guessIndex = 0
  for i in range(5):
    guess.pop()
def password_check():
  global password, guess, password_check_if_any_is_incorect, password_cracked
  if password == guess:
    print("congrats you did it!")
    password_cracked = True
  else:
    password_check_if_any_is_incorect()
generate_password()
#gessing Time
while password_cracked == False:
  ask_for_guess()
  password_check()
  






