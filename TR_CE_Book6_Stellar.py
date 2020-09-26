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

# Constants

# Table of zones - these are dictionaries containing a list of zone boundaries
SIZEIAZONES = {'B0': [8, 12], 'B5': [7, 11], 'A0': [7, 11], 'A5': [7, 11], 'F0': [6, 11], 'F5': [6, 10],
    'G0': [7, 11], 'G5': [7, 11], 'K0': [7, 11], 'K5': [7, 11], 'M0': [7, 11], 'M5': [8, 11], 'M9': [8, 11] }

SIZEVZONES = {'B0': [6, 12], 'B5': [3, 9], 'A0': [0, 7], 'A5': [0, 6], 'F0': [0, 5], 'F5': [0, 4], 'G0': [0, 3],
    'G5': [0, 2], 'K0': [0, 2], 'K5': [0, 0], 'M0': [0, 0], 'M5': [0, -1], 'M9': [0, -1]}



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

def genCompanionOrbit(modifier, primaryType, primarySize):
    x = D6Rollx2() + modifier
    if x <= 3: returnval = 'Close'
    elif x == 4: returnval = 1
    elif x == 5: returnval = 2
    elif x == 6: returnval = 3
    elif x == 7: returnval = 4 + D6Roll()
    elif x == 8: returnval = 5 + D6Roll()
    elif x == 9: returnval = 6 + D6Roll()
    elif x == 10: returnval = 7 + D6Roll()
    elif x == 11: returnval = 8 + D6Roll()
    else: returnval = 'Far'

    # Check that the companion is not inside the primary and adjust accordingly if it is

    # Do some jiggling of the primary type to determine which set of orbital zones to use

    if primaryType[0] == 'M':  
        if primaryType[-1] in ['7', '8', '9']: a = '9'
        elif primaryType[-1] in ['3', '4', '5', '6']: a = '5'
        elif primaryType[-1] in ['0', '1', '2']: a = '0'
    else:
        if primaryType[-1] in ['5', '6', '7', '8', '9']: a = '5'
        elif primaryType[-1] in ['0', '1', '2', '3', '4']: a = '0'

    thisType = primaryType[0] + a

    # Get the first available orbit from the orbital zone constant
    # A bit clunky, may revisit this to make it more elegant but it will do for now


    if primarySize[0] == 'V':
        orbits = SIZEVZONES.get(thisType)
        firstOrbit = orbits[0]

        if isinstance(returnval, int) and returnval < firstOrbit: returnval = firstOrbit
  

    return returnval

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
    starOrbit = []
    star = {}
    
    starCount = genSystemNature()

    # Determine primary characteristics

    mod = 0

    starType.append(genStarType(mod))
    starSize.append(genStarSize(mod))
    starSpNum.append(genSpectralNumber())
    starOrbit.append('N/A')

    star['Primary'] = starSize[0] 
    
    if starCount >= 2:

        # Determine companion charaxcteristics, using primary rolls as DM as necessary

        starType.append(genStarType(starType[0][1]))
        starSize.append(genStarSize(starSize[0][1]))
        starSpNum.append(genSpectralNumber())
        starOrbit.append(genCompanionOrbit(0, starType[0][0]+str(starSpNum[0]), starSize[0]))

        # Determine tertiary charaxcteristics, using primary rolls as DM as necessary

        if starCount >= 3:

            starType.append(genStarType(starType[0][1]))
            starSize.append(genStarSize(starSize[0][1]))
            starSpNum.append(genSpectralNumber())
            starOrbit.append(genCompanionOrbit(4, starType[0][0]+str(starSpNum[0]), starSize[0]))

    
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
    
    # Put the stellar details into a list

    starList = []
    

    primaryString = starType[0][0] + str(starSpNum[0]) + ' ' + starSize[0][0]
    primaryOrbit = starOrbit[0]
    primaryList = [primaryString, primaryOrbit]
    starList.append(primaryList)
    if starCount >= 2: 
        secondaryString = starType[1][0] + str(starSpNum[1]) + ' ' + starSize[1][0]
        secondaryOrbit = starOrbit[1]
        secondaryList = [secondaryString, secondaryOrbit]
        starList.append(secondaryList)
    if starCount >= 3: 
        tertiaryString = starType[2][0] + str(starSpNum[2]) + ' ' + starSize[2][0]
        tertiaryOrbit = starOrbit[2]
        tertiaryList = [tertiaryString, tertiaryOrbit]
        starList.append(tertiaryList)

    return starList


#####
# Test code here

# i = 0
# while i < 50:
#     a = genStellar()
#   # print(a)
#     i += 1







