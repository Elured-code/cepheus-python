#
# Cepheus Engine Support functions and data
# 
#
# Author:   Michael Bailey
# Date:     6 August 2020
#

# Import modules here

import random

# Define common functions

# Dice rollers

def D6Rollx2():
    random.seed()
    return random.randint(1, 6) + random.randint(1, 6)

def D6Roll():
    random.seed()
    return random.randint(1, 6)

def D6Rollx3():
    random.seed()
    return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

def D10Roll():
    random.seed()
    return random.randint(1, 10)

def D100Roll():
    random.seed()
    return random.randint(1, 100)

def D200Roll():
    random.seed()
    return random.randint(1, 200)

def D1000Roll():
    random.seed()
    return random.randint(1, 1000)

def D100KRoll():
    random.seed()
    return random.randint(1, 100000)