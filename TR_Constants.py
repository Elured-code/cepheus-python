#
# Cepheus Engine constants
# 
#
# Author:   Michael Bailey
# Date:     6 August 2020
#

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

# Subsector generation constants

CSUM_DENSITY_MAP = {"EMPTY": 0, "SCATTERED": 20, "DISPERSED": 35, "AVERAGE": 50, "CROWDED": 60, "DENSE": 75}
DENSITY_VALUES = ["EMPTY", "RIFT", "SPARSE", "SCATTERED", "STANDARD", "DENSE"]
DENSITY_LOOKUP = {0: 0, 1: 4, 2: 18, 3: 33, 4: 50, 5: 66}
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

# non-star system types

NON_STARSYSTEMS = ['Brown Dwarf', 'Rogue Planet', 'Neutron Star', 'Black Hole', 'Stellar Nursery', 'Nebula', 'Anomaly']

# Stellar Class Realism

SC_REAL = 1
SC_SEMIREAL = 2
SC_FANTASTIC = 3