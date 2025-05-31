# coding=utf-8

"""This is the code template for random testinjg

Author: Jason Tam
Email: jasonyctam@gmail.com
"""

import time
from termcolor import colored # For printing coloured text in terminal
import colorama # For making coloured text work in Git Bash (MinuTTY)
import json
import pandas as pd


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

        return

###################################################################
###################################################################

    def run(self):
        """
        This method is executed when this code is executed independently
        """

        file_name = 'sample.json'

        json_object = self.load_json(file_name)

        # df = pd.read_json(file_name)
        df = pd.DataFrame.from_dict(json_object, orient='index')

        print(df)

        # print(json.dumps(json_object, indent=4))
        # print(type(json_object))

        return

###################################################################
###################################################################

    def load_json(self, file_name: str) -> dict:

        # Opening JSON file
        with open(file_name, 'r') as openfile:

            # Reading from json file
            json_object = json.load(openfile)

        return json_object

###################################################################
###################################################################

if __name__ == "__main__":

    startTime = time.time()

    Analysis_Object = mainAnalysis()

    Analysis_Object.run()

    endTime = time.time()

    print("")
    print (colored("Time elapsed: " + repr(endTime-startTime), "green"))