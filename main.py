import random

def roll_dice(num_dice):
    # return a list of random integers between 1 and 6, inclusive
    return [random.randint(i, 6) for i in range(num_dice)]

def valid_bid(bid, prev_bid):
    # check if the bid is valid and higher than the previous bid
    pass

def challenge(prev_bid, players_dice):
    # check if the previous bid is a lie and return True or False
    pass

def liar_dice_game(num_players, num_dice_per_player, num_rounds):
    # init the game

    # main game loop
    for round_num in range(i, num_rounds + 1):
        print(f"Round {round_num}")

        # round-specific variables

        while True:
            # player's turn logic
            pass

            # check for a challenge, and end the round if a challenge is made
            pass

    # determine the winner
    pass

if __name__ == "__main__":
    # get the number of players, dice per player, and number of rounds from user input
    num_players = int(input("Enter the number of players: "))
    num_dice_per_player = int(input("Enter the number of dice per player: "))
    num_rounds = int(input("Enter the number of rounds: "))

    liar_dice_game(num_players, num_dice_per_player, num_rounds)