#
# Cepheus Engine SRD with Extensions Sector Generation
#
# Author:   Michael Bailey
# Date:     23 October 2020
#

#
# This code generates an 32 x 40 sector according to:
# 1. CE SRD system generation rules; and
# 2. Stellar data generation using data provided by Ade Stewart
#

# Constructor:  Sector(str sName, str SecName, string subDensity)
#   sName:      Subsector name
#   subDensity: Subsector stellar density value string (16 x number 0 - 6)
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

ISTART = [1, 9, 17, 25, 1, 9, 17, 25, 1, 9, 17, 25, 1, 9, 17, 25]
JSTART = [1, 1, 1, 1, 11, 11, 11, 11, 21, 21, 21, 21, 31, 31, 31, 31]

# Define common functions



class Subsector:

    # Define properties

    @property
    def engName(self):
        return self.__engName

    @property
    def secName(self):
        return self.__secName

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
    
    @secName.setter
    def secName(self, secName):
        self.__secName = secName


    @subDensity.setter
    def subDensity(self, subDensity):
        self.__subDensity = subDensity

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

    # Initialise the Sector object

    def __init__(self, subName, secName, subLetter, subDensity, allowUnusual):
        self.__secName = secName
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


        subsec = 1
        while subsec <= 16:
            a = 1
            
            # Loop through the subsector hexes, checking for and if required generating mainworlds

            while a <= 8:
                b = 1
                while b <= 10:

                    # Get the subsector letter

                    try:
                        subsecletter = TR_Constants.SUBSECLETTERS[subsec - 1]
                    except IndexError:
                        print("Invalid subsector number - cannot assign letter designation")
                        sys.exit()

                    # Calculate the location string

                    iloc = ISTART[subsec - 1] + a - 1
                    jloc = JSTART[subsec - 1] + b - 1
                    loc = format(iloc, '02d') + format(jloc, '02d')
                    
                    # Generate the world using the CE SRD engine 
                    # Probability of system presence is now handled in TR_CE_Extended in order to allow for non-stellar system objects                  

                    w1 = TR_CE_Extended.System()
                    w1.loc = loc
                    # wnameplaceholder = self.secName + ':' + loc
                    wnameplaceholder = ""
                    w1.gen_System(loc, self.subDensity, self.allowUnusual, wnameplaceholder)  

                    # Get the specific subsector density from the string
                
                    # Add any contents generated to the subsector contents list

                    if w1.sysType != 'Empty':
                        self.contents.append(w1)

                    # print(str(i) + ' ' + str(j) + ' ' + loc + '(subsector ' + subsecletter + ')')

                    b += 1
                a += 1
            subsec += 1

    # Print a subsector to stdout

    def printSubSec(self):

        # Print the header text

        print(self.secName)
        print(TR_Constants.FIXEDHEADER)

        for s in self.contents:
            if s.sysType != 'Empty': print(s.sysUWPString)

    def printTRMapSec(self):

        # Print the header text

        print(self.secName)
        print(TR_Constants.FIXEDHEADER)

        for s in self.contents:
            if s.sysType in ['Star System']: 
                print(s.sysUWPString)



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
s1.printTRMapSec()
print("```")