import random


def main():
    # greets our player
    print('Welcome to Rock, Paper or Scissors! ')
    play = input("Would you like to play? Y or N? ")
    choice = play.lower()
    # this will validate the users response to see if they want to play
    while play:
        if choice == 'y':
            # if they enter the correct key this will start the game function
            play_game()
            # now asks if they want to play again
            play = input("Would you like to play again? Y or N? ")
        elif choice == 'n':
            # if they dont want to play this will run
            print('Sorry to see you go, until next time then! ')
            break
            # if they do not enter y or n this will ask them to answer again
        else:
            play = input("Would you like to play? Y or N? ")


def play_game():
    # this is the actual game play function
    # ask user what they want to play
    option = input("Please enter 'Rock' 'Paper' or 'Scissors' For your play: ").lower()
    # this will check the users play to ensure it is a valid choice
    if check_if_valid(option):
        # if this runs it means the choice was valid and the game moves on storing the now all
        # lowercase choice in this variable
        player_choice = option
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
        play_game()


def check_if_valid(player_option) -> bool():
    # this function returns a boolean answer to whether the users choice was among the valid
    # choices contained in this list of strings or not
    valid_choices = ['rock', 'paper', 'scissors']
    if valid_choices.__contains__(player_option):
        return True
    else:
        return False


def computer_play():
    # this function creates a random int and uses it to select a play for the computer
    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    compute_random = random.randint(1, 4)
    computer_choice = choices[compute_random]
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
