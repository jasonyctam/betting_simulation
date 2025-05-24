    # coding=utf-8

"""This is the code template for random testinjg

Author: Jason Tam
Email: jasonyctam@gmail.com
"""

import time
from termcolor import colored # For printing coloured text in terminal
import colorama # For making coloured text work in Git Bash (MinuTTY)
import random


###################################################################
###################################################################
###################################################################
###################################################################

class mainAnalysis():

###################################################################
###################################################################

    def __init__(self):

        __author__ = "Jason Tam"
        __copyright__ = "Copyright 2020"
        __credits__ = ["Jason Tam"]
        __version__ = "1.0"
        __maintainer__ = "Jason Tam"
        __email__ = "jasonyctam@gmail.com"
        __status__ = "Development"

        colorama.init()

        # Define roulette wheel properties
        self.RED_NUMBERS = {
            1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36
        }
        self.BLACK_NUMBERS = {
            2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35
        }

        return

###################################################################
###################################################################

    def run(self):
        """
        This method is executed when this code is executed independently
        """
        # Example use
        result_dict = {'bankroll': 1000}

        results_collection = []

        # Simulate a few rounds
        result_dict = self.simulate_bet("colour", "red", 100, result_dict['bankroll'])
        print(result_dict)
        result_dict = self.simulate_bet("parity", "odd", 50, result_dict['bankroll'])
        print(result_dict)
        result_dict = self.simulate_bet("number", 17, 20, result_dict['bankroll'])
        print(result_dict)

        return

###################################################################
###################################################################

    def spin_wheel(self):
        """
        This method simulates the spinning of the roulette wheel, and returns a random number between 0 and 36 inclusively
        """
        return random.randint(0, 36)

###################################################################
###################################################################

    def get_colour(self, number: int) -> str:
        """
        This method returns the colour of a number on the roulette wheel
        """
        if number == 0:
            return 'green'
        elif number in self.RED_NUMBERS:
            return 'red'
        else:
            return 'black'

###################################################################
###################################################################

    def simulate_bet(self, bet_type, choice, bet_amount, bankroll):
        """
        This method simulates the betting process of a single round in a roulette game
        """
        result_dict = {}

        if bet_amount > bankroll:
            print('Insufficient Funds')
            result_dict = {'bet_result': 'Not played', 'bankroll': bankroll}
            return result_dict

        result = self.spin_wheel()
        colour = self.get_colour(result)
        parity = 'even' if result % 2 == 0 else 'odd'
        print(f"Wheel landed on {result} ({colour})")

        bet_result = ''

        if bet_type == "number":
            if result == choice:
                winnings = bet_amount * 35
                print(f"You won! Payout: {winnings}")
                bankroll += winnings
                bet_result = 'win'
            else:
                print("You lost.")
                bankroll -= bet_amount
                bet_result = 'lose'

        elif bet_type == "colour":
            if colour == choice:
                winnings = bet_amount
                print(f"You won! Payout: {winnings}")
                bankroll += winnings
                bet_result = 'win'
            else:
                print("You lost.")
                bankroll -= bet_amount
                bet_result = 'lose'

        elif bet_type == "parity":
            if result == 0:
                print("You lost.")
                bankroll -= bet_amount
                bet_result = 'lose'
            elif (result % 2 == 0 and choice == "even") or (result % 2 == 1 and choice == "odd"):
                winnings = bet_amount
                print(f"You won! Payout: {winnings}")
                bankroll += winnings
                bet_result = 'win'
            else:
                print("You lost.")
                bankroll -= bet_amount
                bet_result = 'lose'

        output_dict = {}
        output_dict['spin-result'] = result
        output_dict['bet-result'] = bet_result
        output_dict['bankroll'] = bankroll
        output_dict['colour'] = colour
        output_dict['parity'] = parity

        return output_dict

###################################################################
###################################################################

if __name__ == "__main__":

    startTime = time.time()

    Analysis_Object = mainAnalysis()

    Analysis_Object.run()

    endTime = time.time()

    print("")
    print (colored("Time elapsed: " + repr(endTime-startTime), "green"))