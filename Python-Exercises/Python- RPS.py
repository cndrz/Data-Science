import random

ROCK, PAPER, SCISSORS = 1, 2, 3

def get_player_choice():
    while True:
        player = int(input("Enter choice (1: Rock, 2: Paper, 3: Scissors): "))
        if player in [ROCK, PAPER, SCISSORS]:
            print(f"Player -> {'Rock' if player == ROCK else 'Paper' if player == PAPER else 'Scissors'}")
            return player
        else:
            print("Invalid Input. Try Again")

def get_ai_choice():
    bot = random.randint(1, 3)
    print(f"Bot -> {'Rock' if bot == ROCK else 'Paper' if bot == PAPER else 'Scissors'}")
    return bot

def play_game(player, bot):
    player_points = 0
    bot_points = 0

    player_life = 5
    bot_life = 5

    while player_life > 0 and bot_life > 0:
        if player == bot:
            print("Tie")
            player_points += 5
            bot_points += 5
        elif (player == ROCK and bot == PAPER) or (player == PAPER and bot == SCISSORS) or (player == SCISSORS and bot == ROCK):
            bot_points += 10
            player_life -= 1
        else:
            player_points += 10
            bot_life -= 1

        print(f"Player Points -> {player_points} | Player Life -> {player_life}")
        print(f"Bot Points -> {bot_points} | Bot Life -> {bot_life}")

        if player_life == 0:
            print("Bot Win. Game Over.")
            break
        elif bot_life == 0:
            print("Player Win. Game Over.")
            break

        # Get choices from Player and AI for the next round
        player = get_player_choice()
        bot = get_ai_choice()

# Start the game

print("1 Rock, 2 Paper, 3 Scissors")
player_choice = get_player_choice()
bot_choice = get_ai_choice()
play_game(player_choice, bot_choice)
