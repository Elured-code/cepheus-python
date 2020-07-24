#
# Cepheus Engine Extension - Stellar Dats Generation
#
# About:
#
# This module generates stellar data for Cepheus Engine based on Population I distribution

#
# Version:  0.1
# Author:   Michael Bailey
# Date:     24 July 2020
#

# Constructor:  Stellar()
#
# Public methods:
# 
# 
#

#
# Things to do:
#
#  Add 'Traveller-esque' stellar data generation
# 


# Import modules here

import random

# Define common functions

# Determine the star type
# Note that at the moment this is the same for single, binary and trinary systems, 
# when I have more information I will change

def gen_starType(pType):
    
    # Primary generation

    random.seed()
    i = random.randint(1, 200)

    if i <= 185: returnval = 'V'
    elif i <= 197: returnval = 'D'
    elif i <= 199: returnval = 'III'
    else: returnval = 'VI'

    # Drill down further into giants to tease our the (very rare) super giants
    # Hyper giants are too rare and should be added manually if required

    if returnval == 'III':
        j = random.randint(1, 100)
        if j > 95 and j < 100: returnval = 'II'
        elif j == 100: returnval = 'I'

    # Further restrict based on the primary type

    if pType == 'V':
        if returnval in ['I', 'II', 'III', 'V']:

            # Main sequence stars should not have giant companions

            k = random.randint(1, 100)
            if k < 65: returnval = 'D'
            elif k < 99: returnval = 'V'
            else: returnval = 'VI'

    # Subdwarfs and dwarfs get dwarfs

    elif pType in ['D', 'VI']: 
        returnval = 'D'

    # Type II giants
    
    elif pType == 'II' and returnval == 'I':
        l = random.randint(1, 1000)
        if l <= 600: returnval = 'V'
        elif l <= 995: returnval = 'D'
        elif l <= 998: returnval = 'III'
        elif l <= 999: returnval = 'II'

    # Type III giants

    elif pType == 'III' and returnval in ['I', 'II']:
        l = random.randint(1, 1000)
        if l <= 600: returnval = 'V'
        elif l <= 995: returnval = 'D'
        elif l <= 998: returnval = 'III'

    return returnval

def gen_Spectral(sType):
    # Now determine the spectral class

    spec = ""
    if sType in ['I', 'II', 'III']:
        m = random.randint(1, 100)
        if m < 30: spec = 'B'
        elif m < 50: spec = 'A'
        elif m < 60: spec = 'F'
        elif m < 75: spec = 'G'
        elif m < 85: spec = 'K'
        else: spec = 'M'
    elif sType == 'V':
        m = random.randint(1, 100000)
        if m == 1: spec = 'O'
        elif m < 130: spec = 'B'
        elif m < 730: spec = 'A'
        elif m < 3730: spec = 'F'
        elif m < 11330: spec = 'G'
        elif m < 23430: spec = 'K'
        else: spec = 'M'
    elif sType == 'VI':
        m = random.randint(1, 100)
        if m <= 30: spec = 'G'
        elif m <= 60: spec = 'K'
        else: spec = 'M'
    if sType == "D": spec = ""

    if spec != "":
        n = random.randint(0, 9)
        spec += str(n) + " "

    return spec



# Define constants

# Class definition

class Stellar:

# Define properties

    @property
    def nStars(self):
        return self.__nStars

    @property
    def starList(self):
        return self.__starList

    @property
    def spectraList(self):
        return self.__spectraList

# Define setters, including checks

    @nStars.setter
    def nStars(self, nStars):
        if nStars < 1: self.__nStars = 1

        # Note, limiting members to 3 for now

        elif nStars > 3: self.__nStars = 3
        else: self.__nStars = nStars

    @starList.setter
    def starList(self, starList):
        self.__starList = starList

    @spectraList.setter
    def spectraList(self, spectraList):
        self.__spectraList = spectraList

# Initialise the class

    def __init__(self):
        self.nStars = 1
        self.starList = []


# Class methods

# Determine the number of stars in the system

    def gen_nStars(self):
        random.seed()
        i = random.randint(1, 100)

        if i <= 56: self.nStars = 1
        elif i <= 91: self.nStars = 2
        else: self.nStars = 3



# Generate the stellar data using the methods defined above

    def genStellar(self):
        self.gen_nStars()

        # Determine the primary type
        
        tP = gen_starType('x')
        sP = gen_Spectral(tP)

        self.starList.append(sP + tP)

        # Determine the secondary type if present

        if self.nStars >= 2: 
                tS = gen_starType(tP)
                sS = gen_Spectral(tS)
                self.starList.append(sS + tS)
        if self.nStars == 3: 
                tT = gen_starType(tP)
                sT = gen_Spectral(tT) 
                self.starList.append(sT + tT)   
        
