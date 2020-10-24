#
# Cepheus Engine Extended System Generation
#
# About:
#
# This script generates a CE extended system using Ade Stewart's extended system generation rules
#

#
# Author:   Michael Bailey
# Date:     23 October 2020
#

# Usage
#
# No command line usage - this code is intended to be called by other Python scripts with user interfaces
#

import logging
import random
import sys
from tinydb import TinyDB, Query

import TR_CE_SRD_World
import TR_Constants
import TR_Support


# Constants

# # Subsector density

# EMPTY_SUBSECTOR = 12
# SCATTERED_DENSITY = 10
# DISPERSED_DENSITY = 9
# AVERAGE_DENSITY = 8
# CROWDED_SUBSECTOR = 6
# DENSE_SUBSECTOR = 5



# # Subsector Information

# SUBSECLETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
# FIXEDHEADER = ''' 1-13: Name
# 15-18: HexNbr
# 20-28: UWP
#    31: Bases
# 33-47: Codes & Comments
#    49: Zone
# 52-54: PBG
# 56-57: Allegiance
# 59-74: Stellar Data

# ....+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8'''

# Flags

f_debug = False

class System:

# Getters

    @property
    def starList(self):
        return self.__starList

    @property
    def starDetails(self):
        return self.__starDetails

    @property
    def orbitList(self):
        return self.__orbitList

    @property
    def sysType(self):
        return self.__sysType

    @property
    def p_sMin(self):
        return self.__p_sMin

    @property
    def p_sMax(self):
        return self.__p_sMax

    @property
    def s_sMin(self):
        return self.__s_sMin

    @property
    def s_sMax(self):
        return self.__s_sMax

    @property
    def barycentre(self):
        return self.__barycentre

    @property
    def barycentre_ref(self):
        return self.__barycentre_ref

    @property
    def mainWorld(self):
        return self.__mainWorld

    @property
    def sysUWPString(self):
        return self.__sysUWPString



