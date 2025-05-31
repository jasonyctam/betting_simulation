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
import plotly.graph_objects as go


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

        self.CONTROL_RESULTS_DIR = "control_results/"

        return

###################################################################
###################################################################

    def run(self):
        """
        This method is executed when this code is executed independently
        """

        file_name = self.CONTROL_RESULTS_DIR+'red.json'

        results = self.load_json(file_name)

        red_control_bankroll = self.plot_bankroll_evolution(results)
        red_control_bankroll.show()

        return

###################################################################
###################################################################

    def plot_bankroll_evolution(self, results: list):

        fig = go.Figure()

        for idx, element_history in enumerate(results):
            bankrolls = [entry["bankroll"] for entry in element_history]
            
            fig.add_trace(go.Scatter(
                x=list(range(len(bankrolls))),
                y=bankrolls,
                mode='lines+markers',
                line=dict(color='lightgrey', width=2),
                marker=dict(
                    size=2,
                    color='lightgrey',
                    line=dict(width=2, color='cyan')
                ),
                opacity=0.1,
                hoverinfo='skip',  # disables hover text
                showlegend=False   # removes legend
            ))

        fig.update_layout(
            title="Bankroll Evolution",
            xaxis_title="Round",
            yaxis_title="Bankroll",
            template='plotly_dark',
            hovermode=False  # disables hover behavior entirely
        )

        return fig

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