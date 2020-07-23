#
# Cepheus Engine SRD World Generation
#
# Version:  0.2
# Author:   Michael Bailey
# Date:     23 July 2020
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
#  - Add stellar generation method based on Book 6 / MT
# 


# Import modules here

import random

# Define common functions

# Dice rollers

def D2Roll():
    random.seed()
    return random.randint(1, 6) + random.randint(1, 6)

def D1Roll():
    random.seed()
    return random.randint(1, 6)

# Define constants

# Decimal to Traveller Hex Code translation
# Note that in non-Book 3 implementations this is extended out, skipping "I" and "O"

STARPORTS = ["A", "B", "C", "D", "E", "X"]
UWPCODETABLE = {0: "0", 1: "1", 2: "2",
    3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "J", 19: "K", 20: "L", 21: "M" }

# starPort code determination

STARPORTSTABLE = {-5: "X", -4: "X", -3: "X", -2: "X", -1: "X", 0: "X", 1: "X", 2: "X",
    3: "E", 4: "E", 5: "D", 6: "D", 7: "C", 8: "C", 9: "B", 10: "B", 11: "A", 12: "A", 13: "A", 14: "A", 15: "A", 16: "A", 17: "A", 18: "A" }

# Tech level modifiers

STARPORTTLMOD = {"A": 6, "B": 4, "C": 2, "X": -4} 
SIZETLMOD = {0: 2, 1: 2, 2: 1, 3: 1, 4: 1}     
HYDTLMOD = {0: 1, 9: 1, 10: 2}
ATMTLMOD = {0: 1, 1: 1, 2: 1, 3: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1}
POPTLMOD = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 9: 2, 10: 4, 11: 3, 12: 4}
GOVTLMOD = {0: 1, 5: 1, 7: 2, 13: -2, 14: -2}

class World:

# Define properties

    @property
    def worldname(self):
        return self.__worldname

    @property
    def starPort(self):
        return self.__starPort

    @property
    def siz(self):
        return self.__siz

    @property
    def atm(self):
        return self.__atm

    @property
    def hyd(self):
        return self.__hyd

    @property
    def pop(self):
        return self.__pop

    @property
    def gov(self):
        return self.__gov

    @property
    def law(self):
        return self.__law

    @property
    def tlv(self):
        return self.__tlv

    @property
    def bCode(self):
        return self.__bCode

    @property
    def pMod(self):
        return self.__pMod

    @property
    def nBelts(self):
        return self.__nBelts

    @property
    def nGiants(self):
        return self.__nGiants

    @property
    def tCodeString(self):
        return self.__tCodeString

    @property
    def tZone(self):
        return self.__tZone

    @property
    def loc(self):
        return self.__loc

# Define setters, including checks

    @worldname.setter
    def worldname(self, worldname):
        if len(worldname) > 13:
            self.__worldname = worldname[0:13]
        self.__worldname = worldname

    @starPort.setter
    def starPort(self, starPort):
        if starPort in STARPORTS:
            self.__starPort = starPort
        else: self.__starPort = "-"

    @siz.setter
    def siz(self, siz):
        if siz < 0: self.__siz = 0
        elif siz > 10: self.__siz = 10
        else: self.__siz = siz

    @atm.setter
    def atm(self, atm):
        if atm < 0: self.__atm = 0
        elif atm > 15: self.__atm = 15
        else: self.__atm = atm

    @hyd.setter
    def hyd(self, hyd):
        if hyd < 0: self.__hyd = 0
        elif hyd > 10: self.__hyd = 10
        else: self.__hyd = hyd

    @pop.setter
    def pop(self, pop):
        if pop < 0: self.__pop = 0
        elif pop > 10: self.__pop = 10
        else: self.__pop = pop

    @gov.setter
    def gov(self, gov):
        if gov < 0: self.__gov = 0
        elif gov > 15: self.__gov = 15
        else: self.__gov = gov

    @law.setter
    def law(self, law):
        if law < 0: self.__law = 0
        elif law > 15: self.__law = 15
        else: self.__law = law

    @tlv.setter
    def tlv(self, tlv):
        if tlv < 0: self.__tlv = 0
        else: self.__tlv = tlv

    @bCode.setter
    def bCode(self, bCode):
        if len(bCode) > 1: self.__bCode = bCode[0:1]
        else: self.__bCode = bCode

    @pMod.setter
    def pMod(self, pMod):
        if pMod < 1: self.__pMod = 1
        elif pMod > 9: self.__pMod = 9
        else: self.__pMod = pMod

    @nBelts.setter
    def nBelts(self, nBelts):
        if nBelts < 0: self.__nBelts = 0
        elif nBelts > 9: self.__nBelts = 9
        else: self.__nBelts = nBelts

    @nGiants.setter
    def nGiants(self, nGiants):
        if nGiants < 0: self.__nGiants = 0
        elif nGiants > 9: self.__nGiants = 9
        else: self.__nGiants = nGiants

    @tCodeString.setter
    def tCodeString(self, tCodeString):
        self.__tCodeString = tCodeString

    @tZone.setter
    def tZone(self, tZone):
        self.__tZone = tZone

    @loc.setter
    def loc(self, loc):

        self.__loc = loc

