#
# Cepheus Engine SRD with Extensions Subsector Generation
#
# Version:  0.2
# Author:   Michael Bailey
# Date:     23 July 2020
#

#
# This code generates an 8 x 10 subsector according to:
# 1. CE SRD system generation rules; and
# 2. Stellar data generation kludged together by myself with some quickly researched type/spectra
#    distribution
#

# Constructor:  Subsector(str sName, str SecName, char subLetter, int subDensity)
#   sName:      Subsector name
#   secName:    Host Sector name
#   subLetter:  Subsector position designator
#   subDensity: Subsector stellar density value
#
# Public methods:
# 
#   PrintSubsector:      output the subsector data to the console
#



#
# Things to do:
#
# - Add capability to define 'core', 'settled', 'frontier' and 'wild' worlds with definitions 


import random
import TR_CE_EXT_MTB
from TR_Support import D100Roll
import TR_Constants
import sys

class Subsector:

    # Define properties

    @property
    def subName(self):
        return self.__subName

    @property
    def secName(self):
        return self.__secName

    @property
    def subLetter(self):
        return self.__subLetter

    @property
    def subDensity(self):
        return self.__subDensity

    @property
    def popType(self):
        return self.__popType

    @property
    def subContents(self):
        return self.__subContents

    @property
    def sumPop(self):
        return self.__sumPop

    @property
    def hiTL(self):
        return self.__hiTL

    @property
    def hiPop(self):
        return self.__hiPop

    # Define setters

    @subName.setter
    def subName(self, subName):
        self.__subName = subName

    @secName.setter
    def secName(self, secName):
        self.__secName = secName

    @subLetter.setter
    def subLetter(self, subLetter):
        if subLetter in TR_Constants.SUBSECLETTERS: self.__subLetter = subLetter
        else: self.__subLetter = ' '

    @subDensity.setter
    def subDensity(self, subDensity):
        if subDensity in [1, 2, 3, 4, 5]: self.__subDensity = subDensity
        else: self.__subDensity = 3

    @popType.setter
    def popType(self, popType):
        if popType in [0, 1, 2, 3, 4, 5]: self.__popType = popType
        else: self.__popType = 3

    @subContents.setter
    def subContents(self, subContents):
        self.__subContents = subContents

    @sumPop.setter
    def sumPop(self, sumPop):
        self.__sumPop = sumPop

    @hiTL.setter
    def hiTL(self, hiTL):
        if hiTL < 0: self.__hiTL = 0
        else: self.__hiTL = hiTL

    @hiPop.setter
    def hiPop(self, hiPop):
        if hiPop < 0: self.__hiPop = 0
        else: self.__hiPop = hiPop



    # Initialise the Subsector object

    def __init__(self, subName, secName, subLetter, subDensity, popType):
        self.__subName = subName
        self.__secName = secName
        self.__subLetter = subLetter
        self.__subDensity = subDensity
        self.__popType = popType
        self.contents = []
        self.hiTL = 0
        self.sumPop = 0
        self.hiPop = 0

    # Generate the subsector

    def genSubSec(self):

    # Set the probability of system presence in any given hex

        prob = TR_Constants.DENSITY_LOOKUP.get(self.subDensity)
        
        # Loop through the subsector hexes, checking for and if required generating mainworlds
        i = 1
        while i <= 8:
            j = 1
            while j <= 10:   
                if D100Roll() < prob:
                    loc = format(i, '02d') + format(j, '02d')
                    isMainWorld = True
                    w1 = TR_CE_EXT_MTB.World("Main-" + loc, isMainWorld, self.__popType)
                    w1.loc = loc
                    w1.genWorld()
                    
                    # Add the world to the subsector contents

                    self.contents.append(w1)


                j += 1
            i += 1


    def printSubSec(self):

        # Print the header text

        print(self.subName + " " + "(" + self.secName + "/" + self.subLetter + ")")
        print("....+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8")
        print("")

        for World in self.contents:
            World.formatUWPString_text_SEC()
            print(World.UWPString)

# Testing code here

s1 = Subsector("TestSub", "TestSec", "B", 3, 3)
s1.genSubSec()
s1.printSubSec()