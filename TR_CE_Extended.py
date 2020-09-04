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
                sClass = gen_brownDwarfClass()

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
                sClass = gen_brownDwarfClass()

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
            logging.log_exception(AssertionError)
        
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
            logging.log_exception(AssertionError)

        return lum

    def gen_brownDwarfClass(self):
        x = TR_Support.D6Roll()
        if x in [1, 2, 3]: bdclass = 'L'
        elif x in [4, 5]: bdclass = 'T'
        else: bdclass = 'Y'
        return bdclass

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

        if primary == 'Star System': sClass = self.gen_stellarClass(TR_Constants.SC_REAL, seqno)
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
            secondaryStypes = True
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
        
        elif usecase in ['primary']:

            # print('\tTertiary orbits primary.  Checking orbits')

            # First make sure that the tertiary orbits in an allowed orbit around the primary
            # Recalculate if necessary (using a random distance between the primary min and max S-Type orbits)

            is_between = self.starDetails[0]['sMin'] <= self.starDetails[2]['orbitdistance'] <=self.starDetails[0]['sMax']
            if not is_between:
                range = round(self.starDetails[0]['sMax'] - self.starDetails[0]['sMin'])
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

        elif usecase in ['secondary']:

            # print('\tTertiary orbits secondary.  Checking orbits')

            # First make sure that the tertiary orbits in an allowed orbit around the secondary
            # Recalculate if necessary (using a random distance between the primary min and max S-Type orbits)

            is_between = self.starDetails[1]['sMin'] <= self.starDetails[2]['orbitdistance'] <=self.starDetails[1]['sMax']
            if not is_between:
                range = round(self.starDetails[1]['sMax'] - self.starDetails[1]['sMin'])
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

            # Now calculate the primary-tertiary barycentre and recalculate the primaries allowed S-Type orbits

            Mb = self.starDetails[2]['mass']
            Ma = self.starDetails[0]['mass']
            AU = self.starDetails[2]['orbitdistance']

            barycentre = AU * (Mb / (Ma + Mb))

            # print('\tPrimary - tertiary barycentre at ' + str(round(barycentre)) + ' AU')

            if self.starDetails[0]['sMax'] > barycentre * 0.2:
                self.starDetails[0]['sMax'] = barycentre * 0.2
                if self.starDetails[0]['sMin'] > self.starDetails[0]['sMax']: self.starDetails[0]['sMin'] = self.starDetails[0]['sMax'] = 0
                # print('\tPrimary S-Type Orbit limits now ' + str(self.starDetails[0]['sMin'] + ' - ' + str(self.starDetails[0]['sMax'])))

            # Calculate the tertiary S-Type orbit limits
            
            self.starDetails[2]['sMin'] = self.starDetails[2]['roche limit']
            self.starDetails[2]['sMax'] = barycentre * 0.2
            if self.starDetails[2]['sMax'] > self.starDetails[2]['Limit']: self.starDetails[2]['sMax'] = self.starDetails[2]['Limit']
            if self.starDetails[2]['sMin'] > self.starDetails[2]['sMax']: self.starDetails[2]['sMin'] = self.starDetails[2]['sMax'] 


     


        # 3:  if the tertiary is outside the outer limit for both the primary and secondary then it is unbound

        elif usecase == 'unbound':

            # Stuff needs to go in here

            pass
    

    # Write out the system contents
    def print_System(self):

        print('System Type:\t\t' + self.sysType)
        
        if self.sysType in ['Star System', 'Brown Dwarf']:
            print('System Primary:\t\t' + self.starDetails[0]['type'])
            if 'sMin' in self.starDetails[0]: print('\tS-Orbit inner limit = ' + str(self.starDetails[0]['sMin']))
            if 'sMax' in self.starDetails[0]: print('\tS-Orbit outer limit = ' + str(self.starDetails[0]['sMax']))
            if 'pMin' in self.starDetails[0]: print('\tP-Orbit inner limit = ' + str(self.starDetails[0]['pMin']))
            if 'pMax' in self.starDetails[0]: print('\tP-Orbit outer limit = ' + str(self.starDetails[0]['pMax']))

            if len(self.starDetails) >= 2: 
                print('System Secondary:\t' + self.starDetails[1]['type'])
                print('\tDistance from Primary:\t' + str(self.starDetails[1]['orbitdistance']) + ' (' + self.starDetails[1]['orbitzone'] + ')')
                if 'sMin' in self.starDetails[1]: print('\tS-Orbit inner limit = ' + str(self.starDetails[1]['sMin']))
                if 'sMax' in self.starDetails[1]: print('\tS-Orbit outer limit = ' + str(self.starDetails[1]['sMax']))
                if 'pMin' in self.starDetails[1]: print('\tP-Orbit inner limit = ' + str(self.starDetails[1]['pMin']))
                if 'pMax' in self.starDetails[1]: print('\tP-Orbit outer limit = ' + str(self.starDetails[1]['pMax']))

            if len(self.starDetails) > 2:
                print('System Tertiary:\t\t' + self.starDetails[2]['type'])
                if self.starDetails[2]['orbitsubject'] == 'primary': print('\tDistance from Pr:imary:\t\t' + str(self.starDetails[2]['orbitdistance']) + ' (' + self.starDetails[2]['orbitzone'] + ')')
                elif self.starDetails[2]['orbitsubject'] == 'secondary': print('\tDistance from Secondary\t\t' + str(self.starDetails[2]['orbitdistance']) + ' (' + self.starDetails[2]['orbitzone'] + ')')
                elif self.starDetails[2]['orbitsubject'] == 'both': print('\tDistance from system barycentre:\t' + str(self.starDetails[2]['orbitdistance']) + ' (' + self.starDetails[2]['orbitzone'] + ')')

                if 'sMin' in self.starDetails[2]: print('\tS-Orbit inner limit = ' + str(self.starDetails[2]['sMin']))
                if 'sMax' in self.starDetails[2]: print('\tS-Orbit outer limit = ' + str(self.starDetails[2]['sMax']))
                if 'pMin' in self.starDetails[2]: print('\tP-Orbit inner limit = ' + str(self.starDetails[2]['pMin']))
                if 'pMax' in self.starDetails[2]: print('\tP-Orbit outer limit = ' + str(self.starDetails[2]['pMax']))

        print('##########')
        print()

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
                starString, nStars, sClass, sLum = self.gen_Primary(TR_Constants.SC_FANTASTIC)

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
            

            # Generate the first companion 

            if nStars >= 2:
                # print('\nGenerating companion')
                companionstring, companionclass, companionlum = self.gen_Companion(sysPrimary, 2)
                companionzone, companiondistance = self.gen_CompanionOrbit(sysPrimary, 2, self.starDetails[0]['diameter'], self.starDetails[0]['roche limit'])
                self.starList.append(companionstring)
                self.starDetails.append({'orbitzone': companionzone, 'orbitdistance': companiondistance})
                self.starDetails[1].update(self.get_starDetails(companionclass, companionlum))
                
                # print('Secondary: ' + self.starDetails[1]['type'])
                # print('\tOrbit Distance ' + str(self.starDetails[1]['orbitdistance']) + ' AU (' + self.starDetails[1]['orbitzone'] + ')')
                
                self.gen_BinaryArchitecture()

            if nStars >= 3:
                # print('\nGenerating tertiary')
                companionstring, companionclass, companionlum = self.gen_Companion(sysPrimary, 3)

                # Generate the tertiary and add it to the star details
             
                companionzone, companiondistance = self.gen_CompanionOrbit(sysPrimary, 3, self.starDetails[0]['diameter'], self.starDetails[0]['roche limit'])
                self.starList.append(companionstring)
                self.starDetails.append({'orbitzone': companionzone, 'orbitdistance': companiondistance})
                self.starDetails[2].update(self.get_starDetails(companionclass, companionlum)) 

                # print('Tertiary: ' + companionclass + ' ' + companionlum)
                # print('\tOrbit ' + str(companiondistance) + ' (' + companionzone + ')')   

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




            # print()

        else: 
            sysPrimary = 'Empty'
            print(sysPrimary)
        self.sysType = sysPrimary



# Test Code

print('```')
for i in range(1, 21):
    print(str(i) + ': ', end = '')
    sys1 = System()
    sys1.gen_System('0101', 5, False)
    sys1.print_System()
print('```')
    # print(sys1.sysType + ' ', end = '')

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







