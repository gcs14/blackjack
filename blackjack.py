import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_card1 = random.choice(cards)
player_card2 = random.choice(cards)
player_hand = [player_card1, player_card2]
player_score = sum(player_hand)

dealer_card1 = random.choice(cards)
dealer_card2 = random.choice(cards)
dealer_hand = [dealer_card1, dealer_card2]
dealer_score = sum(dealer_hand)
reveal_card = False

intro = input("Welcome to Dusty Sam's Blackjack Palor! Ready to be dealt in? Type 'y' for yes or 'n' for no. ")
if intro == "y":
    print("\nThe deck is shuffled and the cards have been dealt.\n")
elif intro == "n":
    print("\nThat's too bad! Take these cards anyways!\n")
else:
    print("\nNot sure what that means...Anyways, grab these cards, and stop acting strange!\n")

print(f"Your hand is {player_hand}, current score: {player_score}")
print(f"Dealer's first card is {dealer_card1}")

def bust():
    print(f"Your final hand is {player_hand}, final score: {player_score}.")
    print("\nYou Bust. Dealer Wins.")
    
def dealer_bust():
    print(f"Your final hand is {player_hand}, final score: {player_score}.")
    print(f"\nThe dealer bust with a score of {dealer_score}. You win!")

def blackjack():
    print(f"Your final hand is {player_hand}, final score: {player_score}.")
    print(f"\nDealer's hand is {dealer_hand}, and his score was {dealer_score}")
    print("\nYou have 21, you won!")

def win():
    print(f"Your final hand is {player_hand}, final score: {player_score}.")
    print(f"\nDealer's hand is {dealer_hand}, and his score was {dealer_score}")
    print(f"\nYou have {player_score}, you won!")  

def lose():
    print(f"Your final hand is {player_hand}, final score: {player_score}.")
    print(f"\nDealer's hand is {dealer_hand}, and his score was {dealer_score}")
    print("\nYou lose, Dealer wins.")

def draw():
    print(f"Your final hand is {player_hand}, final score: {player_score}.")
    print(f"\nDealer's hand is {dealer_hand}, and his score is {dealer_score}")
    print("It's a draw. No one wins.")

if player_score == 21:
    print("\nYou have 21, you won!")
else:
    hit = input("\nDo you want to another card? Press 'y' for YES or 'n' for NO. ")

    # if hit == "y":
    while hit == "y":
        new_player_card = random.choice(cards)
        player_hand.append(new_player_card)
        player_score += new_player_card
    
        if player_score > 21:
            if 11 in player_hand:
                player_hand = [1 if item == 11 else item for item in player_hand]
                new_player_score = sum(player_hand)
                player_score = new_player_score
                
                if player_score == 21:
                    blackjack()
                    quit()
                elif player_score > 21:
                    bust()
                    quit()
                else:
                    print(f"\nYour hand is {player_hand}, current score: {player_score}")
                    print(f"\nDealer's first card is {dealer_card1}")
                    hit = input("Do you want to draw another card? Press 'y' for YES or 'n' for NO. ")
            else:
                bust()
                quit()
        elif player_score == 21:
            blackjack()
            quit()
        else:
            print(f"\nYour hand is {player_hand}, current score: {player_score}")
            print(f"\nDealer's first card is {dealer_card1}")
            hit = input("Do you want to draw another card? Press 'y' for YES or 'n' for NO. ")
                
    # elif hit == "n":
    print("\nYou decided not to hit.")
    if player_score > 21:
        bust()
    elif player_score == 21:
        blackjack()
    elif player_score < dealer_score:
        lose()
    elif player_score > dealer_score:
        if dealer_score > 16:
            win()
        else:
            while dealer_score < 16:
                print(f"\nDealer's first two cards are {dealer_hand}.")
                new_dealer_card = random.choice(cards)
                dealer_hand.append(new_dealer_card)
                dealer_score += new_dealer_card
                print(f"Dealer draws again. It's a {new_dealer_card}.\n")
                
            if dealer_score > 21:
                dealer_bust()
            elif player_score < dealer_score:
                lose()
            elif player_score > dealer_score:
                win()
            else:
                draw()
    else:
        draw()