# Setters

    @starList.setter
    def starList(self, starList):
        self.__starList = starList

    @starDetails.setter
    def starDetails(self, starDetails):
        self.__starDetails = starDetails

    @orbitList.setter
    def orbitList(self, orbitList):
        self.__orbitList = orbitList

    @sysType.setter
    def sysType(self, sysType):
        self.__sysType = sysType

    @p_sMin.setter
    def p_sMin(self, p_sMin):
        self.__p_sMin = p_sMin

    @p_sMax.setter
    def p_sMax(self, p_sMax):
        self.__p_sMax = p_sMax

    @s_sMin.setter
    def s_sMin(self, s_sMin):
        self.__s_sMin = s_sMin

    @s_sMax.setter
    def s_sMax(self, s_sMax):
        self.__s_sMax = s_sMax

    @barycentre.setter
    def barycentre(self, barycentre):
        self.__barycentre = barycentre

    @barycentre_ref.setter
    def barycentre_ref(self, barycentre_ref):
        self.__barycentre_ref = barycentre_ref

    @mainWorld.setter
    def mainWorld(self, mainWorld):
        self.__mainWorld = mainWorld

    @sysUWPString.setter
    def sysUWPString(self, sysUWPString):
        self.__sysUWPString = sysUWPString

    # Methods

    def gen_brownDwarfClass(self):
        x = TR_Support.D6Roll()
        if x in [1, 2, 3]: bdclass = 'L'
        elif x in [4, 5]: bdclass = 'T'
        else: bdclass = 'Y'
        return bdclass


    def gen_systemPresence(self, density):
        presence = False
        subSectorType = TR_Constants.DENSITY_LOOKUP[density]
        if TR_Support.D100Roll() <= subSectorType: presence = True
        return presence

    def gen_systemObject(self, allowUnusual):

        # Default to a star system

        object = 'Star System'

        # Use the unusual objects allowed table

        if allowUnusual:
            x = TR_Support.D6Rollx3()
            if x in [3, 4, 5]: object = 'Rogue Planet' # * = Rogue Planet
            elif x in [6, 7]: object = 'Brown Dwarf' # DB = Brown Dwarf
            # elif x == 18: 
            elif x > 12:
                y = TR_Support.D6Rollx2()
                if y == 2: object = 'Black Hole' # BH = Black Hole
                elif y == 3: object = 'Stellar Nursery' # SN = Stellar Nursery
                elif y <= 9: object = 'Nebula' # NB = Nebula
                elif y <= 11: object = 'Neutron Star' # NS = Neutron Star / Pulsar
                else: object = 'Anomaly' # ? = Anomaly
            else: object = 'Star System'

        # Otherwise use the 'normal' table

        else: 
            x = TR_Support.D6Rollx2()
            if x in [2, 3]: object = 'Rogue Planet'
            elif x in [4, 5]: object = 'Brown Dwarf'
            else: object = 'Star System'

        return object

    def gen_stellarClass(self, realismType, seqno):
        sClass = ''

        # Realistic classification

        if realismType == TR_Constants.SC_REAL:

            # Make a roll, with the star sequence number as a negative DM

            x = TR_Support.D6Rollx2() - seqno + 1

            # Look up the stellar class

            if x == 1: 
                sClass = self.gen_brownDwarfClass()

    
            elif x in [2, 3, 4, 5, 6, 7, 8, 9]: sClass = 'M'
            elif x in [10, 11]:
                y = TR_Support.D6Roll() - seqno 
                if y <= 3: sClass = 'K'
                elif y <= 5: sClass = 'G'
                else: sClass = 'F'
            else:
                y = TR_Support.D6Rollx2() - seqno
                if y <= 9: sClass = 'A'
                elif y <= 11: sClass = 'B'
                else: sClass = 'O'

        # Semi-realistic - slightly more orange, yellow and white stars

        if realismType == TR_Constants.SC_SEMIREAL:
            x = TR_Support.D6Rollx2() - seqno + 1

            # Look up the stellar class

            if x == 1: 
                sClass = self.gen_brownDwarfClass()
            elif x in [2, 3, 4, 5, 6, 7]: sClass = 'M'
            elif x in [8, 9]: sClass = 'K'
            elif x == 10: sClass = 'G'
            elif x == 11: sClass = 'F'
            else:
                y = TR_Support.D6Rollx2() - seqno
                if y <= 9: sClass = 'A'
                elif y <= 11: sClass = 'B'
                else: sClass = 'O'

        # Fantastic:  more sun-like stars

        if realismType == TR_Constants.SC_FANTASTIC:
            x = TR_Support.D6Rollx2() - seqno + 1
            
            # Look up the stellar class

            if x == 1:
                sClass = self.gen_brownDwarfClass()

            elif x in [2, 3, 4, 5, 6]: sClass = 'M'
            elif x in [7, 8]: sClass = 'K'
            elif x in [9, 10]: sClass = 'G'
            elif x == 11: sClass = 'F'
            else:
                y = TR_Support.D6Rollx2() - seqno
                if y <= 9: sClass = 'A'
                elif y <= 11: sClass = 'B'
                else: sClass = 'O'

        
        # Assert block to trap problems where a class is not assigned

        try:
            assert sClass != ''
        except AssertionError as AssertionError:
            logging.exception(AssertionError)
        
        return sClass

        # Determine the spectral class decimal number

    def gen_sClassDecimal(self):
        x = TR_Support.D6Roll() - TR_Support.D6Roll() + 5
        if x == 10: x = 0
        return x

        # Determine a star luminosity class

    def gen_sLum(self, seqno):
        lum = ''
        x = TR_Support.D6Rollx2() - seqno + 1
        if x in [2, 3]: lum = 'D'
        elif x in [4, 5, 6, 7, 8, 9, 10]: lum = 'V'
        elif x == 11: lum = 'III'
        elif x == 12:
            y = TR_Support.D6Rollx2()
            if y == 2: lum = 'Ia'
            elif y in [3, 4, 5]: lum = 'II'
            elif y in [6, 7, 8]: lum = 'VI'
            elif y in [9, 10, 11]: lum = 'IV'
            else: lum = 'Ib'
        else: lum = 'V'

        # Assert block to catch any errors

        try:
            assert lum != ''
        except AssertionError as AssertionError:
            logging.exception(AssertionError)

        return lum

    def gen_numStars(self, spectralClass):
        nStars = 1
        a = TR_Support.D6Rollx2()
        if spectralClass in ['A', 'B', 'O']:
            if a in [2, 3]: nStars = 1
            elif a in [4, 5, 6, 7, 8, 9]: nStars = 2
            elif a == 10: nStars = 3
            else: nStars = 4
        elif spectralClass in ['K', 'G', 'F']:
            if a in [2, 3, 4, 5, 6, 7]: nStars = 1
            elif a in [8, 9, 0, 11]: nStars = 2
            else: nStars = 3
        elif spectralClass == 'M':
            if a in [2, 3, 4, 5, 6, 7, 8]: nStars = 1
            elif a in [9, 10, 11]: nStars = 2
            else: nStars = 3
        elif spectralClass in ['L', 'T', 'Y']:
            if TR_Support.D6Rollx2() == 12: nStars = 2
            else: nStars = 1
        elif spectralClass == 'X':
            if TR_Support.D6Rollx2() >= 11: nStars = 2
            else: nStars = 1
        
        return nStars
        
    def fix_subDwarfs(self, aclass):
        if aclass in ['O', 'B', 'K', 'F']: return 'V'
        else: return 'VI'

    def fix_subGiants(self, aclass, aclassdec):
        if (aclass == 'K' and aclassdec in [2, 3, 4, 5, 6, 7, 8, 9]) or aclass == 'M':
            x = TR_Support.D6Roll()
            if x <= 5:
                rclass = 'K'
                rclassdec = 0
            else:
                rclass = 'K'
                rclassdec = 1
        else:
            rclass = aclass
            rclassdec = aclassdec
        return rclass, rclassdec
        
    def gen_Primary(self, realismtype):
        
        # Determine the primary stellar class

        sClass = self.gen_stellarClass(realismtype, 1)

        # Determine the system nature

        nStars = self.gen_numStars(sClass) 
                        
        # Generate the spectral class decimal

        sClassDec = self.gen_sClassDecimal() 

        # Generate the primary luminosity

        if sClass not in ['L', 'Y', 'T']: sLum = self.gen_sLum(1)
        else: sLum = 'BD'

        # Apply restrictions - once companion code is in will need to iterate through all bodies

        # Fix subgiants

        if sLum == 'IV':
            temp = self.fix_subGiants(sClass, sClassDec)
            sClass = temp[0]
            sClassDec = temp[1]
        
        # Fix subdwarfs

        if sLum == 'VI': sLum = self.fix_subDwarfs(sClass)

        # Fix yellow supergiants
        # Code will go in when rules are clarified

        # Fix dwarfs

        if sLum == 'D': sClass = ''

        # Fix Type O giants

        if sClass == 'O' and sLum in ['Ia', 'Ib', 'II'] and sClassDec <= 6: sLum = 'I'
                    
        # Format the star string
        
        if sLum != 'D': starString = sClass + str(sClassDec) + ' ' + sLum
        else: starString = sLum + str(sClassDec)

        return starString, nStars, sClass + str(sClassDec), sLum

    def gen_Companion(self, primary, seqno):
        
        # Determine the companion stellar class

        if primary in ['Star System', 'Black Hole']: sClass = self.gen_stellarClass(TR_Constants.SC_REAL, seqno)
        elif primary == 'Brown Dwarf': sClass = self.gen_brownDwarfClass()
        else: 
            starString = ''
            return starString

        # Generate the spectral class decimal

        sClassDec = self.gen_sClassDecimal() 

        # Generate the companion luminosity

        if sClass not in ['L', 'Y', 'T']: sLum = self.gen_sLum(seqno)
        else: sLum = ''

        # Apply restrictions 

        # Fix subgiants

        if sLum == 'IV':
            temp = self.fix_subGiants(sClass, sClassDec)
            sClass = temp[0]
            sClassDec = temp[1]
        
        # Fix subdwarfs

        if sLum == 'VI': sLum = self.fix_subDwarfs(sClass)

        # Fix yellow supergiants
        # Code will go in when rules are clarified

        # Fix dwarfs

        if sLum == 'D': sClass = ''

        # Fix Type O giants

        if sClass == 'O' and sLum in ['Ia', 'Ib', 'II'] and sClassDec <= 6: sLum = 'I'
                    
        # Format the star string
        
        if sLum != 'D': starString = sClass + str(sClassDec) + ' ' + sLum
        else: starString = sLum + str(sClassDec)

        return starString, sClass + str(sClassDec), sLum

    def gen_CompanionOrbit(self, primary, seqno, pd, proche):
        
        # Get the companion orbit band

        if primary != 'Black Hole': x = TR_Support.D6Rollx3()
        else: x = TR_Support.D6Rollx2() + 6

        if seqno == 3: x+= 4
        elif seqno == 4: x+= 8

        # Get companion zone and 'raw' orbit distance - this may be altered after return

        if x in [3, 4]: 
            orbitzone = 'Contact'
            orbitdistance = (TR_Support.D6Roll() - TR_Support.D6Roll() + 5) * pd/2
            if orbitdistance < proche: orbitdistance = proche
        
        elif x in [5, 6]: 
            orbitzone = 'Close'
            orbitdistance = (TR_Support.D6Roll() - TR_Support.D6Roll() + 5) * 0.5
            if orbitdistance < 0.5: orbitdistance = 0.5

        elif x in [7, 8, 9]: 
            orbitzone = 'Near'
            orbitdistance = (TR_Support.D6Roll() - TR_Support.D6Roll() + 5) * 5
            if orbitdistance < 5: orbitdistance = 5

        elif x in [10, 11, 12, 13, 14]: 
            orbitzone = 'Far'
            orbitdistance = (TR_Support.D6Roll() - TR_Support.D6Roll() + 5) * 50
            if orbitdistance < 50: orbitdistance = 50

        elif x in [15, 16]: 
            orbitzone = 'Distant'
            orbitdistance = (TR_Support.D6Roll() - TR_Support.D6Roll() + 5) * 500
            if orbitdistance < 500: orbitdistance = 500
        
        else: 
            orbitzone = 'Remote'
            orbitdistance = (TR_Support.D6Roll() * 1000) + 4000
            if orbitdistance < 5000: orbitdistance = 5000

        orbitdistance = round(orbitdistance, 3)

        return orbitzone, orbitdistance

    def get_starDetails(self, thisclass, thislum):

        db = TinyDB('db.json')
        starTypeStr = ''
    
        if thisclass[0] in ['L', 'T', 'Y']: starTypeStr = thisclass
        if thislum != 'D': starTypeStr = thisclass + ' ' + str(thislum)
        else: starTypeStr = str(thislum) + thisclass
        try:
            q = Query()
            result = db.search(q.type == starTypeStr.rstrip())
            return result[0]

        except RuntimeError as e:
            print(repr(e))
            sys.exit()     

    def gen_BinaryArchitecture(self):

        # First, lets find the barycentre between the two objects

        Mb = self.starDetails[1]['mass']
        Ma = self.starDetails[0]['mass']
        AU = self.starDetails[1]['orbitdistance']

        # print('Ma = ' + str(Ma))
        # print('Mb = ' + str(Mb))
        # print('AU = ' + str(AU))

        if self.starDetails[1]['orbitzone'] in ['Contact Binary', 'Close', 'Near', 'Far']:
            barycentre = AU * (Mb / (Ma + Mb))
        else:
            x =  TR_Support.D6Roll()
            if x >= 4:
                barycentre = AU * (Mb / (Ma + Mb))
            else: barycentre = 999999
        # print('\tbarycentre = ' + str(barycentre))

        # Calculate restrictions on S-Type orbits
        # First, if the barycentre lies within 20% of the separation, the mainworld cannot have an S-Type orbit

        if barycentre > self.starDetails[1]['orbitdistance'] * 0.8 and barycentre < self.starDetails[1]['orbitdistance'] * 1.2:
            primaryStypes = False
            self.starDetails[0]['sMin'] = 0
            self.starDetails[0]['sMax'] = 0
            self.starDetails[1]['sMin'] = self.starDetails[1]['roche limit']
            self.starDetails[1]['sMax'] = self.starDetails[1]['orbitdistance'] * 0.2
            
        else: 
            primaryStypes = True
            self.starDetails[0]['sMin'] = self.starDetails[0]['roche limit']
            self.starDetails[0]['sMax'] = self.starDetails[1]['orbitdistance'] * 0.2
            self.starDetails[1]['sMin'] = self.starDetails[1]['roche limit']
            self.starDetails[1]['sMax'] = self.starDetails[1]['orbitdistance'] * 0.2            

        if primaryStypes: 
            if self.starDetails[0]['sMin'] >= self.starDetails[0]['sMax']: 
                self.starDetails[0]['sMin'] = self.starDetails[0]['sMax'] = 0

        
        if self.starDetails[1]['sMin'] >= self.starDetails[1]['sMax']:
            self.starDetails[1]['sMin'] = self.starDetails[1]['sMax'] = 0


        # If the maximum s_Type orbit is outside the star gravitational limit, reduce it to that limit

        if self.starDetails[0]['sMax'] > self.starDetails[0]['Limit']: self.starDetails[0]['sMax'] = self.starDetails[0]['Limit']
        if self.starDetails[1]['sMax'] > self.starDetails[1]['Limit']: self.starDetails[1]['sMax'] = self.starDetails[1]['Limit']

        # Round all values to 3 decimals

        self.starDetails[0]['sMin'] = round(self.starDetails[0]['sMin'], 3)
        self.starDetails[0]['sMax'] = round(self.starDetails[0]['sMax'], 3)
        self.starDetails[1]['sMin'] = round(self.starDetails[1]['sMin'], 3)
        self.starDetails[1]['sMax'] = round(self.starDetails[1]['sMax'], 3)

        # print('\tPrimary S-Type Orbit limits: ' + str(self.starDetails[0]['sMin']) + ' - ' + str(self.starDetails[0]['sMax']))
        # print('\tSecondary S-Type Orbit limits: ' + str(self.starDetails[1]['sMin']) + ' - ' + str(self.starDetails[1]['sMax']))

        # Save the barycentre in case we need it later, this can go in the system object
        # and set the barycentre reference to the primary - this may be orverriden for trinary systems

        # Calculate the limits for P-Type orbits.  For accounting purposes these will be assigned to the primary, but they 
        # really orbit the primary-secondary barycentre

        # First, determine if the minumum possible orbit is outside the primary-secondary outer limit

        pmin = (self.starDetails[1]['orbitdistance'] * 2 ) + barycentre
        pmax = self.starDetails[0]['Limit'] + self.starDetails[1]['Limit']

        if pmin > pmax: primaryPtypes = False
        else: primaryPtypes = True
        
        if primaryPtypes:
            # Minimum orbit is the twice the primary-secondary separation, measured from the barycentre

            self.starDetails[0]['pMin'] = pmin
            # Maximum orbit is the sum of the primary and secondary outer limits (for now, may change)

            self.starDetails[0]['pMax'] = pmax

            # Round it all to 3 decimal places

            self.starDetails[0]['pMin'] = round(self.starDetails[0]['pMin'], 3)
            self.starDetails[0]['pMax'] = round(self.starDetails[0]['pMax'], 3)
            # print('\tPrimary - Secondary P-Type limits: ' + str(self.starDetails[0]['pMin']) + ' - ' + str(self.starDetails[0]['pMax']))

        # Finally, add the stable T-Type orbits at the primary-secondary L4 and L5 locations

        self.starDetails[0]['tL4'] = self.starDetails[0]['tL5'] = self.starDetails[1]['orbitdistance']

        self.barycentre = barycentre
        self.barycentre_ref = 0
        
    def gen_TrinaryArchitecture(self, usecase):
        
        # barycentre calculations are going to run into the 3 body problem, so our options are:
        # 
        # 1:  The tertiary orbits far enough from the primary-secondary pair to be in a P-Type orbit
        #     Tertiary must be 2 x primary - secondary distance, measured from the primary-secondary barycentre

        if usecase == 'both':
            # print('\tTertiary orbits primary/secondary pair. Checking tertiary orbit...')

            #  Determine the barycentre reference

            if  self.starDetails[0]['mass'] + self.starDetails[1]['mass'] >= self.starDetails[2]['mass']:  self.barycentre_ref = 0
            else: self.barycentre_ref = 2

            # Don't need to adjust orbit now - sufficient distance from the barycentre is a precondition of this block

            self.starDetails[2]['orbitdistance'] += self.barycentre
            self.starDetails[2]['orbitdistance'] = round(self.starDetails[2]['orbitdistance'], 3)

            # Set the maximum S-Type orbit to 20% of the distance to the secondary orbit

            self.starDetails[2]['sMin'] = self.starDetails[2]['roche limit']
            self.starDetails[2]['sMax'] = (self.starDetails[2]['orbitdistance'] - self.starDetails[1]['orbitdistance']) *  0.2 

            if self.starDetails[2]['sMax'] > self.starDetails[2]['Limit']: self.starDetails[2]['sMax'] = self.starDetails[2]['Limit']
            if self.starDetails[2]['sMin'] > self.starDetails[2]['sMax']: self.starDetails[2]['sMin'] = self.starDetails[2]['sMax'] = 0

            # print('\tTertiary S-Type Orbit limits: ' + str(self.starDetails[2]['sMin']) + ' - ' + str(self.starDetails[2]['sMax']))   

            # Calculate the limits for P-Type orbits.  For accounting purposes these will be assigned to the primary, but they 
            # really orbit the primary-secondary-tertiary barycentre

            # First, determine if the minumum possible orbit is outside the primary-secondary-tertiary outer limit

            pmin = (self.starDetails[2]['orbitdistance'] * 2 ) + self.barycentre
            pmax = self.starDetails[0]['Limit'] + self.starDetails[1]['Limit'] + self.starDetails[2]['Limit']

            # Limit the max P-Type orbit to 20% of the distance to the tertiary

            if pmax > (self.starDetails[2]['orbitdistance'] - self.barycentre) * 0.2: pmax = (self.starDetails[2]['orbitdistance'] - self.barycentre) * 0.2

            if pmin > pmax: primaryPtypes = False
            else: primaryPtypes = True 
            
            if primaryPtypes:
                # Minimum orbit is the twice the primary-secondary separation, measured from the barycentre

                self.starDetails[0]['pMin'] = pmin
                # Maximum orbit is the sum of the primary and secondary outer limits (for now, may change)

                self.starDetails[0]['pMax'] = pmax

                # Round it all to 3 decimal places

                self.starDetails[0]['pMin'] = round(self.starDetails[0]['pMin'], 3)
                self.starDetails[0]['pMax'] = round(self.starDetails[0]['pMax'], 3)
                # print('\tPrimary - Secondary P-Type limits: ' + str(self.starDetails[0]['pMin']) + ' - ' + str(self.starDetails[0]['pMax']))        

        # 2:  if the tertiary is within the minimum distance to orbit the pair, it can:
        #    a - orbit the primary
        #    b - orbit the companion

            # Finally, add the T-Type orbits at the primary-tertiary L4 and L5 Lagrange points

            self.starDetails[0]['tL4b'] = self.starDetails[0]['tL5b'] = self.starDetails[2]['orbitdistance']
        
        elif usecase in ['primary']:

            # print('\tTertiary orbits primary.  Checking orbits')

            # First make sure that the tertiary orbits in an allowed orbit around the primary
            # Recalculate if necessary (using a random distance between the primary min and max S-Type orbits)

            is_between = self.starDetails[0]['sMin'] <= self.starDetails[2]['orbitdistance'] <=self.starDetails[0]['sMax']

            # Also check that the orbit does npto clash with the secondary

            is_secondary_blocked = self.starDetails[1]['sMin'] <= self.starDetails[2]['orbitdistance'] <= self.starDetails[1]['sMax']

            while not is_between and not is_secondary_blocked:
                self.starDetails[2]['orbitdistance'] = random.randint(round(self.starDetails[0]['sMin']), round(self.starDetails[0]['sMax']))

                # Recalculate the orbit zone as well

                if self.starDetails[2]['orbitdistance'] < 0.5: self.starDetails[2]['orbitzone'] = 'Contact Binary'
                elif self.starDetails[2]['orbitdistance'] < 5: self.starDetails[2]['orbitzone'] = 'Close'
                elif self.starDetails[2]['orbitdistance'] < 50: self.starDetails[2]['orbitzone'] = 'Near'
                elif self.starDetails[2]['orbitdistance'] < 500: self.starDetails[2]['orbitzone'] = 'Far'
                elif self.starDetails[2]['orbitdistance'] < 5000: self.starDetails[2]['orbitzone'] = 'Distant'
                else: self.starDetails[2]['orbitdistance'] = 'Remote'

                # print('Moved tertiary orbit to ' + str(self.starDetails[2]['orbitdistance']) + ' AU (' + self.starDetails[2]['orbitzone'] + ')')

                # Calculate the limits for P-Type orbits.  For accounting purposes these will be assigned to the primary, but they 
                # really orbit the primary-secondary-tertiary barycentre

                # First, determine if the minumum possible orbit is outside the primary-secondary-tertiary outer limit

                pmin = (self.starDetails[2]['orbitdistance'] * 2 ) + self.barycentre
                pmax = self.starDetails[0]['Limit'] + self.starDetails[1]['Limit'] + self.starDetails[2]['Limit']

                if pmin > pmax: primaryPtypes = False
                else: primaryPtypes = True 
                
                if primaryPtypes:
                    # Minimum orbit is the twice the primary-secondary separation, measured from the barycentre

                    self.starDetails[0]['pMin'] = pmin
                    # Maximum orbit is the sum of the primary and secondary outer limits (for now, may change)

                    self.starDetails[0]['pMax'] = pmax

                    # Round it all to 3 decimal places

                    self.starDetails[0]['pMin'] = round(self.starDetails[0]['pMin'], 3)
                    self.starDetails[0]['pMax'] = round(self.starDetails[0]['pMax'], 3)
                    # print('\tPrimary - Secondary - Tertiary P-Type limits: ' + str(self.starDetails[0]['pMin']) + ' - ' + str(self.starDetails[0]['pMax']))

                # Recheck if blocked

                is_secondary_blocked = self.starDetails[1]['sMin'] <= self.starDetails[2]['orbitdistance'] <= self.starDetails[1]['sMax']

            # Finally, add the T-Type orbits at the primary-tertiary L4 and L5 Lagrange points

            self.starDetails[0]['tL4c'] = self.starDetails[0]['tL5c'] = self.starDetails[2]['orbitdistance']

        elif usecase in ['secondary']:

            # print('\tTertiary orbits secondary.  Checking orbits')

            # First make sure that the tertiary orbits in an allowed orbit around the secondary
            # Recalculate if necessary (using a random distance between the primary min and max S-Type orbits)

            is_between = self.starDetails[1]['sMin'] <= self.starDetails[2]['orbitdistance'] <=self.starDetails[1]['sMax']
            if not is_between:
                
                self.starDetails[2]['orbitdistance'] = random.randint(round(self.starDetails[1]['sMin']), round(self.starDetails[1]['sMax']))

                # Recalculate the orbit zone as well

                if self.starDetails[2]['orbitdistance'] < 0.5: self.starDetails[2]['orbitzone'] = 'Contact Binary'
                elif self.starDetails[2]['orbitdistance'] < 5: self.starDetails[2]['orbitzone'] = 'Close'
                elif self.starDetails[2]['orbitdistance'] < 50: self.starDetails[2]['orbitzone'] = 'Near'
                elif self.starDetails[2]['orbitdistance'] < 500: self.starDetails[2]['orbitzone'] = 'Far'
                elif self.starDetails[2]['orbitdistance'] < 5000: self.starDetails[2]['orbitzone'] = 'Distant'
                else: self.starDetails[2]['orbitdistance'] = 'Remote'

                # print('Moved tertiary orbit to ' + str(self.starDetails[2]['orbitdistance'] + ' AU (' + self.starDetails[2]['orbitzone'] + ')'))

                # Calculate the limits for P-Type orbits.  For accounting purposes these will be assigned to the primary, but they 
                # really orbit the primary-secondary-tertiary barycentre

                # First, determine if the minumum possible orbit is outside the primary-secondary-tertiary outer limit

                pmin = (self.starDetails[2]['orbitdistance'] * 2 ) + self.barycentre
                pmax = self.starDetails[0]['Limit'] + self.starDetails[1]['Limit'] + self.starDetails[2]['Limit']

                if pmin > pmax: secondaryPtypes = False
                else: secondaryPtypes = True 
                
                if secondaryPtypes:
                    # Minimum orbit is the twice the secondary-tertiary separation, measured from the barycentre

                    self.starDetails[1]['pMin'] = pmin
                    # Maximum orbit is the sum of the secondary and tertiary outer limits (for now, may change)

                    self.starDetails[1]['pMax'] = pmax

                    # Round it all to 3 decimal places

                    self.starDetails[1]['pMin'] = round(self.starDetails[1]['pMin'], 3)
                    self.starDetails[1]['pMax'] = round(self.starDetails[1]['pMax'], 3)
                    # print('\tPrimary - Secondary - Tertiary P-Type limits: ' + str(self.starDetails[0]['pMin']) + ' - ' + str(self.starDetails[0]['pMax']))

                    # Check that the maximum P-Type is inside 20% of the primary-secondary distance and correct if needed

                    if self.starDetails[1]['pMax'] > self.starDetails[1]['orbitdistance']: self.starDetails[1]['pMax'] = self.starDetails[1]['orbitdistance']

            # Finally, add the T-Type orbits at the primary-tertiary L4 and L5 Lagrange points

            self.starDetails[0]['tL4d'] = self.starDetails[0]['tL5d'] = self.starDetails[2]['orbitdistance']

        # 3:  if the tertiary is outside the outer limit for both the primary and secondary then it is unbound



        elif usecase == 'unbound':

            # Stuff needs to go in here

            pass

        # Now calculate the primary-tertiary barycentre and recalculate the primaries allowed S-Type orbits

        Mb = self.starDetails[2]['mass']
        Ma = self.starDetails[0]['mass']
        AU = self.starDetails[2]['orbitdistance']

        self.barycentre = AU * (Mb / (Ma + Mb))

        # print('\tPrimary - tertiary barycentre at ' + str(round(barycentre)) + ' AU')

        if self.starDetails[0]['sMax'] > self.starDetails[2]['orbitdistance'] * 0.2:
            self.starDetails[0]['sMax'] = self.starDetails[2]['orbitdistance'] * 0.2
            if self.starDetails[0]['sMin'] > self.starDetails[0]['sMax']: self.starDetails[0]['sMin'] = self.starDetails[0]['sMax'] = 0
            # print('\tPrimary S-Type Orbit limits now ' + str(self.starDetails[0]['sMin'] + ' - ' + str(self.starDetails[0]['sMax'])))

        # Calculate the tertiary S-Type orbit limits
        
        self.starDetails[2]['sMin'] = self.starDetails[2]['roche limit']
        self.starDetails[2]['sMax'] = self.starDetails[2]['orbitdistance'] * 0.2
        if self.starDetails[2]['sMax'] > self.starDetails[2]['Limit']: self.starDetails[2]['sMax'] = self.starDetails[2]['Limit']
        if self.starDetails[2]['sMin'] > self.starDetails[2]['sMax']: self.starDetails[2]['sMin'] = self.starDetails[2]['sMax'] 
    
       
    # Write out the system contents
    
    def print_System(self):

        # print('System Type:\t\t' + self.sysType)
        if f_debug: print(f'{"DEBUG: System Type:":<22}{self.sysType}')
        if self.sysType in ['Star System']: 
            if f_debug: print('DEBUG: Mainworld (orbit TBA): ' + self.mainWorld.UWPString)
        
        if self.sysType in ['Star System', 'Brown Dwarf']:
            print(f'{"DEBUG: System Primary:":<22}{self.starDetails[0]["type"]}')
            if 'sMin' in self.starDetails[0]: print('\tS-Orbit inner limit = ' + str(self.starDetails[0]['sMin']))
            if 'sMax' in self.starDetails[0]: print('\tS-Orbit outer limit = ' + str(self.starDetails[0]['sMax']))
            if 'pMin' in self.starDetails[0]: print('\tP-Orbit inner limit = ' + str(self.starDetails[0]['pMin']))
            if 'pMax' in self.starDetails[0]: print('\tP-Orbit outer limit = ' + str(self.starDetails[0]['pMax']))
            if 'tL4' in self.starDetails[0]: print('\tT-Orbits at L4/L5 points = ' + str(self.starDetails[0]['tL4']))
            if 'tL4b' in self.starDetails[0]: print('\tT-Orbits at L4/L5 points = ' + str(self.starDetails[0]['tL4b']))
            if 'tL4c' in self.starDetails[0]: print('\tT-Orbits at L4/L5 points = ' + str(self.starDetails[0]['tL4c']))
            if 'tL4d' in self.starDetails[0]: print('\tT-Orbits at L4/L5 points = ' + str(self.starDetails[0]['tL4d']))

            if len(self.starDetails) >= 2: 
                print(f'{"System Secondary:":<22}{self.starDetails[1]["type"]}')
                print('\tDistance from Primary:\t' + str(self.starDetails[1]['orbitdistance']) + ' (' + self.starDetails[1]['orbitzone'] + ')')
                if 'sMin' in self.starDetails[1]: print('\tS-Orbit inner limit = ' + str(self.starDetails[1]['sMin']))
                if 'sMax' in self.starDetails[1]: print('\tS-Orbit outer limit = ' + str(self.starDetails[1]['sMax']))
                if 'pMin' in self.starDetails[1]: print('\tP-Orbit inner limit = ' + str(self.starDetails[1]['pMin']))
                if 'pMax' in self.starDetails[1]: print('\tP-Orbit outer limit = ' + str(self.starDetails[1]['pMax']))
                

            if len(self.starDetails) > 2:
                print(f'{"System Tertiary:":<22}{self.starDetails[2]["type"]}')
                if self.starDetails[2]['orbitsubject'] == 'primary': print('\tDistance from primary:\t' + str(self.starDetails[2]['orbitdistance']) + ' (' + self.starDetails[2]['orbitzone'] + ')')
                elif self.starDetails[2]['orbitsubject'] == 'secondary': print('\tDistance from secondary\t' + str(self.starDetails[2]['orbitdistance']) + ' (' + self.starDetails[2]['orbitzone'] + ')')
                elif self.starDetails[2]['orbitsubject'] == 'both': print('\tDistance from barycentre:\t' + str(self.starDetails[2]['orbitdistance']) + ' (' + self.starDetails[2]['orbitzone'] + ')')
                elif self.starDetails[2]['orbitsubject'] == 'unbound': print('\tDistance from primary (unbound):\t' + str(self.starDetails[2]['orbitdistance']) + ' (' + self.starDetails[2]['orbitzone'] + ')')

                if 'sMin' in self.starDetails[2]: print('\tS-Orbit inner limit = ' + str(self.starDetails[2]['sMin']))
                if 'sMax' in self.starDetails[2]: print('\tS-Orbit outer limit = ' + str(self.starDetails[2]['sMax']))
                if 'pMin' in self.starDetails[2]: print('\tP-Orbit inner limit = ' + str(self.starDetails[2]['pMin']))
                if 'pMax' in self.starDetails[2]: print('\tP-Orbit outer limit = ' + str(self.starDetails[2]['pMax']))

            # Some temporary code to dump out system contents

            print('System Contents:')
            i = 0
            for sd in self.starDetails:
                if f_debug: print('DEBUG: body ' + str(i+1) + ':')

                for contents in sd['Contents']:
                    print(contents)
 
                i += 1

        # print('##########')
        print()

    # Format the system extended UWP string

    def formatUWPString_text_SEC(self):

        # Format a UWP text string for the mainworld            
        
        self.mainWorld.formatUWPString_text_SEC()

        # Now add a Non-Aligned (default) allegiance code
        # and the star details to the mainworld UWP string

        self.mainWorld.UWPString += " Na"
        
        for star in self.starList:
            self.mainWorld.UWPString += " " + star
    pass

    # Generate the pool of available worlds

    def gen_worldPool(self):

        # Check for gas giants
        # If the frost line for a star is recorded as -1, then the frost line is outside the stars gravitational limit

        # Initialise some local variables to ensure that they are bound

        nPB = 0
        nGG = 0
        i = 0
        hasGG = False
        GGOrbitsPresent = False

        if self.sysType in ['Star System', 'Brown Dwarf']:
            hasGG = True
            i += 1
        
        # Systems that aren't normally capable of having a gas giant may have a captured one

        if not hasGG: 
            if TR_Support.D6Rollx2() >= 11: nGG = 1
        else:

            # Brown dwarfs rarely contain gas giants

            if self.sysType == 'Brown Dwarf':
                if self.starDetails[0]['type'][0] == 'L':
                    if TR_Support.D6Rollx2() >= 9:
                        nGG = TR_Support.D6Roll() - 4
                        if nGG < 1: nGG = 1
                elif self.starDetails[0]['type'][0] == 'T':
                    if TR_Support.D6Rollx2() >= 11: 
                        nGG = 1
                else: nGG = 0
            
            # Now determne the number of gas giansts

            else:
                if TR_Support.D6Rollx2() >= 5: 
                    nGG = TR_Support.D6Roll() - 2
                    if nGG < 1: nGG = 1
        
        # Determine each gas giant type

        gasGiants = []
        if nGG > 0:
            j = 1
            while j <= nGG:
                if TR_Support.D6Roll() < 4: gasGiants.append('LGG')
                else: gasGiants.append('SGG')

                j += 1

        if f_debug: print('DEBUG: Gas Giants:  ' + str(nGG) + ' ', end = '')
        if nGG != 0: 
            if f_debug: print(gasGiants, end='')
        else: 
            if f_debug: print()

        # Check for planetoid belts and rocky worlds

        if self.sysType in ['Star System', 'Brown Dwarf']:
            nPB = 0

            if TR_Support.D6Rollx2() >= 4:
                nPB = TR_Support.D6Roll() - 3
                if nPB < 1: nPB = 1

            if f_debug: print('DEBUG: Planetoid Belts:  ' + str(nPB))

            # Populate rocky worlds
            # Note we are selecting the mainworld after, so add 1 to the D6+1 as per the rules in Section 11

            nRW = TR_Support.D6Roll() + 2
            rockyWorlds = []
            k = 1

            # Determine each world type

            while k <= nRW:

                x = TR_Support.D6Rollx2()
                if x <= 3: rockyWorlds.append('Dwarf World')
                elif x <= 8: rockyWorlds.append('Normal World')
                else: rockyWorlds.append('Superterran World')
          
                k += 1

            if f_debug: 
                print('DEBUG: Rocky Worlds:  ' + str(nRW) + ' ', end = '')
                if nRW != 0: print(rockyWorlds)

            # Assign gas giants between stars

            # Iterate through each star to determine if suitable orbits exist

            # orbits = []
            for starDetails in self.starDetails:
                GGOrbitsPresent = False
                starDetails['hasGG'] = False

                # Check if S-Type orbits can be used
                # First check that tehre are S-Type orbits

                if 'sMin' in starDetails and 'sMax' in starDetails and 'Frost Line' in starDetails:

                    if starDetails['sMin'] <= starDetails['Frost Line'] <= starDetails['sMax']:
                        if f_debug: print('DEBUG: Suitable S-Type Gas Giant orbits found for object ' + str(self.starDetails.index(starDetails)))

                        GGOrbitsPresent = True
                        starDetails['hasGG'] = True
                    else: 
                        if f_debug: print('DEBUG: No suitable S-Type Gas Giant orbits found for object ' + str(self.starDetails.index(starDetails)))

                else: 
                    if f_debug: print('DEBUG: No suitable S-Type Gas Giant orbits found for object ' + str(self.starDetails.index(starDetails)))

                # Now check for P-Type orbits

                if 'pMin' in starDetails and 'pMax' in starDetails and 'Frost Line' in starDetails:

                    if starDetails['pMin'] <= starDetails['Frost Line'] <= starDetails['pMax']:
                        if f_debug: print('DEBUG: Suitable P-Type Gas Giant orbits found for object ' + str(self.starDetails.index(starDetails)))

                        GGOrbitsPresent = True
                        starDetails['hasGG'] = True
                    else:
                        if f_debug: print('DEBUG: No suitable P-Type Gas Giant orbits found for object ' + str(self.starDetails.index(starDetails)))

                else: 
                    if f_debug: print('DEBUG: No suitable P-Type Gas Giant orbits found for object ' + str(self.starDetails.index(starDetails)))

                # print('DEBUG: GG orbits present? ' + str(GGOrbitsPresent))

                # Asume that Gas Giants do not occupy T-Type orbits for ... reasons

            # We now have a determination for each body as to available Gas Giant orbits

            # If no orbits are available for gas giants but they exist, do stuff here:

            if not GGOrbitsPresent and nGG > 0:
                if f_debug: print('DEBUG: No available GG orbits, but assigning to system stars')
                
                # No orbits but place anyway!

                for objLabel in gasGiants:
                    x = random.randint(0, len(self.starDetails) - 1)
                    self.starDetails[x]['Contents'].append({'Type': objLabel})
                
            # Otherwise, divide up the giants:

            elif nGG > 0:

                # First find a GG to place in the innermost eligible orbit around the primary

                if 'LGG' in gasGiants and 'SGG' in gasGiants:
                    x = TR_Support.D6Roll()
                    if x <= 5: objLabel = 'LGG' 
                    else: objLabel = 'SGG'
                elif 'LGG' in gasGiants: objLabel = 'LGG'
                else: objLabel = 'SGG'

                # First assign the GG to the primary, if orbits are available

                if self.starDetails[0]['hasGG']: self.starDetails[0]['Contents'].append({'Type': objLabel})
                elif len(self.starDetails) > 1 and self.starDetails[1]['hasGG']: self.starDetails[1]['Contents'].append({'Type': objLabel})
                elif len(self.starDetails) > 2 and self.starDetails[2]['hasGG']: self.starDetails[1]['Contents'].append({'Type': objLabel})  

                # Remove the GG from the pool

                gasGiants.remove(objLabel)

                # Now iterate through the remaining gas giants

                for objLabel in gasGiants:
                    ggPlaced = False

                    while not ggPlaced:
                        x = random.randint(0, len(self.starDetails) - 1)
                        if self.starDetails[x]['hasGG']:
                            self.starDetails[x]['Contents'].append({'Type': objLabel})
                            ggPlaced = True

            # Now divide up the planetoid belts

            if nPB > 0:

                i = 1
                while i <= nPB:

                    x = random.randint(0, len(self.starDetails) - 1)
                    self.starDetails[x]['Contents'].append({'Type': 'Planetoid Belt'})
                    i += 1
    
        return nPB, nGG

        
        # Special code for black holes will go here

        # # Generate the mainworld

        # mw = TR_CE_SRD_World.World(title)
        # mw.genWorld(location)
        # mw.formatUWPString_text_SEC()

        # print('Mainworld:  ' + mw.UWPString)

    def place_gasGiants(self):

        # Ok lets start with any gas giants orbiting the primary system, then move to the other bodies
        # We will do this the loop below, checking to see if:
        #   1 - the body exists - this is implied in the loop
        #   2 - it has gas giants

        # i is the body number

        i = 0

        for stardetails in self.starDetails:

            # lastorbit is the orbit of the previously placed object
            # Default this to 0 to avoid unbound variable warnings
            # Also assing an initial value to lastorbit for the same reason

            lastorbit = orbitdistance = 0
        
            # j is the gas giant counter for this body

            j = 0

            #  Reset the extreme inner migration flag

            f_xim = False

            for contents in stardetails['Contents']:

                if contents['Type'] == 'LGG' or contents['Type'] == 'SGG':

                    # If this is the first giant, place at the frost line
                    # If the star does not have a frost line then place the GG randomly between 
                    # the Roche Limit and Outer Limit

                    if j == 0:
                        if stardetails['Frost Line'] != -1: orbitdistance = stardetails['Frost Line']
                        else:
                            rl = stardetails['roche limit']
                            ol = stardetails['outer limit']
                            orbitdistance = random.uniform(rl, ol)

                        # Next determine gas giant migration

                        DM = len(contents) - 1
                        x = TR_Support.D6Rollx2() - DM

                        if x <= 3:

                            # Extreme inward migration

                            if f_debug: print('DEBUG: Extreme inward migration')
                            orbitdistance = (stardetails['Frost Line'] * 0.1) + ((TR_Support.D6Roll() - 3) * (stardetails['Frost Line'] * 0.1))
                            if orbitdistance <= 0: orbitdistance = TR_Support.D6Rollx2() * stardetails['diameter']/2

                            # Set the extreme inner migration flag if this is the first gas gianst

                            if j == 0: f_xim = True

                        elif x in [4, 5]:

                            # Limited inward migration

                            if f_debug: print('DEBUG: Limited inward migration')
                            orbitdistance = (stardetails['Frost Line'] * 0.4) + (TR_Support.D6Roll() * (stardetails['Frost Line'] * 0.1))
                            if orbitdistance >= stardetails['Frost Line']: orbitdistance = stardetails['Frost Line'] * 0.95

                        elif x in [6, 7, 8, 9, 10]:

                            # No migration

                            if f_debug: print('DEBUG: No migration')
                            orbitdistance = stardetails['Frost Line'] + ((TR_Support.D6Roll() - 1) * stardetails['Frost Line'] * 0.02)

                        elif x in [11, 12]:

                            # Limited outward migration

                            if f_debug: print('DEBUG: Limited outward migration')
                            y = random.randint(1, 3)
                            orbitdistance = stardetails['Frost Line'] * (1 + y/10)

                        # Note orbit as the last placed orbit

                        lastorbit = orbitdistance
                        

                    # Now place subsequent giants

                    else:

                    # First, if this is the second giant and the first one has been subject to extreme inward migration
                    # (i.e. the f_xim flag is set) then run some special case code to determine the second giants position
                    # this code is a repeat of the migration code above, but with extreme inward migration removed

                        if j == 1 and f_xim:

                            x = TR_Support.D6Rollx2()
                            if x in [4, 5]:

                                # Limited inward migration

                                if f_debug: print('DEBUG: Limited inward migration')
                                orbitdistance = (stardetails['Frost Line'] * 0.4) + (TR_Support.D6Roll() * (stardetails['Frost Line'] * 0.1))
                                if orbitdistance >= stardetails['Frost Line']: orbitdistance = stardetails['Frost Line'] * 0.95

                            elif x in [6, 7, 8, 9, 10]:

                                # No migration

                                if f_debug: print('DEBUG: No migration')
                                orbitdistance = stardetails['Frost Line'] + ((TR_Support.D6Roll() - 1) * stardetails['Frost Line'] * 0.02)

                            elif x in [11, 12]:

                                # Limited outward migration

                                if f_debug: print('DEBUG: Limited outward migration')
                                y = random.randint(1, 3)
                            
                                orbitdistance = stardetails['Frost Line'] * (1 + y/10)
                            
                        else: 
                            
                            # Place remaining gas giants in near bodean outward orbits from the last orbit (
                            # set at the end of the previous loop)

                            z = TR_Support.D6Rollx2()

                            # Unusual orbits not yet implemented.  When ready change == 1 to == 2
                            if z == 1:

                                # Unusual orbit

                                contents['Status'] = 'Not yet implemented (unusual orbit) - ignore values'

                            elif z == 3: orbitdistance = lastorbit * 1.5
                            elif z in [4, 5]: orbitdistance = lastorbit * 1.75
                            elif z in [6, 7, 8]: orbitdistance = lastorbit * 2
                            elif z in [9, 10]: orbitdistance = lastorbit *2.25
                            elif z == 11: orbitdistance = lastorbit * 2.5
                            else: orbitdistance = lastorbit * 3

                            # Calculate minor variance

                            mv = (TR_Support.D6Roll() - TR_Support.D6Roll()) * 0.02
                            orbitdistance *= (1 + mv)
                    

                    # Check that the placed object is in a suitable orbit, and annotate with the orbit type
                    # If not then move to the nearest available orbit outwards

                    if stardetails['sMin'] <= orbitdistance <= stardetails['sMax']: contents['Orbit Type'] = 'S-Type Orbit'
                    elif 'pMin' in stardetails:
                        if stardetails['pMin'] <= orbitdistance <= stardetails['pMax']: contents['Orbit Type'] = 'P-Type Orbit'
                    else:
                        if orbitdistance < stardetails['sMin']: 
                            orbitdistance = stardetails['sMin']
                            contents['Orbit Type'] = 'S-Type Orbit'
                        elif 'pMin' in stardetails and orbitdistance < stardetails['pMin']: 
                            orbitdistance = stardetails['pMin']
                            contents['Orbit Type'] = 'P-Type Orbit'
                        else: 
                            orbitdistance = stardetails['sMax']
                            contents['Orbit Type'] = 'S-Type Orbit'

                    orbitdistance = float("{:.3f}".format(orbitdistance))
                    if f_debug: print('DEBUG: Placing gas giant #' + str(j+1) + ' at ' + str(orbitdistance) + ' AU from body ' + str(i+1))

                    # Format the orbit distance to 3 decimals and add to the contents record


                    contents['Orbital Distance'] = lastorbit = orbitdistance

                    # Finally record the position of the first gas giant for later use

                    if j == 0:
                        stardetails['firstGG'] = orbitdistance

                    # Progressively record the GG position as the outermost GG

                    stardetails['lastGG'] = orbitdistance

                j += 1
                
            i += 1


    def place_Belts(self):

        # Iterate through the star bodies, then through each body contents looking for planetoid belts

        for stardetails in self.starDetails:

            # Initialise some variables to avoid potential unbound conditions

            orbitdistance = 0

            for contents in stardetails['Contents']:

                if contents['Type'] == 'Planetoid Belt':
                    contents['Status'] = 'Unplaced'

                    # Belts will be in one of a number of places:
                    # 1 - inside the innermost rocky planet (these will be placed later)
                    # 2 - inside the first gas giant
                    # 3 - outside the last gas giant

                    # This will be determined by a random roll

                    x = TR_Support.D6Rollx2()

                    if x <= 3:

                        # Hold it over

                        contents['Status'] = 'Hold'

                    elif x <= 8:

                        # Place in first inward bodean from GG #1 (if it exists) otherwise hold it over until rocky worlds have been placed

                        if 'firstGG' in stardetails:
                            fGG = stardetails['firstGG']
                            y = TR_Support.D6Rollx2()

                            # Note that planetoid belts should not have unusual orbits

                            if y <= 3: orbitdistance = fGG * 0.3
                            elif y <= 5: orbitdistance = fGG * 0.4
                            elif y <= 8: orbitdistance = fGG * 0.5
                            elif y <= 10: orbitdistance = fGG * 0.6
                            elif y <= 11: orbitdistance = fGG * 0.7
                            else: orbitdistance = fGG * 0.85
                            contents['Status'] = 'Placed'
                           
                        else:

                            contents['Status'] = 'Hold'

                    else:

                        if 'lastGG' in stardetails:

                        # Place beyond the last GG using outward bodean table for placement

                            lGG = stardetails['lastGG']
                            y = TR_Support.D6Rollx2()
                            if y <= 3: orbitdistance = lGG * 1.5
                            elif y <= 5: orbitdistance = lGG * 1.75
                            elif y <= 8: orbitdistance =  lGG * 2
                            elif y <= 10: orbitdistance = lGG * 2.25
                            elif y <= 11: orbitdistance = lGG * 2.5
                            else: orbitdistance = lGG * 3
                            contents['Status'] = 'Placed'

                        else:
                            contents['Status'] = 'Hold'


                    # Determine minor variation for placed belts and updated the contents record with orbital distance

                    if contents['Status'] == 'Placed':

                        vf = 1 + ((TR_Support.D6Roll() - TR_Support.D6Roll()) / 100)
                        orbitdistance *= vf

                        # Check that the placed object is in a suitable orbit, and annotate with the orbit type
                        # If not then move to the nearest available orbit outwards

                        if stardetails['sMin'] <= orbitdistance <= stardetails['sMax']: contents['Orbit Type'] = 'S-Type Orbit'
                        elif 'pMin' in stardetails:
                            if stardetails['pMin'] <= orbitdistance <= stardetails['pMax']: contents['Orbit Type'] = 'P-Type Orbit'
                        else:
                            if orbitdistance < stardetails['sMin']: 
                                orbitdistance = stardetails['sMin']
                                contents['Orbit Type'] = 'S-Type Orbit'
                            elif 'pMin' in stardetails and orbitdistance < stardetails['pMin']: 
                                orbitdistance = stardetails['pMin']
                                contents['Orbit Type'] = 'P-Type Orbit'
                            else: 
                                orbitdistance = stardetails['sMax']
                                contents['Orbit Type'] = 'S-Type Orbit'

                        orbitdistance = float("{:.3f}".format(orbitdistance))
                        contents['Orbital Distance'] = orbitdistance

    def assign_Zones(self):
        
        for sd in self.starDetails:

            # Get the zone boundaries for each body

            hminus = sd['H-']
            hzeroa  = sd['H'] - (sd['H'] - sd['H-'])/2
            hzerob  = sd['H'] + (sd['H+'] - sd['H'])/2
            hplus   = sd['H+']


            for contents in sd['Contents']:
                if 'Orbital Distance' in contents:
                    d = contents['Orbital Distance']
                    if 0 <= d < hminus: contents['Zone'] = 'Inner Zone'
                    elif hminus <= d < hzeroa: contents['Zone'] = 'H- Zone'
                    elif hzeroa <= d < hzerob: contents['Zone'] = 'H Zone'
                    elif hzerob <= d < hplus: contents['Zone'] = 'H+ Zone'
                    else: contents['Zone'] = 'Outer Zone'
        
    def gen_System(self, location, density, allowunusual, wName):
        self.starList = []
        self.starDetails = []
        self.orbitList = {}

        # Determine system presence

        isPresent = self.gen_systemPresence(density)

        # If a system is present, start the generation process

        if isPresent:
            sysPrimary = self.gen_systemObject(allowunusual)
            if f_debug: print('DEBUG: ' + sysPrimary)

            # First, always process the system primary, this processing will also determine the number of
            # companions to be generated
                
            # Generate spectral class, decimal and luminosity class for star systems
            
            sClass = sLum = ''

            if sysPrimary == 'Star System': 
                starString, nStars, sClass, sLum = self.gen_Primary(TR_Constants.SC_REAL)

                # Dwarfs don't have companions, override if needed

                if sClass == 'D': nStars = 1

            # Some primaries have been changed to brown dwarfs when generating spectral class
            # Update the primary type, format the star string if so and regenerate the number of objects
            # in the system

                if sClass in ['L', 'T', 'Y']:
                    sysPrimary = 'Brown Dwarf'
                    nStars = self.gen_numStars(starString[0])
                    
            # Process brown dwarfs

            elif sysPrimary == 'Brown Dwarf': 
                sClass = self.gen_brownDwarfClass() + str(self.gen_sClassDecimal())
                starString = sClass + ' BD'
                nStars = self.gen_numStars(starString[0])    

            # Process black holes

            elif sysPrimary == 'Black Hole':
                nStars = self.gen_numStars(sysPrimary[0])
                starString = 'X'
 

            elif sysPrimary == 'Neutron Star':
                nStars = 1
                starString = 'NS'

            else: 
                nStars = 1
                starString = ''

            # Add the star to the list of system stars
                
            self.starList.append(starString)            
            self.starDetails.append({'orbitzone': '', 'orbitdistance': ''})            
            if sysPrimary in ['Star System', 'Brown Dwarf']: self.starDetails[0].update(self.get_starDetails(sClass, sLum))

            # print('Primary: ' + sysPrimary, end = '')
            if sysPrimary in ['Star System', 'Brown Dwarf']: 
                # print(' ' + self.starDetails[0]['type'])

            # Is solo, we can generate the primary S-Type orbit bounds here

                if nStars == 1:
                    self.starDetails[0]['sMin'] = self.starDetails[0]['roche limit']
                    self.starDetails[0]['sMax'] = self.starDetails[0]['Limit']
                    # print('\tPrimary S-Type Orbit limits: ' + str(self.starDetails[0]['sMin']) + ' - ' + str(self.starDetails[0]['sMax']))
            
            # Do some fudging for black holes to avoid crashes - this will be replaced shortly with proper table lookup
            elif sysPrimary == 'Black Hole': 
                self.starDetails[0]['mass'] = 999999999
                self.starDetails[0]['roche limit'] = 0
                self.starDetails[0]['Limit'] = 10000
            

            # Generate the first companion 

            if nStars >= 2:
                # print('\nGenerating companion')
                companionstring, companionclass, companionlum = self.gen_Companion(sysPrimary, 2)
                if sysPrimary != 'Black Hole': companionzone, companiondistance = self.gen_CompanionOrbit(sysPrimary, 2, self.starDetails[0]['diameter'], self.starDetails[0]['roche limit'])
                else: companionzone, companiondistance = self.gen_CompanionOrbit(sysPrimary, 2, 0, 0)
                self.starList.append(companionstring)
                self.starDetails.append({'orbitzone': companionzone, 'orbitdistance': companiondistance})
                self.starDetails[1].update(self.get_starDetails(companionclass, companionlum))
                
                # print('Secondary: ' + self.starDetails[1]['type'])
                # print('\tOrbit Distance ' + str(self.starDetails[1]['orbitdistance']) + ' AU (' + self.starDetails[1]['orbitzone'] + ')')

                # If the companion is larger than the primary, swap them

                if self.starDetails[1]['mass'] > self.starDetails[0]['mass']:
                    temprecord = self.starDetails[0]
                    self.starDetails[0] = self.starDetails[1]
                    self.starDetails[1] = temprecord
                    self.starDetails[1]['orbitdistance'] = self.starDetails[0]['orbitdistance']
                    self.starDetails[1]['orbitzone'] = self.starDetails[0]['orbitzone']
                    del self.starDetails[0]['orbitdistance']
                    del self.starDetails[0]['orbitzone']                 
                
                self.gen_BinaryArchitecture()

            if nStars >= 3:
                # print('\nGenerating tertiary')
                companionstring, companionclass, companionlum = self.gen_Companion(sysPrimary, 3)

                # Generate the tertiary and add it to the star details
             
                companionzone, companiondistance = self.gen_CompanionOrbit(sysPrimary, 3, self.starDetails[0]['diameter'], self.starDetails[0]['roche limit'])
                companiondistance = round(companiondistance, 3)
                self.starList.append(companionstring)
                self.starDetails.append({'orbitzone': companionzone, 'orbitdistance': companiondistance})
                self.starDetails[2].update(self.get_starDetails(companionclass, companionlum)) 

                # If the companion is larger than the primary, swap them and regenerate the primary-secondary architcture

                if self.starDetails[2]['mass'] > self.starDetails[0]['mass']:
                    temprecord = self.starDetails[0]
                    self.starDetails[0] = self.starDetails[2]
                    self.starDetails[2] = temprecord
                    self.starDetails[2]['orbitdistance'] = self.starDetails[0]['orbitdistance']
                    self.starDetails[2]['orbitzone'] = self.starDetails[0]['orbitzone']
                    del self.starDetails[0]['orbitdistance']
                    del self.starDetails[0]['orbitzone']
                    self.gen_BinaryArchitecture()

                # Make a choice - is the companion orbiting the primary, secondary or both

                # If the tertiary is further than the secondary orbit distance + barycentre x 2 then it orbits both

                if companiondistance > (self.starDetails[1]['orbitdistance'] *2 ) + self.barycentre:
                    self.starDetails[2]['orbitsubject'] = 'both'
                    self.gen_TrinaryArchitecture('both')  

                # Otherwise, determine which body (if any) the tertiary orbits
                # Weight the odds in favour of the larger body

                else:
                    ma = self.starDetails[0]['mass']
                    mb = self.starDetails[1]['mass']

                    # Convert the masses to parts of a hundred and roll

                    ma = round(ma/(ma + mb) * 100, 0)
                    mb = round(mb/(ma + mb) * 100, 0)

                    if TR_Support.D6Roll() >= 5: 
                        self.starDetails[2]['orbitsubject'] = 'primary'
                        self.gen_TrinaryArchitecture('unbound')
                    elif TR_Support.D100Roll() <= ma: 
                        self.starDetails[2]['orbitsubject'] = 'primary'
                        self.gen_TrinaryArchitecture('primary')
                    else: 
                        self.starDetails[2]['orbitsubject'] = 'secondary'
                        self.gen_TrinaryArchitecture('secondary')

            self.sysType = sysPrimary

            # Generate the pool of available worlds

            # First initialise a contents list for each star

            for SD in self.starDetails:
                SD['Contents'] = []

            nBelts, nGiants = self.gen_worldPool()

            # Place gas giants

            self.place_gasGiants()

            # Place belts

            self.place_Belts()


            # Assign each object to an orbital zone around its primary

            c = 0
            for sd in self.starDetails:
                c += len(sd['Contents'])

            if c > 0: 
                if f_debug: print('DEBUG: ' + str(c) + ' contents found, assigning to zones')
                self.assign_Zones()

            # Generate the mainworld if appropriate, this will be assigned to an orbit later

            if sysPrimary in ['Star System']:
                self.mainWorld = TR_CE_SRD_World.World(wName)
                self.mainWorld.genWorld(location)   

                # Substitute the generated nunber of belts and giants

                self.mainWorld.nBelts = nBelts
                self.mainWorld.nGiants = nGiants

                # Get the mainworld UWP text string, including stellar data

                self.formatUWPString_text_SEC()
                self.sysUWPString = self.mainWorld.UWPString
            
            # Otherwise generate a UWP string line for the non-stellaer object

            else:
                self.sysUWPString = '             ' + location + ' ' + sysPrimary          

            # print()

        else: 
            sysPrimary = 'Empty'
            if f_debug: print('DEBUG: ' + sysPrimary)
            self.sysType = sysPrimary

# Test Code

# print('```')
# for i in range(1, 11):
#     if f_debug: print('DEBUG: System #' + str(i) + ': ')
#     sys1 = System()
#     sys1.gen_System('0101', 5, True, 'Testworld')
#     if sys1.sysType != 'Empty': sys1.print_System()
# #   else: print()
# print('```')








