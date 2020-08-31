import logging

import TR_CE_SRD_World
import TR_CE_EXT_StarClass

import TR_Support

# Constants

# Subsector density

EMPTY_SUBSECTOR = 12
SCATTERED_DENSITY = 10
DISPERSED_DENSITY = 9
AVERAGE_DENSITY = 8
CROWDED_SUBSECTOR = 6
DENSE_SUBSECTOR = 5

# Stellar Class Realism

SC_REAL = 1
SC_SEMIREAL = 2
SC_FANTASTIC = 3

# Subsector Information

SUBSECLETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
FIXEDHEADER = ''' 1-13: Name
15-18: HexNbr
20-28: UWP
   31: Bases
33-47: Codes & Comments
   49: Zone
52-54: PBG
56-57: Allegiance
59-74: Stellar Data

....+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8'''

class System:

# Getters

    @property
    def starList(self):
        return self.__starList

    @property
    def isPresent(self):
        return self.__isPresent

# Setters

    @starList.setter
    def starList(self, starList):
        self.__starList = starList

    @isPresent.setter
    def isPresent(self, isPresent):
        self.__isPresent = isPresent

# Methods

    def gen_systemPresence(self, subSectorType):
        presence = False
        if TR_Support.D6Rollx2() >= subSectorType: presence = True
        return presence

    def gen_systemObject(self, allowUnusual):

        # Default to a star system

        object = 'Star System'

        # Use the unusual objects allowed table

        if allowUnusual:
            x = TR_Support.D6Rollx3()
            if x in [3, 4, 5]: object = 'Rogue Planet' # * = Rogue Planet
            elif x in [6, 7]: object = 'Brown Dwarf' # DB = Brown Dwarf
            elif x == 18: 
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

        if realismType == SC_REAL:
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

        if realismType == SC_SEMIREAL:
            x = TR_Support.D6Rollx2()
            
            # Apply a -1 DM if the object is not a primary
            
            if not isPrimary: x -= 1

            # Look up the stellar class

            if x == 1: 
                sClass = self.gen_brownDwarfClass()

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

        if realismType == SC_FANTASTIC:
            x = TR_Support.D6Rollx2()
            
            # Apply a -1 DM if the object is not a primary
            
            if not isPrimary: x -= 1

            # Look up the stellar class

            if x == 1:
                sClass = self.gen_brownDwarfClass()

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

        sLum = self.gen_sLum()

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

        sClass = sClass + str(sClassDec)
        return sClass, sLum, nStars

    def gen_Companion(self, primary):
        
        # Determine the companion stellar class

        if primary == 'Star System': sClass = self.gen_stellarClass(SC_REAL, False)
        elif primary == 'Brown Dwarf': sClass = self.gen_brownDwarfClass()
        elif primary == 'Black Hole': sClass = self.gen_stellarClass(SC_REAL, False) 
        else:
            sClass = ''
            sLum = ''
            return sClass, sLum

        # Generate the spectral class decimal

        sClassDec = self.gen_sClassDecimal()

        # Generate the companion luminosity

        sLum = self.gen_sLum()

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

        sClass = sClass + str(sClassDec)

        return sClass, sLum

    def gen_System(self, subsectortype, loc, allowexotics, realismtype):
        self.starList = []
               # All worlds generated here are mainworlds

        isMainWorld = True

        # Determine system presence

        self.isPresent = self.gen_systemPresence(DISPERSED_DENSITY)
        
        if self.isPresent:
 
            sysPrimary = self.gen_systemObject(allowexotics)

            # First, always process the system primary, this processing will also determine the number of
            # companions to be generated
            
            # Generate spectral class, decimal and luminosity class for star systems
        
            if sysPrimary == 'Star System': 
                temp = self.gen_Primary(realismtype)
                thisClass = temp[0]
                thisLum = temp[1]
                nStars = temp[2]

                # Dwarfs don't have companions, override if needed

                if thisClass == 'D': nStars = 1


            # Some primaries have been changed to brown dwarfs when generating spectral class
            # Update the primary type, format the star string if so and regenerate the number of objects
            # in the system

                if thisClass in ['L', 'T', 'Y']:
                    sysPrimary = 'Brown Dwarf'
                    nStars = thisSystem.gen_numStars(sysPrimary[0])
                    
            # Process brown dwarfs

            elif sysPrimary == 'Brown Dwarf':
                thisClass = thisSystem.gen_brownDwarfClass() + str(thisSystem.gen_sClassDecimal())
                thisLum = 'BD'
                nStars = thisSystem.gen_numStars(thisClass[0])    

            # Process black holes

            elif sysPrimary == 'Black Hole':
                nStars = thisSystem.gen_numStars(sysPrimary[0])
                thisClass = 'Black Hole'
                thisLum = ''
                

            else: 
                nStars = 1
                thisClass = sysPrimary
                thisLum = ''
                            
            # Now add the star to the list of system stars

            st1 = TR_CE_EXT_StarClass.Star()
            st1.spectralClass = thisClass
            st1.luminosityClass = thisLum
            self.starList.append(st1)

            
            # Ok, now that the primary is out of the way, loop through the companions

            objectNumber = 2
            while objectNumber <= nStars:
                # print('Companion generation ' + str(objectNumber) + ' for ' + starString)
                temp = thisSystem.gen_Companion(sysPrimary)
                thisClass = temp[0]
                thisLum = temp[1]
                
                stx = TR_CE_EXT_StarClass.Star()
                stx.spectralClass = thisClass
                stx.luminosityClass = thisLum
                self.starList.append(stx)

                objectNumber += 1



# Main, will eventually become test code

# Print the subsector header

print(FIXEDHEADER)

# Loop through the subsector hexes, checking for and if required generating mainworlds

for i in range(1, 9):
    for j in range(1, 11):

        thisSystem = System()

        # Format the location string

        loc = format(i, '02d') + format(j, '02d')

        thisSystem.gen_System(AVERAGE_DENSITY, loc, True, SC_FANTASTIC)
        
        if thisSystem.isPresent:
            print(loc + '\t', end = '')
            for aStar in thisSystem.starList:
                
                # Note slightly different print order for white dwarfs vs everything else

                if aStar.luminosityClass != 'D': outputString = aStar.spectralClass + ' ' + aStar.luminosityClass
                else: outputString = aStar.luminosityClass + aStar.spectralClass
                print(outputString.rstrip(), end = '')
                print(' ', end = '')
            print('\r')






