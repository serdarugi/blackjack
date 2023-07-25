import random
# from art import logo
# from replit import clear
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  elif sum(cards)>21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
  
def compare(user_score,computer_score):
  if user_score == computer_score:
    return "Draw 🙃!"
    if computer_score>21 and user_score>21:
      return "You lose😤"
  elif computer_score == 0:
    return "Unlucky,youlose. It's a Blackjack😱"
  elif user_score==0:
    return "You win dear! It's a Blackjack😎"
  elif user_score>21:
    return "You went over through 21. You lose😭."
  elif computer_score>21:
    return "Your opponent went over you win!😁"
  elif user_score>computer_score:
    return "You win😁."
  elif user_score<computer_score:
    return "You lose😤."


def blackjack_game():
  # print(logo)
  blackjack_continue = True
  computer_hand=[]
  user_hand=[]
  for pick in range(2):
    user_hand.append(deal_card())
    computer_hand.append(deal_card())
  while blackjack_continue:
    user_score = calculate_score(user_hand)
    computer_score= calculate_score(computer_hand)
    print(f"First card of computer : {computer_hand[0]}")
    print(f"Currently you have :{user_hand} and your score:{user_score}")
    if user_score==0 or computer_score==0 or user_score>21:
      blackjack_continue=False
    else:
      additional_card= input("Do you want additional card ? : 'y' or 'n'")
      if additional_card=="y":
        user_hand.append(deal_card())
        if user_score>21:
          print("You lose.")
      else:
        blackjack_continue=False
  while computer_score != 0 and computer_score<17:
    computer_hand.append(deal_card())
    computer_score = calculate_score(computer_hand)

  print(f"Here is the your final hand -> {user_hand},also your score : {user_score}")
  print(f"Also computer final hand -> {computer_hand},also its score : {computer_score}")
  print(compare(user_score,computer_score))
while input("Do you want play a blackjack game against computer ? : 'y' or 'n'\n").lower() == "y":
   clear()
   blackjack_game()
  
