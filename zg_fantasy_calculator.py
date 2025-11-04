## Fantasy Sports Estimator API Functions 
## By: Zach Gozlan, Data Strategy
## Last Updated 4 November 2025

## This is a migration of previously-developed functions to a separate scirpt. 

#__all__ = [score_generator, score_generator2, prob_10k]

import requests
import json 
import math 
import pandas as pd
import numpy as np

def score_generator(table, team, week, wobble):

# "remaining table" is a pandas dataframe of the teams and their 
# actual or expected scores for the remaininder of the season   

    try:
        mu = table.loc[team][week]
        predict = np.random.normal(loc=mu, scale=wobble)
        return(predict)
    except: #bye weeks (in playoffs)
        return(0)

def score_generator2(table, team, week):
# same as above but returns the projected average
    try:
        mu = table.loc[team][week]
        return(mu)
    except: #bye weeks (in playoffs)
        return(0)
        
def prob_10k(score1, score2, wobble):
# uses two projected to estimate % chance of victory for each team in matchup
    j = 0
    for i in range(0,100000):
        x = np.random.normal(loc=score1, scale=wobble)
        y = np.random.normal(loc=score2, scale=wobble)
        if x > y:
            j = j + 1
    return(j/100000)