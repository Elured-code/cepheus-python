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
import re
import sys

# Local imports

import TR_CE_SRD_World
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

    def __init__(self, subName, secName, subLetter, subDensity):
        self.__subName = subName
        self.__secName = secName
        self.__subLetter = subLetter
        self.__subDensity = subDensity
        self.contents = []
        self.hiTL = 0
        self.sumPop = 0
        self.hiPop = 0

    # Clear the subsector object

    def clear(self):
        self.contents = []
    
    # Generate the subsector

    def genSubSec(self):
        
        # Loop through the subsector hexes, checking for and if required generating mainworlds
        i = 1
        while i <= 8:
            j = 1
            while j <= 10:

                # Set the probability of system presence in any given hex

                prob = int(TR_Constants.DENSITY_LOOKUP.get(self.subDensity)) 
                  
                if TR_Support.D100Roll() < prob:
                    loc = format(i, '02d') + format(j, '02d')
                                        
                    # Generate the world using the CE SRD engine                   

                    w1 = TR_CE_SRD_World.World("Main-" + loc)
                    w1.loc = loc
                    w1.genWorld(loc)
                    
                    # Add the world to the subsector contents

                    self.contents.append(w1)


                j += 1
            i += 1

    #  Read a subsector from a file

    def readSubSec(self, filename):

        try:
            with open('subsec.uwp', 'r') as f:

                # Get first line and parse the subsector name, letter and parent sector name

                line = f.readline()
                # print(line)

                # Set some defaults

                xsubsecname = 'Placeholder'
                xsubsecletter = 'A'
                xsectorname = 'Placeholder'

                m0 = re.match(r"(.*)\(", line)
                m1 = re.match(r".*\((.*)\/", line)
                m2 = re.match(r".*\/(.*)\)", line)
                if m0: xsubsecname = m0.group(1)
                if m1: xsectorname = m1.group(1)
                if m2: xsubsecletter = m2.group(1)

                # print('### ' + xsectorname)

                # Add the subsector details to the subsector object

                self.subName = xsubsecname
                self.subLetter = xsubsecletter
                self.secName = xsectorname

                # Read and ignore the header

                while not line.startswith("....+....1"):
                    line = f.readline()
                    # print(line, end='')

                # Ok, now read in the remaining lines and parse to populate the subsector object

                lines = f.readlines()

                for line in lines:
                    # print(line, end='')

                    # World name is in columns 1 - 12, strip any trailing spaces
                    # I haven't assigned directly to world object fields to enable future error checking

                    # Note, wrap some import checking and substitution of invalid values at some point

                    worldname = line[0:12].rstrip()
                    loc       = line[13:17]
                    starPort  = line[18:19].upper()
                    siz       = line[19:20]
                    atm       = line[20:21]
                    hyd       = line[21:22]
                    pop       = line[22:23]
                    gov       = line[23:24]
                    law       = line[24:25]
                    tlv       = line[26:27]
                    bCode     = line[28:29]
                    tCodeString     = line[30:47]
                    tZone     = line[48:49]
                    pMod      = int(line[51:52])
                    nBelts    = int(line[52:53])
                    nGiants   = int(line[53:54])

                    # Create an inverted dictionary to enable reverse lookups on the UWP int --> char dictionary
                    # This dictionary (TR_Constants.UWPCODETABLE) is a 1:1 so we can do this

                    ivd = {v: k for k, v in TR_Constants.UWPCODETABLE.items()}

                    # Now create a world object to hold the data and assign the values read above

                    w1 = TR_CE_SRD_World.World(worldname)
                    w1.loc = loc
                    w1.starPort = starPort
                    w1.siz = ivd[siz]
                    w1.atm = ivd[atm]
                    w1.hyd = ivd[hyd]
                    w1.pop = ivd[pop]
                    w1.gov = ivd[gov]
                    w1.law = ivd[law]
                    w1.tlv = ivd[tlv]
                    w1.bCode = bCode
                    w1.tCodeString = tCodeString
                    w1.tZone = tZone
                    w1.pMod = int(pMod)
                    w1.nBelts = int(nBelts)
                    w1.nGiants = int(nGiants)

                # Now that we have all the fields, add the world object to the subsector

                    self.contents.append(w1)

                    # print(xworldname + ' ' + xlocation + ' ' + xstarport + '#')
               
        except IOError as error: 
            print('Unable to open input UWP file')
            print(error)
            sys.exit(8)
    
    # TO DO:  Read a subsector from JSON
    
    #  Print a subsector to stdout

    def printSubSec(self):

        # Print the header text

        print(self.subName + " " + "(" + self.secName + "/" + self.subLetter + ")")
        print(TR_Constants.FIXEDHEADER)

        for World in self.contents:
            World.formatUWPString_text_SEC()
            print(World.UWPString)
    
    # Write a subsector to a variable

    def writeSubSec(self):
        returnval = ''
        returnval += self.subName + " " + "(" + self.secName + "/" + self.subLetter + ")" + '\n'
        returnval += TR_Constants.FIXEDHEADER + '\n'
    
        for World in self.contents:
            World.formatUWPString_text_SEC()
            returnval += World.UWPString
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
            if World.worldname not in ['Brown Dwarf', 'Rogue Planet', 'Neutron Star', 'Black Hole',
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
                worldjson['System Type'] = World.worldname
            
            
            subsecjson[World.loc] = worldjson

        outjson = json.dumps(subsecjson, indent=4)
        return outjson


# # Testing code here

s1 = Subsector("TestSub", "TestSec", "B", 3)
s1.readSubSec('subsec.uwp')

# # print(s1.pType)
# s1.genSubSec()
# print("```")
s1.printSubSec()
# print("```")