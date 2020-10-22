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
#   engName:    Generation engine name - currently CE (CE SRD) or CEEX (CE Extended)
#   sName:      Subsector name
#   secName:    Host Sector name
#   subLetter:  Subsector position designator
#   subDensity: Subsector stellar density value
#
# Public methods:
# 
#   PrintSubsector:      output the subsector data to the console
#

# Python imports

import json
import random
import sys

# Local imports

import TR_CE_Extended
import TR_Support
import TR_Constants


# Define local constants

ENGINES = ['CT', 'CE', 'CEEX']
# DENSITY_LOOKUP = {1: 4, 2: 18, 3: 33, 4: 50, 5: 66}
SUBSECLETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']


# Define common functions



class Subsector:

    # Define properties

    @property
    def engName(self):
        return self.__engName

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
    def allowUnusual(self):
        return self.__allowUnusual

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

    @engName.setter
    def engName(self, engName):
        if engName in ENGINES: self.__engName = engName
        else: self.engName = 'CE'
    
    @subName.setter
    def subName(self, subName):
        self.__subName = subName

    @secName.setter
    def secName(self, secName):
        self.__secName = secName

    @subLetter.setter
    def subLetter(self, subLetter):
        if subLetter in SUBSECLETTERS: self.__subLetter = subLetter
        else: self.__subLetter = ' '

    @subDensity.setter
    def subDensity(self, subDensity):
        if subDensity in [1, 2, 3, 4, 5]: self.__subDensity = subDensity
        else: self.__subDensity = 3

    @allowUnusual.setter
    def allowUnusual(self, allowUnusual):
        if allowUnusual in [True, False]: self.__allowUnusual - allowUnusual
        else: allowUnusual = False

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

    def __init__(self, subName, secName, subLetter, subDensity, allowUnusual):
        self.__subName = subName
        self.__secName = secName
        self.__subLetter = subLetter
        self.__subDensity = subDensity
        self.__allowUnusual = allowUnusual
        self.contents = []
        self.hiTL = 0
        self.sumPop = 0
        self.hiPop = 0

    # Clear the subsector object

    def clear(self):
        self.contents = []
    
    # Generate the subsector

    def genSubSecExtended(self):


        
        # Loop through the subsector hexes, checking for and if required generating mainworlds
        i = 1
        while i <= 8:
            j = 1
            while j <= 10:

                # Probability of system presence is now handled in TR_CE_Extended in order to allow for non-stellar system objects

                loc = format(i, '02d') + format(j, '02d')
                 
                # Generate the world using the CE SRD engine                   

                w1 = TR_CE_Extended.System()
                w1.loc = loc
                wnameplaceholder = self.subName + ' ' + loc
                w1.gen_System(loc, self.subDensity, self.allowUnusual, wnameplaceholder)  
              
                # Add any contents generated to the subsector contents list

                if w1.sysType != 'Empty':
                    self.contents.append(w1)


                j += 1
            i += 1

    # Print a subsector to stdout

    def printSubSec(self):

        # Print the header text

        print(self.subName + " " + "(" + self.secName + "/" + self.subLetter + ")")
        print(TR_Constants.FIXEDHEADER)

        for s in self.contents:
            if s.sysType != 'Empty': print(s.sysUWPString)


    # Write a subsector to a variable

    def writeSubSec(self):
        returnval = ''
        returnval += self.subName + " " + "(" + self.secName + "/" + self.subLetter + ")" + '\n'
        returnval += TR_Constants.FIXEDHEADER + '\n'
    
        for s in self.contents:
            if s.sysType != 'Empty': returnval += s.sysUWPString
            returnval += '\n'

        return returnval

        # Write the subsector to a JSON documment

    def writeSubSecJSON(self):
        subsecjson = {}
        subsecjson['Name'] = self.subName
        subsecjson['Position'] = self.subLetter
        
        for World in self.contents:
            worldjson = {}
            World.formatUWPString_text_SEC()
            if World.sysType not in ['Brown Dwarf', 'Rogue Planet', 'Neutron Star', 'Black Hole',
                'Stellar Nursery', 'Nebula']:
                worldjson['System Type'] = 'Star System'
                worldjson['Name'] = World.worldname
                worldjson['UWP'] = World.UWPString
                worldjson['Starport'] = World.starPort
                worldjson['Size'] = World.siz
                worldjson['Atmosphere'] = World.atm
                worldjson['Hydrographics'] = World.hyd
                worldjson['Population'] = World.pop
                worldjson['Goverment'] = World.gov
                worldjson['Law Level'] = World.law
                worldjson['Tech Level'] = World.tlv
                worldjson['Bases'] = World.bCode                
                worldjson['Trade Codes'] = World.tCodeString.rstrip()
                worldjson['Population Modifier'] = World.pMod
                worldjson['Planetoid Belts'] = World.nBelts
                worldjson['Gas Giants'] = World.nGiants

            else:
                worldjson['System Type'] = World.sysType
            
            
            subsecjson[World.loc] = worldjson

        outjson = json.dumps(subsecjson, indent=4)
        return outjson


# # Testing code here

s1 = Subsector("TestSub", "TestSec", "B", 3, False)

# print(s1.pType)
s1.genSubSecExtended()
print("```")
s1.printSubSec()
print("```")