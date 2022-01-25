import pandas as pd
import numpy as np

colors={'Lead':'#DB3838',
 'Position':'#AAE10D',
 'Evidence':'#0DE1A7',
 'Claim':'#DF3CEC',
 'Concluding Statement':'#7c9bf7',
 'Counterclaim':'#FFF942',
 'Rebuttal':'#FFCE26',
       'None':'#FFFFFF'}

def render_html(df):
    return f"<span style='background-color:{colors[df['discourse_type']]}'> {df['discourse_text']} </span> <span style='background-color:{colors[df['discourse_type']]} '> [{df['discourse_type']}] </span>"
