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
        else:
            y = TR_Support.D6Rollx2()
            if y == 2: lum = 'Ia'
            elif y in [3, 4, 5]: lum = 'II'
            elif y in [6, 7, 8]: lum = 'VI'
            elif y in [9, 10, 11]: lum = 'IV'
            else: lum = 'Ib'

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

                    self.starDetails[1]['pMin'] = round(self.starDetails[0]['pMin'], 3)
                    self.starDetails[1]['pMax'] = round(self.starDetails[0]['pMax'], 3)
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
        print(f'{"System Type:":<22}{self.sysType}')
        
        if self.sysType in ['Star System', 'Brown Dwarf']:
            print(f'{"System Primary:":<22}{self.starDetails[0]["type"]}')
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
            for sd in self.starDetails:
                print('*** ' + str(self.starDetails.index(sd)) + ' ', end='')
                print(sd['Contents'])

        # print('##########')
        print()

    # Generate the pool of available worlds

    def gen_worldPool(self):

        # Check for gas giants
        # If the frost line for a star is recorded as -1, then the frost line is outside the stars gravitational limit

        nGG = 0
        i = 0
        hasGG = False
        if self.sysType in ['Star System', 'Brown Dwarf']:
            while i < len(self.starDetails):
                if self.starDetails[i]['Frost Line'] != -1: hasGG = True
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

        print('*** Gas Giants:  ' + str(nGG) + ' ', end = '')
        if nGG != 0: print(gasGiants)
        else: print()

        # Check for planetoid belts and rocky worlds

        if self.sysType in ['Star System', 'Brown Dwarf']:
            nPB = 0

            if TR_Support.D6Rollx2() >= 4:
                nPB = TR_Support.D6Roll() - 3
                if nPB < 1: nPB = 1

            print('*** Planetoid Belts:  ' + str(nPB))

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

            print('*** Rocky Worlds:  ' + str(nRW) + ' ', end = '')
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
                        print('*** Suitable S-Type Gas Giant orbits found for object ' + str(self.starDetails.index(starDetails)))

                        GGOrbitsPresent = True
                        starDetails['hasGG'] = True
                    else: 
                        print('*** No suitable S-Type Gas Giant orbits found for object ' + str(self.starDetails.index(starDetails)))

                else: print('*** No suitable S-Type Gas Giant orbits found for object ' + str(self.starDetails.index(starDetails)))

                # Now check for P-Type orbits

                if 'pMin' in starDetails and 'pMax' in starDetails and 'Frost Line' in starDetails:

                    if starDetails['pMin'] <= starDetails['Frost Line'] <= starDetails['pMax']:
                        print('*** Suitable P-Type Gas Giant orbits found for object ' + str(self.starDetails.index(starDetails)))

                        GGOrbitsPresent = True
                        starDetails['hasGG'] = True
                    else:
                        print('*** No suitable P-Type Gas Giant orbits found for object ' + str(self.starDetails.index(starDetails)))

                else: print('*** No suitable P-Type Gas Giant orbits found for object ' + str(self.starDetails.index(starDetails)))

                # print('*** GG orbits present? ' + str(GGOrbitsPresent))

                # Asume that Gas Giants do not occupy T-Type orbits for ... reasons

            # We now have a determination for each body as to available Gas Giant orbits

            # If no orbits are available for gas giants but they exist, do stuff here:

            if not GGOrbitsPresent and nGG > 0:
                print('*** No available GG orbits, but assigning to system stars')
                
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

        # Special code for black holes will go here

        # # Generate the mainworld

        # mw = TR_CE_SRD_World.World(title)
        # mw.genWorld(location)
        # mw.formatUWPString_text_SEC()

        # print('Mainworld:  ' + mw.UWPString)

    def place_gasGiants(self):
        pass
    
    def gen_System(self, location, density, allowunusual):
        self.starList = []
        self.starDetails = []
        self.orbitList = {}

        # Determine system presence

        isPresent = self.gen_systemPresence(density)

        # If a system is present, start the generation process

        if isPresent:
            sysPrimary = self.gen_systemObject(allowunusual)

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

            self.gen_worldPool()

            # Place gas giants

            self.place_gasGiants()


            # print()

        else: 
            sysPrimary = 'Empty'
            print(sysPrimary)
            self.sysType = sysPrimary



# Test Code

# print('```')
# for i in range(1, 11):
#     print(str(i) + ': ')
#     sys1 = System()
#     sys1.gen_System('0101', 5, True)
#     if sys1.sysType != 'Empty': sys1.print_System()
#     else: print()
# print('```')


#     # print(sys1.sysType + ' ', end = '')

#     # j = 0
#     # for star in sys1.starList:
#     #     if sys1.sysType in ['Star System', 'Brown Dwarf']:
#     #         print(star + ' ', end = '')
#     #         if j >= 1: print(star + ' ' + str(sys1.starDetails[j]['orbitzone']) + ' ('  + str(sys1.starDetails[j]['orbitdistance']) + ' AU) ', end = '')
#     #     else: print(sys1.sysType, end = '')
#     #     j += 1
#     #     print()

#     print(sys1.sysType)
#     if sys1.sysType in ['Star System', 'Brown Dwarf', 'Black Hole']:
#         sortedOrbitList = sorted(sys1.orbitList.items(), key=lambda x: x[0])
#         for orbititem in sortedOrbitList: 
#             print('\t' + str(orbititem[0]) + ' --> ', orbititem[1]['String'])




#         # sortedOrbitList = sorted(sys1.orbitList, key = lambda x: sys1.orbitList[x]['Orbit'])
#         # for orbit in sortedOrbitList:
#         #     print(str(orbit['Orbit' ]) + '\t' + orbit['Details'])


#     # if "Mainworld" in sys1.orbitList:
#     #     print(sys1.orbitList["Mainworld"].starPort)
#     # else: print()







