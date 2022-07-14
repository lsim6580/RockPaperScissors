from enum import Enum
import random
class Announcer:

    
    def start_game(self):
        print("Lets Play Rock, Paper, Scissors")
        print("ROCK!")
        print("PAPER!")
        print("SCISSORS!")
    def announce_winner(self, winner_name):
        print(f"{winner_name} Has won")

class ROCK_PAPER_SCISSORS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
def main():
    announcer = Announcer()
    announcer.start_game()
    winner = 0
    while winner == 0:
        selections = playersTurn()
        winner = winningSelection(selections[0], selections[1])
        if(winner == -1):
            announcer.announce_winner("money")
        elif(winner == 1):
            announcer.announce_winner("dog")
    announcer = Announcer()


    return

def playersTurn():
    userSelection = int(input("SHOOT! (1 = rock, 2 = paper, 3 = scissors): "))
    userOptionSelection = ROCK_PAPER_SCISSORS(userSelection)
    computerSelection = random.choice([1,2,3])
    computerOptionSelection = ROCK_PAPER_SCISSORS(computerSelection)
    print("You selected {option}".format(option = userOptionSelection))
    print("Bob selected {option}".format(option = computerOptionSelection))
    return [userOptionSelection, computerOptionSelection]

def winningSelection(user, computer):
    if(user == ROCK_PAPER_SCISSORS.ROCK):
        if(computer == ROCK_PAPER_SCISSORS.ROCK):
            return 0
        elif(computer == ROCK_PAPER_SCISSORS.PAPER):
            return 1
        else:
            return -1
    elif(user == ROCK_PAPER_SCISSORS.PAPER):
        if(computer == ROCK_PAPER_SCISSORS.ROCK):
            return -1
        elif (computer == ROCK_PAPER_SCISSORS.PAPER):
            return 0
        else:
            return 1
    else:
        if(computer == ROCK_PAPER_SCISSORS.ROCK):
            return 1
        elif(computer == ROCK_PAPER_SCISSORS.PAPER):
            return -1
        else:
            return 0

main()