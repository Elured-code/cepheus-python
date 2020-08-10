#
# Cepheus Engine SRD World Generation with extensions
# 
# Extensions:
# 1. Stellar data generation kludged together by myself with some quickly researched type/spectra
#    distribution
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
# - Move supporting functions to a separate module
# 
#  


# Import modules here

import random
import TR_Constants
from TR_CE_EXT_Stellar import gen_Spectral, gen_starType
from TR_Support import D6Roll, D6Rollx2, D100Roll

# Module specific functions


class World:

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
        self.__pop = pop

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
        self.__pMod = pMod

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

    def __init__(self, wName, isMainWorld, popType):
        
        # Initialise variables

        self.mainWorld = isMainWorld
        self.popType = popType
        self.nStars = 1
        self.starList = []
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
        
    # Determine the number of stars in the system

    def gen_nStars(self):
        i = D100Roll()

        if i <= 56: self.nStars = 1
        elif i <= 91: self.nStars = 2
        else: self.nStars = 3

    def gen_siz(self):
        self.siz = D6Rollx2() - 2

    def gen_atm(self, T):
        self.atm = D6Rollx2() - 7 + self.siz
        if self.atm < 0: self.atm = 0
        elif self.atm > 15: self.atm = 15

        # Burn the atmosphere off worlds with dwarf primaries

        if T == 'D':
            i = D6Rollx2()
            if i == 12: self.atm = 14
            elif i == 11: self.atm = 3
            elif i == 10: self.atm = 2
            elif i == 9: self.atm = 1
            else: self.atm = 0 

        if self.siz == 0: self.atm = 0

    def gen_hyd(self):
        if self.siz == 0: self.hyd = 0
        else:
            self.hyd = D6Rollx2() - 7 + self.siz
            if self.atm in [0, 1, 10, 11, 12]: self.hyd -= 4
            if self.atm == 14: self.hyd -= 2
            if self.hyd < 0: self.hyd = 0

    def gen_pop(self, T, S):
        self.pop = D6Rollx2() - 2

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

        if self.siz <= 2: self.pop -= 1
        if self.atm in [0, 1, 10, 11, 12]: self.pop -= 2
        if self.atm == 6: self.pop  += 3
        if self.atm in [5, 8]: self.pop += 1
        if self.hyd == 0 and self.atm < 3: self.pop -= 2


        # Some additional population modifiers based on settlement type
        # I may move to make these more editable via lists/tuples later


        if self.popType == 0:

            # print("-->" + str(self.popType))

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
        
        self.pMod = D6Rollx2() - 2
        if self.pop > 0 and self.pMod < 1: self.pMod = 1
        if self.pop == 0: self.pMod = 0
        if self.pMod == 10: self.pMod = 9

    def gen_gov(self):
        self.gov = D6Rollx2() - 7 + self.pop
        if self.gov < 0: self.gov = 0
        if self.gov > 15: self.gov = 15
        if self.pop  == 0: self.gov   = 0

    def gen_law(self):
        self.law = D6Rollx2() - 7 + self.gov
        if self.law < 0: self.law = 0
        elif self.law > 15: self.law = 15
        if self.pop == 0: self.law  = 0 
   
    def gen_starPort(self):
        spRoll = D6Rollx2() - 7 + self.pop
        self.starPort = TR_Constants.STARPORTSTABLE.get(spRoll)

    def gen_tlv(self):
        self.tlv = D6Roll()
        if self.starPort in TR_Constants.STARPORTTLMOD: self.tlv += TR_Constants.STARPORTTLMOD.get(self.starPort)
        if self.siz in TR_Constants.SIZETLMOD: self.tlv += TR_Constants.SIZETLMOD.get(self.siz)
        if self.hyd in TR_Constants.HYDTLMOD: self.tlv += TR_Constants.HYDTLMOD.get(self.hyd)
        if self.atm in TR_Constants.ATMTLMOD: self.tlv += TR_Constants.ATMTLMOD.get(self.atm)
        if self.pop in TR_Constants.POPTLMOD: self.tlv += TR_Constants.POPTLMOD.get(self.pop)
        if self.gov in TR_Constants.GOVTLMOD: self.tlv += TR_Constants.GOVTLMOD.get(self.gov)

        if self.tlv < 0: self.tlv = 0
        elif self.tlv > 15: self.tlv = 15

        # Add CE world condition requirements

        if self.hyd in [0, 10] and self.pop > 6 and self.tlv < 4: self.tlv = 4
        if self.atm in [4, 7, 9] and self.tlv < 5: self.tlv = 5
        if self.atm in [0, 1, 2, 3, 10, 11, 12] and self.tlv < 7: self.tlv = 7
        if self.atm in [13, 14] and self.hyd == 10 and self.tlv  < 7: self.tlv = 7

        # Finally, if population is zero, no TL

        if self.pop == 0: self.tlv = 0

    def gen_bases(self):
        # Naval bases

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

        self.bCode = " "
        if nBase and sBase: self.bCode = "A"
        if nBase and not sBase: self.bCode = "N"
        if sBase and pBase: self.bCode = "G"
        if pBase and not sBase: self.bCode = "P"
        if sBase and not nBase and not pBase: self.bCode = "S"

    def gen_tCodeString(self):
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
        self.gen_gov()
        self.gen_law()

        # Generate the starport

        self.gen_starPort()

        # Generate Tech Level

        self.gen_tlv()

        # Determine presence of bases

        self.gen_bases()

        # Generate trade codes

        self.gen_tCodeString()

        # Determine the presence of planetoid belts, gas giants

        self.genBelts()
        self.genGiants()
   
        # Determine travel zones

        self.genZone()


        
    def formatUWPString_text_SEC(self):
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
        self.UWPString += TR_Constants.UWPCODETABLE.get(self.siz)
        self.UWPString += TR_Constants.UWPCODETABLE.get(self.atm)
        self.UWPString += TR_Constants.UWPCODETABLE.get(self.hyd)
        self.UWPString += TR_Constants.UWPCODETABLE.get(self.pop)
        self.UWPString += TR_Constants.UWPCODETABLE.get(self.gov)
        self.UWPString += TR_Constants.UWPCODETABLE.get(self.law)
        self.UWPString += "-" + TR_Constants.UWPCODETABLE.get(self.tlv)
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

        self.UWPString += " " + str(self.pMod) + str(self.nBelts) + str(self.nGiants) + " "

        stellarString = ""
        for star in self.starList:
            stellarString += star + " "
        stellarString.rstrip()

        self.UWPString += stellarString

# Print a formatted UWP line for the world/system

    def printUWPString(self):
        print(self.UWPString)


# Test code here


# i = 1
# while i < 10:
#     w1 = World("Blargo", True, 5)
#     w1.genWorld()
#     w1.formatUWPString_text_SEC()
#     w1.printUWPString()
#     i += 1





