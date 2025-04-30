# Write a class called Rock_paper_scissors that implements the logic of the game Rock paper-
# scissors. For this game the user plays against the computer for a certain number of rounds.

# Your class should have fields for the how many rounds there will be, the current round number,
# and the number of wins each player has. There should be methods for getting the computer’s
# choice, finding the winner of a round, and checking to see if someone has one the (entire)
# game. You may want more methods.
import random


class RockPaperScissors:
    def __init__(self, total_rounds):
        self.total_rounds = total_rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.user_wins += 1
            return "user"
        else:
            self.computer_wins += 1
            return "computer"

    def check_game_winner(self):
        if self.user_wins > self.total_rounds // 2:
            return "user"
        elif self.computer_wins > self.total_rounds // 2:
            return "computer"
        return None

    def play_round(self, user_choice):
        self.current_round += 1
        computer_choice = self.get_computer_choice()
        round_winner = self.find_winner(user_choice, computer_choice)
        return computer_choice, round_winner