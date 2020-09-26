#
# Cepheus Engine SRD World Generation with extensions from Classic Traveller Book 6
# 
# This class inherits the TR_CE_SRD_World class
#
# Extensions:
# 1. CT Book 6 Extended System Generation
#
# Author:   Michael Bailey
# Date:     13 August 2020
#

# Constructor:  World(str wName)
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
import TR_Constants
import TR_CE_SRD_World
import TR_CE_Book6_Stellar
from TR_Support import D6Roll, D6Rollx2, D100Roll

# Module specific functions


class World(TR_CE_SRD_World.World):

# Define properties

 
    @property
    def starList(self):
        return self.__starList

    @property
    def spectraList(self):
        return self.__spectraList

    @property
    def mainWorld(self):
        return self.__mainWorld
   
    @starList.setter
    def starList(self, starList):
        self.__starList = starList

    @spectraList.setter
    def spectraList(self, spectraList):
        self.__spectraList = spectraList

    @mainWorld.setter
    def mainWorld(self, mainWorld):
        self.__mainWorld = mainWorld

# Initialise the world class        

    def __init__(self, wName, isMainWorld):
        super().__init__(wName)
        
        # Initialise additional variables

        self.mainWorld = True
        self.nStars = 1
        self.starList = []

# Provide a string representation of the object

    def __str__(self):
        returnstr = super().__str__() + ' '

        # There's a lot of fun going on here with nested lists.  To break it down:
        #   starList[0][0] = primary string
        #   starList[0][1] = primary orbit (N/A)
        #   starList[1][0] = secondary string
        #   starList[1][1] = secondary orbit
        #   and so on
         
        i = 1
        while i <= len(self.starList):
            returnstr += self.starList[i - 1][0] + ' '
            i += 1

        returnstr.rstrip()
        return returnstr


    def genBelts(self):
        # Determine the presence of belts
        
        if D6Rollx2() >= 4:
            self.nBelts = D6Roll() - 3
            if self.siz == 0 and self.nBelts < 1: self.nBelts = 1
        else: self.nBelts = 0 

    def genGiants(self):
        # Determine the presence of gas giants

        if D6Rollx2() >= 5:
            self.nGiants = D6Roll() - 2
            if self.nGiants < 1: self.nGiants = 1
        else: self.nGiants = 0

    def genZone(self):
        self.tZone = " "
        if self.atm >= 10: self.tZone = "A"
        elif self.gov in [0, 7, 10]: self.tZone = "A"
        elif self.law == 0 or self.law >= 9: self.tZone = "A"
        else: self.tZone = " "


    #####
    
    def genWorld(self):
        
        # Generate the world, using the component generators defined above
        # If a mainworld, generate stellar data

        if self.mainWorld: 

        # Determine the system type (single, binary or trinary)

            self.nStars = TR_CE_Book6_Stellar.genSystemNature()

        # Generate the star(s)

            self.starList = TR_CE_Book6_Stellar.genStellar()

        # Generate world data
    
        # Generate physical stats

        self.gen_siz()
        self.gen_atm()
        self.gen_hyd()
         
        # Generate social stats

        self.gen_pop()
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

        self.genBelts()
        self.genGiants()
   
        # Determine travel zones

        self.genZone()
       
    def formatUWPString_text_SEC(self):
        self.UWPString = self.__str__()

####
# Test code here


# i = 1
# while i < 10:
#     w1 = World("Blargo", True)
#     w1.genWorld()
#     w1.formatUWPString_text_SEC()
#     w1.printUWPString()
#     i += 1





