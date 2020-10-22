#
# Cepheus Engine SRD World Generation with extensions
#
# Inherits TR_CE_SRD_World
# 
# Extensions:
# 1. Stellar data generation kludged together by myself with some quickly researched type/spectra
#    distribution
#
# Author:   Michael Bailey
# Date:     13 August 2020
#

# Constructor:  World(str wName, boolean isMainWorld, int popType)
#
# Public methods:
# 
# PrintUWPString:      output the world data as a single line of text
#

#
# Things to do:
#
# - Move supporting functions to a separate module
# 
#  


# Import modules here

import random
from . import TR_Constants, TR_CE_SRD_World

from .TR_CE_EXT_Stellar import gen_Spectral, gen_starType
from .TR_Support import D6Roll, D6Rollx2, D100Roll

# Module specific functions


class World(TR_CE_SRD_World.World):

# Define properties

    @property
    def mainWorld(self):
        return self.__mainWorld

    @property
    def popType(self):
        return self.__popType

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

    @mainWorld.setter
    def mainWorld(self, mainWorld):
        self.__mainWorld = mainWorld
    
    @nStars.setter
    def nStars(self, nStars):
        if nStars < 1: self.__nStars = 1

        # Note, limiting members to 3 for now

        elif nStars > 3: self.__nStars = 3
        else: self.__nStars = nStars

    @popType.setter
    def popType(self, popType):
        # print("++" + str(popType))
        self.__popType = popType
    
    @starList.setter
    def starList(self, starList):
        self.__starList = starList

    @spectraList.setter
    def spectraList(self, spectraList):
        self.__spectraList = spectraList


# Initialise the world class        

    def __init__(self, wName, isMainWorld, popType):
        super().__init__(wName)
        
        # Initialise variables

        self.mainWorld = isMainWorld
        self.popType = popType
        self.nStars = 1
        self.starList = []

# Provide a string representation of the object

    def __str__(self):
        returnstr = super().__str__()

        # Add stellar data

        stellarString = ""
        for star in self.starList:
            stellarString += star + " "
        stellarString.rstrip()

        returnstr += " " + stellarString

        return returnstr 
        
    # Determine the number of stars in the system

    def gen_nStars(self):
        i = D100Roll()

        if i <= 56: self.nStars = 1
        elif i <= 91: self.nStars = 2
        else: self.nStars = 3

 
    def gen_atm(self, T):

        # First we call the parent generator before adding additional calculations

        super().gen_atm()

        # Burn the atmosphere off worlds with dwarf primaries

        if T == 'D':
            i = D6Rollx2()
            if i == 12: self.atm = 14
            elif i == 11: self.atm = 3
            elif i == 10: self.atm = 2
            elif i == 9: self.atm = 1
            else: self.atm = 0 

        if self.siz == 0: self.atm = 0

    def gen_pop(self, T, S):

        # First we call the parent generator before adding additional calculations
        
        super().gen_pop()

        # Skew the population away from smaller (flares) and giant primaries

        if T[0] == 'I' or T == 'II':
            self.pop -= 3
        elif T[0] == 'III':
            self.pop -= 2
        elif T[0] == 'V':
            if S[0] == 'M': self.pop -= 2
            elif S[0] == 'K':  self.pop -= 1
        elif T[0] == 'VI':
            self.pop -= 2 
        elif T[0] == 'D':
            self.pop -= 4

        # CE SRD standard population modifiers
        # Note this is repeated in the parent class, look at abstracting it to avoid this

        if self.siz <= 2: self.pop -= 1
        if self.atm in [0, 1, 10, 11, 12]: self.pop -= 2
        if self.atm == 6: self.pop  += 3
        if self.atm in [5, 8]: self.pop += 1
        if self.hyd == 0 and self.atm < 3: self.pop -= 2

        # Some additional population modifiers based on settlement type
        # I may move to make these more editable via lists/tuples later

        if self.popType == 0:

            # Empty, no population at all (including no indigenous sapients)

            self.pop = 0

        elif self.popType == 1:

            # Wilds, greatly reduce population for the less hospitable worlds
            # as well as reducing population for the better ones

            if self.atm in [5, 6, 8] and self.hyd >= 4: self.pop -= 2
            else: self.pop -= 4

        elif self.popType == 2:

            # Frontier worlds, reduce population for the less hospitable worlds
            # and slightly for the better ones

            if self.atm in [5, 6, 8] and self.hyd >= 4: self.pop -= 1
            else: self.pop -= 3

        # No changes for standard worlds

        elif self.popType == 4:

            # Highly settled worlds, bump population 

            if self.atm in [5, 6, 8]:
                if self.hyd >= 4: self.pop += 2
                elif self.hyd >= 2: self.pop += 1
            elif self.atm in [4, 7, 9, 13, 14]: self.pop += 1

        # Very highly settled worlds, higher increases as appropriate

        elif self.popType == 5:
            if self.atm in [5, 6, 8]:
                if self.hyd >= 4: 
                    if D6Rollx2() > 5: self.pop += 4
                    else: self.pop += 3
                elif self.hyd <= 2: self.pop += 3
            elif self.atm in [4, 7, 9, 13, 14]: self.pop += 3
            else: self.pop += 1

        # Bounds on the population
        
        if self.pop < 0: self.pop = 0
        if self.pop > 10: self.pop = 10   

    def gen_pMod(self):    
        self.pMod = D6Rollx2() - 2
        if self.pop > 0 and self.pMod < 1: self.pMod = 1
        if self.pop == 0: self.pMod = 0
        if self.pMod == 10: self.pMod = 9

    #####
    
    def genWorld(self):
        
        # Generate the world, using the component generators defined above
        # If a mainworld, generate stellar data

        if self.mainWorld: 
            self.gen_nStars()

            # Determine the primary type
            
            tP = gen_starType('x')
        
            # Determine the primary spectral classification
            
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

        # Generate world data
    
        # Generate physical stats

        self.gen_siz()
        self.gen_atm(tP)
        self.gen_hyd()
         
        # Generate social stats

        self.gen_pop(tP, sP)
        self.gen_pMod()
        self.gen_gov()
        self.gen_law()

        # Generate the starport

        self.gen_starPort()

        # Generate Tech Level

        self.gen_tlv()

        # Determine presence of bases

        self.gen_bCode()

        # Generate trade codes

        self.gen_tCode()

        # Determine the presence of planetoid belts, gas giants

        self.gen_belts()
        self.gen_gasgiants()
   
        # Determine travel zones

        self.gen_zones()
     
    def formatUWPString_text_SEC(self):
        self.UWPString = self.__str__()

#####
# Test code here


# i = 1
# while i < 10:
#     w1 = World("Blargo", True, 5)
#     w1.genWorld()
#     w1.formatUWPString_text_SEC()
#     w1.printUWPString()
#     i += 1





