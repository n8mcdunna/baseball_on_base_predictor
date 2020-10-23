from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = dcc.Markdown("""
### Introduction
The movie Moneyball first sparked my interest in predicting at bats. At bats in baseball are each time a batter faces a pitcher, and the batter either gets on base or gets out. In the movie one of the important statistics that the movie characters use to build a winning team is the on base percentage. Since this statistic is important in baseball, this app begins to explore the intricacy of the on base percentage by analyzing individual at bats.

This app allow you to create scenarios for a single at bat to predict whether a batter gets on base. Batters, pitchers, teams, weather conditions, and game conditions are all adjustable features. Good luck! 
""")