import random


def main():
    # greets our player
    print('Welcome to Rock, Paper or Scissors! ')
    # this will validate the users response to see if they want to play
    while play_or_nah():
        play_game()


def play_or_nah():
    choice = input("Would you like to play? Y or N? ").lower()
    if choice == 'y':
        # if they enter the correct key this will start the game function
        return True
    # if they dont want to play this will run
    elif choice == 'n':
        print('Sorry to see you go, until next time then! ')
        return False
    # if they do not enter y or n this will ask them to answer again
    else:
        print('That is not a valid response ')
        return play_or_nah()


def play_game():
    # this is the actual game play function
    # ask user what they want to play
    player_choice = input("Please enter 'Rock' 'Paper' or 'Scissors' For your play: ").lower()
    # this will check the users play to ensure it is a valid choice
    if check_if_valid(player_choice):
        # if this runs it means the choice was valid and the game moves on storing the now all
        # this will grab the random choice for the "computer"'s choice
        computer_choice = computer_play().lower()
        # variable to store the winning statement
        champ = determine_winner(player_choice, computer_choice)
        # prints the winner
        print(champ)
    else:
        # if this runs it means the users choice was invalid
        print('Please follow instructions:')
        # starts over


def check_if_valid(player_option) -> bool():
    # this function returns a boolean answer to whether the users choice was among the valid
    # choices contained in this list of strings or not
    valid_choices = ['rock', 'paper', 'scissors']
    if player_option in valid_choices:
        return True
    else:
        return False


def computer_play():
    # this function creates a random int and uses it to select a play for the computer
    choices = ['Rock', 'Paper', 'Scissors']
    # compute_random = random.randint(1, 4)
    computer_choice = random.choice(choices)
    return computer_choice


def determine_winner(player_choice, computer_choice):
    # this compares the various outcome of the game and returns the winner
    tie = 'No winner, it was a draw'
    if player_choice == computer_choice.lower():
        winner = tie
    elif player_choice == 'rock' and computer_choice == 'scissors':
        winner = 'Rock smashes scissors, player one wins! '
    elif player_choice == 'scissors' and computer_choice == 'paper':
        winner = 'Scissors cut paper, player one wins! '
    elif player_choice == 'paper' and computer_choice == 'rock':
        winner = 'Paper covers Rock, player one wins! '
    else:
        winner = 'Computer wins, you lose! '
    return winner


main()
