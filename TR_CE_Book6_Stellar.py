#
# Cepheus Engine Extension - Stellar Dats Generation
#
# About:
#
# This module generates stellar data for Cepheus Engine based on the CT Book 6 method
#

#
# Version:  0.1
# Author:   Michael Bailey
# Date:     13 August 2020
#

# Constructor:  Stellar()
#
# Public methods:
# 
# 
#

# Import modules here

import random
from multipledispatch import dispatch
from TR_Support import D6Roll, D6Rollx2, D10Roll, D100Roll, D200Roll, D1000Roll, D100KRoll


# Define common functions

    # Detemine the system nature (number of stars)

def genSystemNature():

    x = D6Rollx2()
    if x < 8: nStars = 1
    elif x < 12: nStars = 2
    else: nStars = 3
    return nStars

def genStarType(modifier):

    retlist = []

    x = D6Rollx2() + modifier

    if x < 0: sType = 'O'
    elif x < 2: sType = 'B'
    elif x < 3: sType = 'A'
    elif x < 5: sType = 'F'
    elif x < 7: sType = 'G'
    elif x < 9: sType = 'K'
    else: sType = 'M'

    retlist.append(sType)
    retlist.append(x)

    return retlist

def genStarSize(modifier):

    retlist = []

    x = D6Rollx2() + modifier

    if x <= 0: sSize = 'Ia'
    elif x <= 1: sSize = 'Ib'
    elif x <= 2: sSize = 'II'
    elif x <= 3: sSize = 'III'
    elif x <= 4: sSize = 'IV'
    elif x <= 10: sSize = 'V'
    elif x <= 11: sSize = 'VI'
    else: sSize = 'D'

    retlist.append(sSize)
    retlist.append(x)

    return retlist

def genSpectralNumber():
    return D10Roll() - 1

# Functions for continued and expanded system generation

# Continued sysgen takes a World object as a parameter

@dispatch(object)
def genStellar(mainWorldObject):

# Will need logic here to check that the passed object parameter is or inherits from TR_CE_World

        pass

# Expanded generation - build it from scratch and return a list of stellar list string

@dispatch()
def genStellar():

    starType = []
    starSize = []
    starSpNum = []
    star = {}
    
    starCount = genSystemNature()

    # Determine primary characteristics

    mod = 0

    starType.append(genStarType(mod))
    starSize.append(genStarSize(mod))
    starSpNum.append(genSpectralNumber())

    star['Primary'] = starSize[0] 
    
    if starCount >= 2:

        # Determine companion charaxcteristics, using primary rolls as DM as necessary

        starType.append(genStarType(starType[0][1]))
        starSize.append(genStarSize(starSize[0][1]))
        starSpNum.append(genSpectralNumber())

        # Determine tertiary charaxcteristics, using primary rolls as DM as necessary

        if starCount >= 3:

            starType.append(genStarType(starType[0][1]))
            starSize.append(genStarSize(starSize[0][1]))
            starSpNum.append(genSpectralNumber())

    
    # Verify the stars and eliminate known bads

    i = 0
    while i < 3 and i < starCount:
        if starSize[i][0] == 'IV' and starType[i][0] in ['K', 'M']:
            if starType[i][0] == 'K' and starSpNum[i] > 5: starSize[i][0] = 'V'
            elif starType[i][0] == 'M': starSize[i][0] = 'V'

        if starSize[i][0] == 'VI' and starType[i][0] in ['B', 'F']:
            if starType[i][0] == 'B': starSize[i][0] = 'V'
            elif starType[i][0] == 'F' and starSpNum[i] <= 4: starSize[i][0] = 'V'
            
        i += 1
    
    # Generate the string for the first star

    stellarString = starType[0][0] + str(starSpNum[0]) + ' ' + starSize[0][0]

    # Append the second star details

    if starCount >= 2: stellarString += ' ' + starType[1][0] + str(starSpNum[1]) + ' ' + starSize[1][0]

    # Append the third star details

    if starCount >= 3: stellarString += ' ' + starType[2][0] + str(starSpNum[2]) + ' ' + starSize[2][0]

    return stellarString


#####
# Test code here

i = 0
while i < 10:
    a = genStellar()
    print(a)
    i += 1







