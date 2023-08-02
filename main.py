import random

def roll_dice(num_dice):
    # return a list of random integers between 1 and 6, inclusive
    return [random.randint(i, 6) for i in range(num_dice)]

def valid_bid(bid, prev_bid):
    # check if the bid is valid and higher than the previous bid
    if bid[0] < prev_bid[0]:
        return False
    elif bid[0] == prev_bid[0] and bid[1] <= prev_bid[1]:
        return False
    return True

def challenge(prev_bid, players_dice):
    # check if the previous bid is a lie and return True or False
    face_value, quantity = prev_bid
    total_dice_count = sum(players_dice.values())

    return total_dice_count < quantity or players_dice[face_value] < quantity

def liar_dice_game(num_players, num_dice_per_player, num_rounds):
    # init the game
    players_dice = {player: num_dice_per_player for player in range(1, num_players + 1)}

    # main game loop
    for round_num in range(1, num_rounds + 1):
        print(f"Round {round_num}")
        # round-specific variables
        current_bid = (0, 0)
        current_player = random.randint(1, num_players)

        while True:
            # player's turn logic
            print(f"Player {current_player}'s turn")
            print(f"Current bid: {current_bid}")

            # get the player's bid
            player_input = input("Enter your bid as 'face_value quantity': ")
            face_value, quantity = map(int, player_input.split())

            bid = (face_value, quantity)
            
            if valid_bid(bid, current_bid):
                # update the current bid
                current_bid = bid
                # update the current player
                current_player = (current_player % num_players) + 1
            else:
                print("Invalid bid. Try again.")
                continue
            
            # check for a challenge, and end the round if a challenge is made
            challenge_input = input("Challenge? (y/n): ")
            if challenge_input.lower() == 'y':
                if challenge(current_bid, players_dice):
                    # the challenge was successful
                    print(f"Player {current_player} was lying! They lose a die.")
                    players_dice[current_player] -= 1
                else:
                    # the challenge was unsuccessful
                    print(f"Player {current_player} was telling the truth! The challenger loses a die.")
                    players_dice[current_player % num_players + 1] -= 1
                break

    # determine the winner
    winner = max(players_dice, key = players_dice.get)
    print(f"\nPlayer {winner} wins the game with {players_dice[winner]} dice remaining!")

if __name__ == "__main__":
    # get the number of players, dice per player, and number of rounds from user input
    num_players = int(input("Enter the number of players: "))
    num_dice_per_player = int(input("Enter the number of dice per player: "))
    num_rounds = int(input("Enter the number of rounds: "))

    liar_dice_game(num_players, num_dice_per_player, num_rounds)