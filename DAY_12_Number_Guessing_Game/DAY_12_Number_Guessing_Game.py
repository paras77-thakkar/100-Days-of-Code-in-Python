import random as rnd
EASY=10
HARD=5
def set_difficulty():
  level=input("Select the difficulty level hard or easy:  ").lower()
  if level=="easy":
    return EASY
  else:
    return HARD
def check_answer(guess,ans,turns):
  if guess>ans:
    print("Too high")
    return turns-1
  elif guess<ans:
    print("Too low")
    return turns-1
  else:
    print("Correct Answer")

def game():
  print("Welcome to the Number Guessing Game!")
  answer=rnd.randint(1, 100)
  turns=set_difficulty()
  guess=0
  while answer!=guess:
    guess=int(input("Make a guess: "))
    turns= check_answer(guess,answer,turns)
    if turns==0:
      print("You are running out of the guesses ")
      return 0
    elif guess!=answer:
      print(f"{turns} turns are remaining , Guess again")

game()
  