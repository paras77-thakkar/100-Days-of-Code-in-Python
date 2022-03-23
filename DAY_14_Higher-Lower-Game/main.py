from art import logo
from art import vs
from game_data import data
from replit import clear
import random

def random_acc():
  """Get Data From Random Account"""
  return random.choice(data)
  
def account_data(account):
  """Give data of account in format"""
  return (f"{account['name']}, a {account['description']}, from {account['country']} ")

def check_ans(guess,a_follower,b_follower):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_follower>b_follower:
    return guess=='a'
  else:
    return guess=='b'

def game():
  print(logo)
  score=0
  a_account=random_acc()
  b_account=random_acc()
  should_continue=True
  while should_continue:
    a_account=b_account
    b_account=random_acc()
    while a_account==b_account:
        b_account=random_acc()
    print(f"Compare A:{account_data(a_account)}")
    print(vs)
    print(f"Against B: {account_data(b_account)}")
    guess=input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower=a_account['follower_count']
    b_follower=b_account['follower_count']
    
    is_correct=check_ans(guess,a_follower,b_follower)
    clear()
    print(logo)
    if is_correct:
      score+=1
      print(f"You're right! Current score: {score}.")
    else:
      should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")
game()
