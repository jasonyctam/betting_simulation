    # coding=utf-8

"""This is the code template for random testinjg

Author: Jason Tam
Email: jasonyctam@gmail.com
"""

import time
from termcolor import colored # For printing coloured text in terminal
import colorama # For making coloured text work in Git Bash (MinuTTY)
import random
import json
from tqdm import tqdm


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
        self.CONTROL_RESULTS_DIR = "control_results/"

        return

###################################################################
###################################################################

    def run(self):
        """
        This method is executed when this code is executed independently
        """
        # Example use
        # result_dict = {'bankroll': 1000}

        # Simulate a few rounds
        # result_dict = self.simulate_bet("colour", "red", 100, result_dict['bankroll'])
        # print(result_dict)
        # result_dict = self.simulate_bet("parity", "odd", 50, result_dict['bankroll'])
        # print(result_dict)
        # result_dict = self.simulate_bet("number", 17, 20, result_dict['bankroll'])
        # print(result_dict)

        ###################################

        starting_bankroll = 1000
        bet_amount = 10
        repetitions = 100
        iterations = 100

        bet_configurations = {
            "red": {
                "bet_type": 'colour',
                "bet_selection": 'red',
                "bankroll": starting_bankroll,
                "bet_amount": bet_amount,
                "repetitions": repetitions,
                "iterations": iterations
            },
            "black": {
                "bet_type": 'colour',
                "bet_selection": 'black',
                "bankroll": starting_bankroll,
                "bet_amount": bet_amount,
                "repetitions": repetitions,
                "iterations": iterations
            },
            "odd": {
                "bet_type": 'parity',
                "bet_selection": 'odd',
                "bankroll": starting_bankroll,
                "bet_amount": bet_amount,
                "repetitions": repetitions,
                "iterations": iterations
            },
            "even": {
                "bet_type": 'parity',
                "bet_selection": 'even',
                "bankroll": starting_bankroll,
                "bet_amount": bet_amount,
                "repetitions": repetitions,
                "iterations": iterations
            }
        }

        for key in bet_configurations:
            print("Processing control simulation for: " + key)
            control_results = self.control(bet_configurations[key])

            # Writing to sample.json
            json_object = json.dumps(control_results, indent=4)
            with open(self.CONTROL_RESULTS_DIR+key+".json", "w") as outfile:
                outfile.write(json_object)

        return

###################################################################
###################################################################

    def control(self, bet_configurations: dict) -> list[list]:
        #############################
        # Produce control data to examine any intrinsic biases of tools/methods used
        # Start the initial bankroll at an amount, say 1000
        # Keep a constant bet amount, say $10 that is at least a couple of orders magnitude smaller
        # Keep a constant colour or parity bet selection, so that the probability of winning can be reflected on the outcome
        # Each option has a winning probability of 18/37, and a winning return of 200% of the bet amount
        # The end bankroll should theoretically be close to 1000 - (bet_amount * n) + (2 * bet_amount * n * 18/37)
        # For n = 100, 1000 - 10*100 + (2*10*18/37*100) = 972.97 = approximately 973
        #############################

        bet_type = bet_configurations["bet_type"]
        bet_selection = bet_configurations["bet_selection"]
        bankroll = bet_configurations["bankroll"]
        bet_amount = bet_configurations["bet_amount"]
        repetitions = bet_configurations["repetitions"]
        iterations = bet_configurations["iterations"]

        spin_result_iteration_collection = []

        for j in tqdm(range(0,iterations)):
            results_collection = self.generate_repeated_result(repetitions)
            spin_result_iteration_collection.append(results_collection)

        iteration_collection = []
        initial_result_dict = {'bankroll': bankroll}

        for j in tqdm(range(len(spin_result_iteration_collection))):
            repetition_collection = [initial_result_dict]
            results_collection = spin_result_iteration_collection[j]
            bet_result = initial_result_dict
            for i in range(len(results_collection)):
                result = results_collection[i]
                bet_result = self.simulate_betting(bet_type, bet_selection, bet_amount, bet_result['bankroll'], result)
                repetition_collection.append(bet_result)
            iteration_collection.append(repetition_collection)

        return iteration_collection

###################################################################
###################################################################

    def spin_wheel(self) -> int:
        """
        This method simulates the spinning of the roulette wheel, and returns a random number between 0 and 36 inclusively
        """
        return random.randint(0, 36)

###################################################################
###################################################################

    def generate_repeated_result(self, repetitions: int) -> list:
        """
        This method repeats the simulation of spinning of the roulette wheel, and returns a dictionary containing the result of each iteration
        """
        results_list = []

        for i in range(repetitions):
            iteration_dict = {}
            result = self.spin_wheel()
            colour = self.get_colour(result)
            parity = 'even' if result % 2 == 0 else 'odd'
            if result == 0:
                parity = 'zero'
            iteration_dict['spin-result'] = result
            iteration_dict['colour'] = colour
            iteration_dict['parity'] = parity
            results_list.append(iteration_dict)

        return results_list

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

    def simulate_betting(self, bet_type, choice, bet_amount, bankroll, spin_result_dict) -> dict:
        """
        This method simulates the betting result with the output of generate_repeated_result
        """

        result = spin_result_dict['spin-result']
        colour = spin_result_dict['colour']
        parity = spin_result_dict['parity']

        bet_result = ''

        if bet_type == "number":
            if result == choice:
                winnings = bet_amount * 35
                bankroll += winnings
                bet_result = 'win'
            else:
                bankroll -= bet_amount
                bet_result = 'lose'

        elif bet_type == "colour":
            if colour == choice:
                winnings = bet_amount
                bankroll += winnings
                bet_result = 'win'
            else:
                bankroll -= bet_amount
                bet_result = 'lose'

        elif bet_type == "parity":
            if result == 0:
                bankroll -= bet_amount
                bet_result = 'lose'
            elif (result % 2 == 0 and choice == "even") or (result % 2 == 1 and choice == "odd"):
                winnings = bet_amount
                bankroll += winnings
                bet_result = 'win'
            else:
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