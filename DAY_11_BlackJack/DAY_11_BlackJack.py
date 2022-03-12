
import random 

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card= random.choice(cards)
  return card

def calculate_score(cards):
  """Take the list of cards and calculate the total score"""
  if sum(cards)==21 and len(cards)==2:
    return 0
  if sum(cards)>21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score,computer_score):
  if user_score==computer_score:
    return "draw"
  elif computer_score==0:
    return "You lose,opponent has a blackjack"
  elif user_score==0:
    return "You win with blackjack"
  elif user_score>21:
    return "You lose, your score is over 21"
  elif computer_score>21:
    return "You win, computer's score is over 21"
  elif user_score>computer_score:
    return "You win"
  else:
    return "You lose"
def play_game():
  user_cards = []
  computer_cards = []
  is_game_over=False
  for _ in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  while not is_game_over:
      user_score=calculate_score(user_cards)
      computer_score=calculate_score(computer_cards)
      print(f"Your cards={user_cards},Your score={user_score}")
      print(f"Computer cards={computer_cards},Computer score=            {computer_score}")  
    
      if user_score==0 or computer_score==0 or user_score>21:
        is_game_over=True
      
      else:
        user_should_deal=input("Type y to get another card or type n to pass ")
        if user_should_deal=="y":
         user_cards.append(deal_card())
        else:
         is_game_over=True
  
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
  
  print(f"Your cards={user_cards},Your score={user_score}")
  print(f"Computer cards={computer_cards},Computer score={computer_score}") 
  print(compare(user_score,computer_score))

while input("Do you want to play game of blackjack? type 'y' or 'n':") == "y":
    play_game()
