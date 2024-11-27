# Authors: Zane Dalco, Taj Hunter, Rohan Mehta
# Project: The Art of War: A Strategic Journey in a 52-Card World
# Date: November 2023

# - - - -  - - - - - - - - - - - - - - - - - - 

from tkinter import *
import random
from PIL import Image, ImageTk
import pygame


# -------------- MUSIC -------------------


pygame.init()
pygame.mixer.music.load("images/music.mp3")  
pygame.mixer.music.set_volume(0.5)  

# Play the music on loop
pygame.mixer.music.play(-1)



# --------------- TITLE ---------------

# Gives Title and Size of the App
root = Tk()
root.title('---  WAR --- ')
root.geometry("1250x650")


# ---------------- BACKGROUND -------------


# Load the image
background_img = Image.open("images/greengs.jpg")  
background_photo = ImageTk.PhotoImage(background_img)

# Create a Label to display the image
background_label = Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)



# ------------------- FUNCTIONS ----------------

                

            # - - - Resize Function - - -

# Function Designed to Resize the Images of the Cards
def resize_cards(card):
    card_img = Image.open(card)
    card_resize_image = card_img.resize((165, 225))

    global card_image
    card_image = ImageTk.PhotoImage(card_resize_image)

    return card_image




    # - - - Shuffle Cards Function - - -



def shuffle():
    # Define the suits for the deck
    suits = ["diamonds", "clubs", "hearts", "spades"]
    
    # Define the range of card values from 2 to 14 (inclusive)
    values = range(2, 15)

    # Initialize an empty deck
    global deck
    deck = []

    # Create a deck by combining each suit with each value
    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    # Initialize empty lists to store cards for dealer and player, and scores for both
    global dealer, player, dscore, pscore
    dealer = []
    player = []
    dscore = []
    pscore = []

    # Dealer draws a card from the deck
    dealer_card = random.choice(deck)
    deck.remove(dealer_card)
    dealer.append(dealer_card)

    # Resize the card image for the dealer and update the UI
    global dealer_image
    dealer_image = resize_cards(f'images/cards/{dealer_card}.png')
    dealer_label.config(image=dealer_image)

    # Player draws a card from the deck
    player_card = random.choice(deck)
    deck.remove(player_card)
    player.append(player_card)

    # Resize the card image for the player and update the UI
    global player_image
    player_image = resize_cards(f'images/cards/{player_card}.png')
    player_label.config(image=player_image)

    # Update the window title with the number of cards left in the deck
    root.title(f'--- WAR  --- {len(deck)} Cards Left')

    # Calculate and display the scores for the initial cards
    score(dealer_card, player_card)




#         - - -  Rules Function - - -

def game_rules():
    rules_text = """WELCOME TO WAR!:

HERE ARE THE RULES:

1. Objective:
   - The goal of the game is to finish with the most Points/Cards

2. Setup:
   - The deck is shuffled, and is dealt evenly to each player every round.

3. Gameplay:
   - Players simultaneously reveal their card.
   - The player with the higher-ranked card wins both cards and receives a point.

4. Card Ranking:
   - Cards are ranked from 2 (lowest) to Ace (highest).
   - Suits are irrelevant in this game.

5. Ties:
   - In the event of a tie (both players play cards of the same rank), a "war" is declared.
   - Another round is played and the player with the higher-ranked card wins the card and receives the point

6. Game Over:
   - The game continues until there are no cards left.
   
   GOOD LUCK & HAVE FUN!
"""
    
    # Create a new window for displaying the rules
    rules_window = Toplevel(root)
    rules_window.title("Game Rules")
    
    # Display the rules text in a Label widget
    rules_label = Label(rules_window, text=rules_text, font=("Georgia", 14), padx=20, pady=20)
    rules_label.pack()




#           - - - Dealing / Showing Cards Function - - -

