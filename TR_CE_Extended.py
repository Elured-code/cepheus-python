import logging
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

    def gen_stellarClass(self, realismType, isPrimary):
        sClass = ''

        # Realistic classification

        if realismType == TR_Constants.SC_REAL:
            x = TR_Support.D6Rollx2()
            
            # Apply a -1 DM if the object is not a primary
            
            if not isPrimary: x -= 1

            # Look up the stellar class

            if x == 1: 
                sClass = self.gen_brownDwarfClass()

    
            elif x in [2, 3, 4, 5, 6, 7, 8, 9]: sClass = 'M'
            elif x in [10, 11]:
                y = TR_Support.D6Roll()
                if isPrimary: y -= 1
                if y <= 3: sClass = 'K'
                elif y <= 5: sClass = 'G'
                else: sClass = 'F'
            else:
                y = TR_Support.D6Rollx2()
                if isPrimary: y -= 1
                if y <= 9: sClass = 'A'
                elif y <= 11: sClass = 'B'
                else: sClass = 'O'

        # Semi-realistic - slightly more orange, yellow and white stars

        if realismType == TR_Constants.SC_SEMIREAL:
            x = TR_Support.D6Rollx2()
            
            # Apply a -1 DM if the object is not a primary
            
            if not isPrimary: x -= 1

            # Look up the stellar class

            if x == 1: 
                sClass = gen_brownDwarfClass()

            elif x in [2, 3, 4, 5, 6, 7]: sClass = 'M'
            elif x in [8, 9]: sClass = 'K'
            elif x == 10: sClass = 'G'
            elif x == 11: sClass = 'F'
            else:
                y = TR_Support.D6Rollx2()
                if isPrimary: y -= 1
                if y <= 9: sClass = 'A'
                elif y <= 11: sClass = 'B'
                else: sClass = 'O'

        # Fantastic:  more sun-like stars

        if realismType == TR_Constants.SC_FANTASTIC:
            x = TR_Support.D6Rollx2()
            
            # Apply a -1 DM if the object is not a primary
            
            if not isPrimary: x -= 1

            # Look up the stellar class

            if x == 1:
                sClass = gen_brownDwarfClass()

            elif x in [2, 3, 4, 5, 6]: sClass = 'M'
            elif x in [7, 8]: sClass = 'K'
            elif x in [9, 10]: sClass = 'G'
            elif x == 11: sClass = 'F'
            else:
                y = TR_Support.D6Rollx2()
                if isPrimary: y -= 1
                if y <= 9: sClass = 'A'
                elif y <= 11: sClass = 'B'
                else: sClass = 'O'

        
        # Assert block to trap problems where a class is not assigned

        try:
            assert sClass != ''
        except AssertionError as AssertionError:
            logging.log_exception(AssertionError)
        
        return sClass

    # # Change the primary type when needed

    # def changePrimary(newprimary):
    #     sysPrimary = newprimary

    # Determine the spectral class decimal number

    def gen_sClassDecimal(self):
        x = TR_Support.D6Roll() - TR_Support.D6Roll() + 5
        if x == 10: x = 0
        return x

    # Determine a star luminosity class

    def gen_sLum(self):
        lum = ''
        x = TR_Support.D6Rollx2()
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

        sClass = self.gen_stellarClass(realismtype, True)

        # Determine the system nature

        nStars = self.gen_numStars(sClass) 
                        
        # Generate the spectral class decimal

        sClassDec = self.gen_sClassDecimal() 

        # Generate the primary luminosity

        if sClass not in ['L', 'Y', 'T']: sLum = self.gen_sLum()
        else: sLum = ''

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

    def gen_Companion(self, primary):
        
        # Determine the companion stellar class

        if primary == 'Star System': sClass = self.gen_stellarClass(TR_Constants.SC_REAL, False)
        elif primary == 'Brown Dwarf': sClass = self.gen_brownDwarfClass()
        else: 
            starString = ''
            return starString

        # Generate the spectral class decimal

        sClassDec = self.gen_sClassDecimal() 

        # Generate the companion luminosity

        if sClass not in ['L', 'Y', 'T']: sLum = self.gen_sLum()
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

        elif x in [7, 8, 9]: 
            orbitzone = 'Near'
            orbitdistance = (TR_Support.D6Roll() - TR_Support.D6Roll() + 5) * 5

        elif x in [10, 11, 12, 13, 14]: 
            orbitzone = 'Far'
            orbitdistance = (TR_Support.D6Roll() - TR_Support.D6Roll() + 5) * 50

        elif x in [15, 16]: 
            orbitzone = 'Distant'
            orbitdistance = (TR_Support.D6Roll() - TR_Support.D6Roll() + 5) * 500
        
        else: 
            orbitzone = 'Remote'
            orbitdistance = (TR_Support.D6Roll() * 1000) + 4000

        return orbitzone, orbitdistance

    def get_starDetails(self, Class, Lum):

        db = TinyDB('db.json')
        if Class[0] == 'D': starTypeStr = Class + Lum
    
        else: starTypeStr = Class + ' ' + Lum
        try:
            q = Query()
            result = db.search(q.type == starTypeStr)
            return result[0]

        except RuntimeError as e:
            print(repr(e))
            sys.exit()     

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
                starString, nStars, sClass, sLum = self.gen_Primary(TR_Constants.SC_SEMIREAL)

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
            if sysPrimary in ['Star System', 'Brown Dwarf']: self.starDetails[-1].update(self.get_starDetails(sClass, sLum))
 
            outline = '{0: <14}'.format(sysPrimary) + location

            
            # Ok, now that the primary is out of the way, loop through the companions

            objectNumber = 2
            while objectNumber <= nStars:
                # print('Companion generation ' + str(objectNumber) + ' for ' + starString)
                companionString, sClass, sLum = self.gen_Companion(sysPrimary)

                # Get the companion orbit

                # Add the companion to the star list

                self.starList.append(companionString)              
                if sysPrimary in ['Star System', 'Brown Dwarf']: self.starDetails[-1].update(self.get_starDetails(sClass, sLum))
                
                # Get the primary radius and roche limit values - these are needed for orbital calculations below

                rad = self.starDetails[0]['diameter']
                roche = self.starDetails[0]['roche limit']

                coz, cod = self.gen_CompanionOrbit(sysPrimary, objectNumber, rad, roche)
                self.starDetails.append({'orbitzone': coz, 'orbitdistance': cod})  
                self.orbitList[cod] = companionString

                # Add companion details to the star details list

                objectNumber += 1
            
            # Start populating the orbitlist dictionary with any companions
            # This will go in once the orbit and zone object is ready

            # Lets start temporarily by generating the mainworld

            if sysPrimary == 'Star System':
                mw = TR_CE_SRD_World.World("Main-" + location)
                mw.loc = location
                mw.genWorld(location)
                mw.formatUWPString_text_SEC()

                # Add the mainworld to the orbit list dictionary
                # using orbit 3 temporarily

                self.orbitList[3] = mw.UWPString
                # self.orbitList["5"] = mw.UWPString
        else: sysPrimary = 'None'
        self.sysType = sysPrimary

# Test Code

for i in range(1, 11):
    sys1 = System()
    sys1.gen_System('0101', 5, False)
    # print(sys1.sysType + ' ', end = '')

    j = 0
    for star in sys1.starList:
        if sys1.sysType in ['Star System', 'Brown Dwarf']:
            print(star + ' ', end = '')
            if j >= 1: print(star + ' ' + str(sys1.starDetails[j]['orbitzone']) + ' ('  + str(sys1.starDetails[j]['orbitdistance']) + ' AU) ', end = '')
        else: print(sys1.sysType, end = '')
        j += 1
        print()

    if sys1.sysType in ['Star System', 'Brown Dwarf', 'Black Hole']: 
        for key in sorted(sys1.orbitList.keys()):
            print(key, '->', sys1.orbitList[key])

    # if "Mainworld" in sys1.orbitList:
    #     print(sys1.orbitList["Mainworld"].starPort)
    # else: print()







