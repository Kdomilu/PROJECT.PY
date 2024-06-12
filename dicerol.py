import random  # Import the random module to use for generating random numbers

# Function to simulate rolling a die
def roll():
    min_value = 1  
    max_value = 6
    result = random.randint(min_value, max_value)  # Generate a random number between 1 and 6
    return result  # Return the result of the roll

# Ask the user for the number of players (between 2 and 4)
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():  # Check if the input is a digit
        players = int(players)  # Convert the input to an integer
        if 2 <= players <= 4:  # Check if the number of players is between 2 and 4
            break  # Exit the loop if valid
        else:
            print("Must be between 2 - 4 players.")  # Inform the user if the number is out of range
    else:
        print("Invalid, try again.")  # Inform the user if the input is not a number

max_score = 50  # The score needed to win the game
# Initialize player scores to 0 using list comprehension
player_scores = [0 for _ in range(players)]

# Loop until one of the players reaches the max score
while max(player_scores) < max_score:
    for player_idx in range(players):  # Iterate through each player
        print("\nPlayer", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0  # Initialize current turn score

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() == "y":  # If the player wants to roll the die
                value = roll()  # Roll the die
                if value == 1:  # If the player rolls a 1
                    print("You rolled a 1! Turn done!")
                    current_score = 0  # The turn score is reset to 0
                    break  # End the player's turn
                else:
                    current_score += value  # Add the roll value to the current turn score
                    print("You rolled a:", value)
            else:
                break  # End the player's turn if they don't want to roll

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score  # Add the current turn score to the player's total score
        print("Your total score is:", player_scores[player_idx])

# Determine the winner
max_score = max(player_scores)  # Find the highest score
winning_idx = player_scores.index(max_score)  # Find the index of the highest score
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)