# This function is responsible for dealing cards to the dealer and player,
# updating the UI, and calculating and displaying the scores.
def deal_cards():
    try:
        # Dealer draws a card from the deck
        dealer_card = random.choice(deck)
        deck.remove(dealer_card)
        dealer.append(dealer_card)
        # Resize the card image for the dealer and update the UI
        global dealer_image
        dealer_image = resize_cards(f'images/cards/{dealer_card}.png')
        dealer_label.config(image=dealer_image)

        # Player draws a card from the deck
        player_card = random.choice(deck)
        deck.remove(player_card)
        player.append(player_card)
        # Resize the card image for the player and update the UI
        global player_image
        player_image = resize_cards(f'images/cards/{player_card}.png')
        player_label.config(image=player_image)

        # Update the window title with the number of cards left in the deck
        root.title(f'--- WAR --- {len(deck)} Cards Left')

        # Calculate and display the scores
        score(dealer_card, player_card)
    except:
        # Handle exceptions, such as when the deck is empty
        if dscore.count("x") == pscore.count("x"):
            root.title(f'--- WAR ---  GAME OVER!    ITS A TIE! {dscore.count("x")} to {pscore.count("x")}')
        elif dscore.count("x") > pscore.count("x"):
            root.title(
                f'--- WAR ---    GAME OVER!    THE DEALER WINS!      FINAL SCORE :   DEALER : {dscore.count("x")}   PLAYER :  {pscore.count("x")}')
        else:
            root.title(
                f'--- WAR ---    GAME OVER!       PLAYER WINS!       FINAL SCORE :   PLAYER : {pscore.count("x")}   DEALER :  {dscore.count("x")}')



#               - - - Score Tracker Function - - -

# This function calculates and updates the scores based on the drawn cards.
def score(dealer_card, player_card):
    dealer_card = int(dealer_card.split("_", 1)[0])
    player_card = int(player_card.split("_", 1)[0])

    if dealer_card == player_card:
        # It's a tie
        score_label.config(text="ITS A TIE! PLAY AGAIN!", font=("Georgia", 18, "bold"), bg="#009416")

    elif dealer_card > player_card:
        # Dealer wins
        score_label.config(text="THE DEALER WINS!", font=("Georgia", 18, "bold"), bg="#009416")
        dscore.append("x")

    else:
        # Player wins
        score_label.config(text="PLAYER WINS!", font=("Georgia", 18, "bold"), bg="#009416")
        pscore.append("x")

    # Update the window title with the current scores and remaining cards in the deck
    root.title(
        f'         ---   WAR   ---     {len(deck)} Cards Left   |        SCORE :        Dealer: {dscore.count("x")}           Player : {pscore.count("x")}')




#              - - - Player / Dealer Frame - - -

# Create a frame to contain the entire user interface
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create a frame for the dealer's section with a title and formatting
dealer_frame = LabelFrame(my_frame, text="                                   DEALER                       ", bd=0, font=("Georgia", 10,  "bold"))
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

# Create a frame for the player's section with a title and formatting
player_frame = LabelFrame(my_frame, text="                                   PLAYER                       ", bd=0, font=("Georgia", 10,  "bold"))
player_frame.grid(row=0, column=1, ipadx=20)

# Create a label to display the dealer's card image
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

# Create a label to display the player's card image
player_label = Label(player_frame, text='')
player_label.pack(pady=20)

# Create a label to display the game score
score_label = Label(root, text='', font=("Georgia", 16))
score_label.pack(pady=20)




#            - - - Buttons - - -

# Create a button to restart / start a new game when clicked
shuffle_button = Button(root, text="RESTART / NEW GAME ", font=("Georgia", 16), command=shuffle)
shuffle_button.pack(pady=20)

# Create a button to deal cards when clicked
card_button = Button(root, text="DEAL CARDS", font=("Georgia", 16), command=deal_cards)
card_button.pack(pady=20)

# Create a button to display game rules when clicked
rules_button = Button(root, text="RULES", font=("Georgia", 16), command=game_rules)
rules_button.pack(pady=20)

# Shuffle the deck to start the game
shuffle()

root.mainloop()
