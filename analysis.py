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
from scipy.stats import norm
import numpy as np


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

        # Extract final bankrolls
        final_bankrolls = [trace[-1]["bankroll"] for trace in results]

        # Fit normal distribution
        mu, std = norm.fit(final_bankrolls)

        # Create y values (bankroll) and corresponding x values (PDF)
        y_vals = np.linspace(min(final_bankrolls) - 3*std, max(final_bankrolls) + 3*std, 200)
        pdf_vals = norm.pdf(y_vals, mu, std)

        # Normalize PDF height to match the y-axis scale (e.g., max bankroll)
        pdf_scaled = pdf_vals * max(final_bankrolls) * 2  # Scale for visibility

        # Add vertical normal distribution on secondary x-axis
        fig.add_trace(go.Scatter(
            x=pdf_scaled + len(results[0]) + 1,  # offset to right of plot
            y=y_vals,
            mode='lines',
            line=dict(color='cyan', width=2, dash='dot'),
            hovertemplate=(
                    "μ (mean): %{customdata[0]:.2f}<br>" +
                    "σ (std): %{customdata[1]:.2f}<extra></extra>"
                ),
            customdata=np.column_stack([[mu] * len(y_vals), [std] * len(y_vals)]),
            showlegend=False
        ))

        fig.update_layout(
            title="Bankroll Evolution",
            xaxis_title="Round",
            yaxis_title="Bankroll",
            template='plotly_dark',
            hovermode='closest',  # disables hover behavior entirely
            hoverlabel=dict(
                bgcolor='#222',  # dark grey background
                font=dict(color='#00ffff')  # cyan text
            )
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