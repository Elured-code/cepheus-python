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


# Import modules here

import random

# import TR_Constants
# from TR_Support import D6Roll, D6Rollx2, D100Roll

from . import TR_Constants
from .TR_Support import D6Roll, D6Rollx2, D100Roll

# World class - holds the world details as defined in the CE SRD
#

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
        if starPort in TR_Constants.STARPORTS:
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

# Generate a string representation of the world object
# This will possibly eventually be used instead of the formatUWPString() method, but to avoid breaking things for now
# formatUWPString() will remain and call this method

    def __str__(self):
        
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
        
        returnstr = self.worldname + pad
        returnstr += self.loc + " "
        returnstr += self.starPort
        returnstr += TR_Constants.UWPCODETABLE.get(self.siz)
        returnstr += TR_Constants.UWPCODETABLE.get(self.atm)
        returnstr += TR_Constants.UWPCODETABLE.get(self.hyd)
        returnstr += TR_Constants.UWPCODETABLE.get(self.pop)
        returnstr += TR_Constants.UWPCODETABLE.get(self.gov)
        returnstr += TR_Constants.UWPCODETABLE.get(self.law)
        returnstr += "-" + TR_Constants.UWPCODETABLE.get(self.tlv)
        returnstr = returnstr + " " + self.bCode
        returnstr += " " + self.tCodeString

        # Pad the UWP String with spaces to column 48

        if len(returnstr) <= 48:
            i = 1
            pad = " "
            while i < 49 - len(returnstr):
                pad += " "
                i += 1

        returnstr += pad + self.tZone
         
        # Add the PBG data

        returnstr += " " + str(self.pMod) + str(self.nBelts) + str(self.nGiants)

        return returnstr

# Internal methods to generate stats

    def gen_siz(self):
        x = D6Rollx2() - 2
        self.siz = x

    def gen_atm(self):
        x = D6Rollx2() + self.siz - 7
        if x < 0: x = 0
        elif x > 15: x = 15
        if self.siz == 0: x = 0
        self.atm = x

    def gen_hyd(self):
        x = D6Rollx2() + self.siz - 7

        if self.siz == 0: x = 0
        else:
            if self.atm in [0, 1, 10, 11, 12]: x -= 4
            if self.atm == 14: x -= 2
        if x < 0: x = 0
        self.hyd = x

    def gen_pop(self):
        x = D6Rollx2() - 2
        if self.siz <= 2: x -= 1
        if self.atm in [0, 1, 10, 11, 12]: x -= 2
        if self.atm == 6: x  += 3
        if self.atm in [5, 8]: x += 1
        if self.hyd == 0 and self.atm < 3: x -= 2
        if self.pop < 0: x = 0
        if self.pop > 12: x = 12
        self.pop = x

    def gen_pMod(self):
        x = D6Rollx2() - 2
        if self.pop > 0 and x < 1: x = 1
        if self.pop == 0: x = 0
        if x == 10: x = 9
        self.pMod = x

    def gen_gov(self):
        x = D6Rollx2() - 7 + self.pop
        if self.pop == 0: x = 0
        self.gov = x

    def gen_law(self):
        x = D6Rollx2() - 7 + self.gov
        if self.pop == 0: x = 0
        self.law = x

    def gen_starPort(self):
        spRoll = D6Rollx2() - 7 + self.pop
        self.starPort = TR_Constants.STARPORTSTABLE.get(spRoll)

    def gen_tlv(self):
        x = D6Roll()
        if self.starPort in TR_Constants.STARPORTTLMOD: x += TR_Constants.STARPORTTLMOD.get(self.starPort)
        if self.siz in TR_Constants.SIZETLMOD: x += TR_Constants.SIZETLMOD.get(self.siz)
        if self.hyd in TR_Constants.HYDTLMOD: x += TR_Constants.HYDTLMOD.get(self.hyd)
        if self.atm in TR_Constants.ATMTLMOD: x += TR_Constants.ATMTLMOD.get(self.atm)
        if self.pop in TR_Constants.POPTLMOD: x += TR_Constants.POPTLMOD.get(self.pop)
        if self.gov in TR_Constants.GOVTLMOD: x += TR_Constants.GOVTLMOD.get(self.gov)

        # Add CE world condition requirements

        if self.hyd in [0, 10] and self.pop > 6 and x < 4: x = 4
        if self.atm in [4, 7, 9] and self.tlv < 5: x = 5
        if self.atm in [0, 1, 2, 3, 10, 11, 12] and x < 7: x = 7
        if self.atm in [13, 14] and self.hyd == 10 and x  < 7: x = 7

        # Finally, if population is zero, no TL

        if self.pop == 0: x = 0

        self.tlv = x

    def gen_bCode(self):
                
        # Check for Naval bases

        nBase = False
        if self.starPort == "A" or self.starPort == "B": 
            if D6Rollx2() >= 8: nBase = True
            else: nBase = False

        # Scout bases / outposts

        sBase = False
        if self.starPort != "E" and self.starPort != "X":
            roll = D6Rollx2()
            if self.starPort == "A": roll -= 3
            if self.starPort == "B": roll -= 2
            if self.starPort == "C": roll -= 1
            if roll >= 7: sBase = True
            else: sBase = False

        # Pirate bases

        pBase = False
        if self.starPort != "A" and not nBase:
            if D6Rollx2() == 12: pBase = True

        # Format the base code

        bCode = " "
        if nBase and sBase: bCode = "A"
        if nBase and not sBase: bCode = "N"
        if sBase and pBase: bCode = "G"
        if pBase and not sBase: bCode = "P"
        if sBase and not nBase and not pBase: bCode = "S"

        self.bCode = bCode

    def gen_tCode(self):

        # Generate trade codes

        tCode = []
        tCodeString = ''
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

        for t in tCode:
            tCodeString += t + " "
        tCodeString.rstrip()

        self.tCodeString = tCodeString

    def gen_belts(self):
         
        # Determine the presence of planetoid belts

        if D6Rollx2() >= 4:
            nBelts = D6Roll() - 3
            if self.siz == 0 and nBelts < 1: nBelts = 1
        else: nBelts = 0        

        self.nBelts = nBelts

    def gen_gasgiants(self):

        # Determine the presence of gas giants

        if D6Rollx2() >= 5:
            nGiants = D6Roll() - 2
            if nGiants < 1: nGiants = 1
        else: nGiants = 0
        self.nGiants = nGiants

    def gen_zones(self):
       
        # Determine travel zones

        tZone = " "
        if self.atm >= 10: tZone = "A"
        elif self.gov in [0, 7, 10]: tZone = "A"
        elif self.law == 0 or self.law >= 9: tZone = "A"
        else: tZone = " "
        self.tZone = tZone

    def genWorld(self):
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
        self.gen_starPort()
        self.gen_tlv()

        self.gen_bCode()
        self.gen_tCode()

        self.gen_belts()
        self.gen_gasgiants()
        self.gen_zones()

       
    def formatUWPString_text_SEC(self):
        self.UWPString = self.__str__()

# Print a formatted UWP line for the world/system

    def printUWPString(self):
        print(self.UWPString)


# Test code here

# i = 0
# while i < 10:

#     w1 = World("Blargo")
#     w1.genWorld()
#     w1.formatUWPString_text_SEC()
#     print(w1.UWPString)
#     i += 1
