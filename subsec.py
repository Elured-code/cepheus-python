#
# Cepheus Engine SRD with Extensions Subsector Generation
#
# Version:  0.2
# Author:   Michael Bailey
# Date:     23 July 2020
#

#
# This code generates an 8 x 10 subsector according to:
# 1. CE SRD system generation rules; and
# 2. Stellar data generation kludged together by myself with some quickly researched type/spectra
#    distribution

# 
# Run subsec.py -h for usage
#

#
# Things to do:
#
# 


import argparse
import random
import TR_CE_EXT_World
# import TR_CE_EXT_Stellar

# import sys

# print (str(sys.argv))

# Define common functions

# Dice rollers

def D100Roll():
    random.seed()
    return random.randint(1, 6) + random.randint(1, 101)

DENSITY_LOOKUP = {1: 4, 2: 18, 3: 33, 4: 50, 5: 66}

# Construct and parse command line arguments

parser = argparse.ArgumentParser(description='Generate a CE subsector', formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('name', help = 'Enter the name of the subsector to be generated')
parser.add_argument('-d', '--density', type=int, choices=[1, 2, 3, 4, 5], default=3, help='density value (1 = rift, 2 = sparse, 3 = scattered, 4 = standard, 5 = dense).', metavar='DENSITY')
parser.add_argument('-s', '--stellar', action = 'store_true', help= "Generate stellar data")
args = parser.parse_args()

print(args)

# Set the probability of system presence in any given hex

prob = DENSITY_LOOKUP.get(args.density)

# Print the header text

print(args.name)
print("....+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8")

# Loop through the subsector hexes, checking for and if required generating mainworlds
i = 1
while i <= 8:
    j = 1
    while j <= 10:   
        if D100Roll() < prob:
            loc = format(i, '02d') + format(j, '02d')
            # print(loc, end=" ")

            isMainWorld = True
            w1 = TR_CE_EXT_World.World("Main-" + loc, isMainWorld)
            w1.loc = loc
            w1.genWorld()
            w1.formatUWPString_text_SEC()
            
            print(f'{w1.UWPString}')
        j += 1
    i += 1
