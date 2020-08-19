import TR_CE_SRD_World

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

# Setters

    @starList.setter
    def starList(self, starList):
        self.__starList = starList

# Methods

def gen_systemPresence(subSectorType):
    presence = False
    if TR_Support.D6Rollx2() >= subSectorType: presence = True
    return presence

def gen_systemObject(allowUnusual):

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

def gen_stellarClass(realismType, isPrimary):
    sClass = ''

    # Realistic classification

    if realismType == SC_REAL:
        x = TR_Support.D6Rollx2()
        
        # Apply a -1 DM if the object is not a primary
        
        if not isPrimary: x -= 1

        # Look up the stellar class

        if x == 1: 
            sClass = gen_brownDwarfClass()

 
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

    if realismType == SC_FANTASTIC:
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
        Logging.log_exception(error)
    
    return sClass

# # Change the primary type when needed

# def changePrimary(newprimary):
#     sysPrimary = newprimary

# Determine the spectral class decimal number

def gen_sClassDecimal():
    x = TR_Support.D6Roll() - TR_Support.D6Roll() + 5
    if x == 10: x = 0
    return x

# Determine a star luminosity class

def gen_sLum():
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
        Logging.log_exception(error)

    return lum

def gen_brownDwarfClass():
    x = TR_Support.D6Roll()
    if x in [1, 2, 3]: bdclass = 'L'
    elif x in [4, 5]: bdclass = 'T'
    else: bdclass = 'Y'
    return bdclass

def gen_numStars(spectralClass):
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
    
def fix_subDwarfs(aclass):
    if aclass in ['O', 'B', 'K', 'F']: return 'V'
    else: return 'VI'

def fix_subGiants(aclass, aclassdec):
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
    
def gen_Primary(realismtype):
    
    # Determine the primary stellar class

    sClass = gen_stellarClass(realismtype, True)

    # Determine the system nature

    nStars = gen_numStars(sClass) 
                    
    # Generate the spectral class decimal

    sClassDec = gen_sClassDecimal() 

    # Generate the primary luminosity

    if sClass not in ['L', 'Y', 'T']: sLum = gen_sLum()
    else: sLum = ''

    # Apply restrictions - once companion code is in will need to iterate through all bodies

    # Fix subgiants

    if sLum == 'IV':
        temp = fix_subGiants(sClass, sClassDec)
        sClass = temp[0]
        sClassDec = temp[1]
    
    # Fix subdwarfs

    if sLum == 'VI': sLum = fix_subDwarfs(sClass)

    # Fix yellow supergiants
    # Code will go in when rules are clarified

    # Fix dwarfs

    if sLum == 'D': sClass = ''

    # Fix Type O giants

    if sClass == 'O' and sLum in ['Ia', 'Ib', 'II'] and sClassDec <= 6: sLum = 'I'
                
    # Format the star string
    
    if sLum != 'D': starString = sClass + str(sClassDec) + ' ' + sLum
    else: starString = sLum + str(sClassDec)

    return starString, nStars

def gen_Companion(primary):
    
    # Determine the companion stellar class

    if primary == 'Star System': sClass = gen_stellarClass(SC_REAL, False)
    elif primary == 'Brown Dwarf': sClass = gen_brownDwarfClass()
    else: 
        starString = ''
        return starString

    # Generate the spectral class decimal

    sClassDec = gen_sClassDecimal() 

    # Generate the companion luminosity

    if sClass not in ['L', 'Y', 'T']: sLum = gen_sLum()
    else: sLum = ''

    # Apply restrictions 

    # Fix subgiants

    if sLum == 'IV':
        temp = fix_subGiants(sClass, sClassDec)
        sClass = temp[0]
        sClassDec = temp[1]
    
    # Fix subdwarfs

    if sLum == 'VI': sLum = fix_subDwarfs(sClass)

    # Fix yellow supergiants
    # Code will go in when rules are clarified

    # Fix dwarfs

    if sLum == 'D': sClass = ''

    # Fix Type O giants

    if sClass == 'O' and sLum in ['Ia', 'Ib', 'II'] and sClassDec <= 6: sLum = 'I'
                
    # Format the star string
    
    if sLum != 'D': starString = sClass + str(sClassDec) + ' ' + sLum
    else: starString = sLum + str(sClassDec)

    return starString

# Main, will eventually become test code

# Print the subsector header

print(FIXEDHEADER)

# Loop through the subsector hexes, checking for and if required generating mainworlds

for i in range(1, 9):
    for j in range(1, 11):

        starList = []

        # Format the location string

        loc = format(i, '02d') + format(j, '02d')

        # All worlds generated here are mainworlds

        isMainWorld = True

        # Determine system presence

        isPresent = gen_systemPresence(DISPERSED_DENSITY)
        
        if isPresent:
 
            sysPrimary = gen_systemObject(False)

            # First, always process the system primary, this processing will also determine the number of
            # companions to be generated
            
            # Generate spectral class, decimal and luminosity class for star systems
        
            if sysPrimary == 'Star System': 
                temp = gen_Primary(SC_SEMIREAL)
                starString = temp[0]
                nStars = temp[1]

                # Dwarfs don't have companions, override if needed

                if starString[0] == 'D': nStars = 1


            # Some primaries have been changed to brown dwarfs when generating spectral class
            # Update the primary type, format the star string if so and regenerate the number of objects
            # in the system

                if starString[0] in ['L', 'T', 'Y']:
                    sysPrimary = 'Brown Dwarf'
                    nStars = gen_numStars(starString[0])
                    


            # Process brown dwarfs

            elif sysPrimary == 'Brown Dwarf': 
                starString = gen_brownDwarfClass() + str(gen_sClassDecimal())
                nStars = gen_numStars(starString[0])    

            # Process black holes

            elif sysPrimary == 'Black Hole':
                nStars = gen_numStars(sysPrimary[0])
                starString = 'X'

            elif sysPrimary == 'Neutron Star':
                nStars = 1
                starString = 'NS'

            else: 
                nStars = 1
                starString = ''
                            
            # Add the star to the list of system stars
                
            starList.append(starString)
            outline = '{0: <14}'.format(sysPrimary) + loc
            
            # Ok, now that the primary is out of the way, loop through the companions

            objectNumber = 2
            while objectNumber <= nStars:
                # print('Companion generation ' + str(objectNumber) + ' for ' + starString)
                companionString = gen_Companion(sysPrimary)
                starList.append(companionString)

                objectNumber += 1
           
            # Generate the mainworld if needed

            # if sysPrimary == 'Star System':
            #     mw = TR_CE_SRD_World.World("Main-" + loc)
            #     mw.loc = loc
            #     mw.genWorld()
            #     mw.formatUWPString_text_SEC()
            #     outline = mw.UWPString
                

            # else: 
            #     tempstr = '{0: <14}'.format(sysPrimary) + loc + ' ----'
            #     outline = tempstr

            print('{0: <58}'.format(outline), end = '')
            for aStar in starList:
                print(aStar + ' ', end = '')
            print('\r')