# Initialise the world class        

    def __init__(self, wName):
        
        # Initialise variables

        self.UWPString = ""
        self.worldname = wName
        self.loc = "0000"
        self.starPort = "-"
        self.siz = 0
        self.atm = 0
        self.hyd = 0
        self.pop = 0
        self.gov = 0
        self.law = 0
        self.tlv = 0
        self.bCode = " "
        self.pMod = 0
        self.nBelts = 1
        self.nGiants = 0
        self.tCodeString = ""
        self.tZone = " "
        

    def genWorld(self):
        # Generate world data
    
        # Generate physical stats

        self.siz = D2Roll() - 2
        
        self.atm = D2Roll() - 7 + self.siz
        if self.atm < 0: self.atm = 0
        elif self.atm > 15: self.atm = 15
        if self.siz == 0: self.atm = 0
        
        if self.siz == 0: self.hyd = 0
        else:
            self.hyd = D2Roll() - 7 + self.siz
            if self.atm in [0, 1, 10, 11, 12]: self.hyd -= 4
            if self.atm == 14: self.hyd -= 2
            if self.hyd < 0: self.hyd = 0
        
        # Generate social stats

        self.pop = D2Roll() - 2
        if self.siz <= 2: self.pop -= 1
        if self.atm in [0, 1, 10, 11, 12]: self.pop -= 2
        if self.atm == 6: self.pop  += 3
        if self.atm in [5, 8]: self.pop += 1
        if self.hyd == 0 and self.atm < 3: self.pop -= 2
        if self.pop < 0: self.pop = 0
        if self.pop > 12: self.pop = 12
        
        self.pMod = D2Roll() - 2
        if self.pop > 0 and self.pMod < 1: self.pMod = 1
        if self.pop == 0: self.pMod = 0
        if self.pMod == 10: self.pMod = 9

        self.gov = D2Roll() - 7 + self.pop
        if self.gov < 0: self.gov = 0
        if self.gov > 15: self.gov = 15
        if self.pop  == 0: self.gov   = 0
     
        self.law = D2Roll() - 7 + self.gov
        if self.law < 0: self.law = 0
        elif self.law > 15: self.law = 15
        if self.pop == 0: self.law  = 0
        

        # Generate the starport

        spRoll = D2Roll() - 7 + self.pop
        self.starPort = STARPORTSTABLE.get(spRoll)
        self.UWPString = self.starPort + self.UWPString

        # Generate Tech Level

        self.tlv = D1Roll()
        if self.starPort in STARPORTTLMOD: self.tlv += STARPORTTLMOD.get(self.starPort)
        if self.siz in SIZETLMOD: self.tlv += SIZETLMOD.get(self.siz)
        if self.hyd in HYDTLMOD: self.tlv += HYDTLMOD.get(self.hyd)
        if self.atm in ATMTLMOD: self.tlv += ATMTLMOD.get(self.atm)
        if self.pop in POPTLMOD: self.tlv += POPTLMOD.get(self.pop)
        if self.gov in GOVTLMOD: self.tlv += GOVTLMOD.get(self.gov)

        if self.tlv < 0: self.tlv = 0
        elif self.tlv > 15: self.tlv = 15


        # Add CE world condition requirements

        if self.hyd in [0, 10] and self.pop > 6 and self.tlv < 4: self.tlv = 4
        if self.atm in [4, 7, 9] and self.tlv < 5: self.tlv = 5
        if self.atm in [0, 1, 2, 3, 10, 11, 12] and self.tlv < 7: self.tlv = 7
        if self.atm in [13, 14] and self.hyd == 10 and self.tlv  < 7: self.tlv = 7

        # Finally, if population is zero, no TL

        if self.pop == 0: self.tlv = 0

        # Determine presence of bases

        # Naval bases

        nBase = False
        if self.starPort == "A" or self.starPort == "B": 
            if D2Roll() >= 8: nBase = True
            else: nBase = False

        # Scout bases / outposts

        sBase = False
        if self.starPort != "E" and self.starPort != "X":
            roll = D2Roll()
            if self.starPort == "A": roll -= 3
            if self.starPort == "B": roll -= 2
            if self.starPort == "C": roll -= 1
            if roll >= 7: sBase = True
            else: sBase = False

        # Pirate bases

        pBase = False
        if self.starPort != "A" and not nBase:
            if D2Roll() == 12: pBase = True

        # Format the base code

        self.bCode = " "
        if nBase and sBase: self.bCode = "A"
        if nBase and not sBase: self.bCode = "N"
        if sBase and pBase: self.bCode = "G"
        if pBase and not sBase: self.bCode = "P"
        if sBase and not nBase and not pBase: self.bCode = "S"

        # Generate trade codes

        tCode = []
        if self.atm >= 4 and self.atm <= 9 and self.hyd >= 4 and self.hyd <= 8 and self.pop >= 5 and self.pop <= 7: tCode.append("Ag")
        if self.siz == 0 and self.atm == 0 and self.hyd == 0: tCode.append("As")
        if self.pop == 0 and  self.gov  == 0 and self.law == 0: tCode.append("Ba") 
        if self.atm >= 2 and self.hyd == 0: tCode.append("De")
        if self.atm >= 10 and self.hyd >= 1: tCode.append("Fl")
        if self.atm in [5, 6, 8] and self.hyd >= 4 and self.hyd <= 9 and self.pop >= 4 and self.pop <= 8: tCode.append("Ga")
        if self.pop >= 9: tCode.append("Hi")
        if self.tlv >= 12: tCode.append("Ht")
        if self.atm in [0, 1] and self.hyd >= 1: tCode.append("Ic")
        if self.atm in [0, 1, 2, 4, 7, 9] and self.pop >= 9: tCode.append("In")
        if self.pop >= 1 and self.pop <= 3: tCode.append("Lo")
        if self.tlv <= 5: tCode.append("Lt")
        if self.atm <= 3 and self.hyd <= 3 and self.pop >= 6: tCode.append("Na")
        if self.pop >= 4 and self.pop <= 6: tCode.append("Ni")
        if self.atm >= 2 and self.atm <= 5 and self.hyd <= 3: tCode.append("Po")
        if self.atm in [6, 8] and self.pop >= 6 and self.pop <= 8: tCode.append("Ri")
        if self.hyd == 10: tCode.append("Wa")
        if self.atm == 0: tCode.append("Va")

        # Format the trade code string

        # print(tCode)

        for t in tCode:
            self.tCodeString += t + " "
        self.tCodeString.rstrip()

        # Determine the presence of planetoid belts

        if D2Roll() >= 4:
            self.nBelts = D1Roll() - 3
            if self.siz == 0 and self.nBelts < 1: self.nBelts = 1
        else: self.nBelts = 0 

        # Determine the presence of gas giants

        if D2Roll() >= 5:
            self.nGiants = D1Roll() - 2
            if self.nGiants < 1: self.nGiants = 1
        else: self.nGiants = 0
       
        # Determine travel zones

        self.tZone = " "
        if self.atm >= 10: self.tZone = "A"
        elif self.gov in [0, 7, 10]: self.tZone = "A"
        elif self.law == 0 or self.law >= 9: self.tZone = "A"
        else: self.tZone = " "

        # Capitalise the world name if it is a high population world

        if self.pop >= 9: self.worldname = self.worldname.upper()

        # Build the UWP String from the values generated above

        # Pad the world name with strings to column 13
        
        if len(self.worldname) <= 13:
           i = 1
           pad = " "
           while i < 14 - len(self.worldname):
               pad += " "
               i += 1
        
        self.UWPString = self.worldname + pad
        self.UWPString += self.loc + " "
        self.UWPString += self.starPort
        self.UWPString += UWPCODETABLE.get(self.siz)
        self.UWPString += UWPCODETABLE.get(self.atm)
        self.UWPString += UWPCODETABLE.get(self.hyd)
        self.UWPString += UWPCODETABLE.get(self.pop)
        self.UWPString += UWPCODETABLE.get(self.gov)
        self.UWPString += UWPCODETABLE.get(self.law)
        self.UWPString += "-" + UWPCODETABLE.get(self.tlv)
        self.UWPString = self.UWPString + " " + self.bCode
        self.UWPString += " " + self.tCodeString


        # Pad the UWP String with spaces to column 48

        if len(self.UWPString) <= 48:
            i = 1
            pad = " "
            while i < 49 - len(self.UWPString):
                pad += " "
                i += 1

        self.UWPString += pad + self.tZone
         
        # Add the PBG data

        self.UWPString += " " + str(self.pMod) + str(self.nBelts) + str(self.nGiants)


        




# Print a formatted UWP line for the world/system

    def printUWPString(self):
        print(self.UWPString)

# w1 = World("Blargo")
# print(w1.UWPString)





