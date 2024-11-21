import random

board_size = 50

snakes = {11: 2, 44: 33, 10: 7, 24: 10}
ladders = {16: 22, 34: 40, 10: 24, 28: 38, 18: 29}

def roll_dice():
    
    return random.randint(1, 6)

def move_player(player_pos):
    
    dice_value = roll_dice()
    print(f"Dice rolled: {dice_value}")
    player_pos += dice_value

    if player_pos > board_size:
        
        player_pos -= dice_value
        print(f"Overshot! Staying at {player_pos}")
        return player_pos

    print(f"Player moves to: {player_pos}")

    if player_pos in snakes:
        print(f"Oh no! Landed on a snake at {player_pos}. Going down to {snakes[player_pos]}")
        player_pos = snakes[player_pos]
    elif player_pos in ladders:
        print(f"Great! Landed on a ladder at {player_pos}. Climbing up to {ladders[player_pos]}")
        player_pos = ladders[player_pos]

    print(f"Player is now at: {player_pos}")
    return player_pos

def play_game():
    
    player_position = 0

    while player_position < board_size:
        input("Press Enter to roll the dice: ")
        player_position = move_player(player_position)

    print("Congratulations! You reached the finish line!")

play_game()
