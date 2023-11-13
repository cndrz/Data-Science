# Make functions for AI choice.
# Point increment for player and bot.
# Lives decrement for player and bot.
# 1 = Rock, 2 = Paper, 3 = Scissors

import random

def Player():
    while True:
        player = int(input("Enter choice: "))
        if player in [1, 2, 3]:
            print(f"Player -> {'Rock' if player == 1 else 'Paper' if player == 2 else 'Scissors'}")
            return player
        else:
            print("Invalid Input. Try Again")

def AI():
    bot = random.randint(1, 3)
    print(f"Bot -> {'Rock' if bot == 1 else 'Paper' if bot == 2 else 'Scissors'}")
    return bot

def PS_LS(player, bot):
    pp = 0
    bp = 0

    pl = 5  # Player life
    bl = 5  # Bot life

    while pl > 0 and bl > 0:
        if player == bot:
            print("Tie")
            pp += 5
            bp += 5
        elif player == 1 and bot == 2:
            bp += 10
            pl -= 1
        elif player == 1 and bot == 3:
            pp += 10
            bl -= 1
        elif player == 2 and bot == 1:
            pp += 10
            bl -= 1
        elif player == 2 and bot == 3:
            bp += 10
            pl -= 1
        elif player == 3 and bot == 1:
            bp += 10
            pl -= 1
        elif player == 3 and bot == 2:
            pp += 10
            bl -= 1
    
        print(f"Player Points -> {pp} | Player Life -> {pl}")
        print(f"Bot Points -> {bp} | Bot Life -> {bl}")

        if pl == 0:
            print("Bot Win. Game Over.")
            break
        elif bl == 0:
            print("Player Win. Game Over.")
            break

        # Get choices from Player and AI for the next round
        player = Player()
        bot = AI()

# Start the game
player_choice = Player()
bot_choice = AI()
PS_LS(player_choice, bot_choice)
















