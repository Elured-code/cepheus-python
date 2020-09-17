#
# Cepheus Engine Subsector Generation
#
# About:
#
# This script generates a CE SRD subsector and outputs to text, and alternatively
# JSON and PNG files
#

#
# Version:  0.1
# Author:   Michael Bailey
# Date:     17 September 2020
#

# Usage
#
# usage: TR_CE_Create_SubsecFiles.py [-h] [--sector SECTOR] [--letter {A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P}] [--density {RIFT,SPARSE,SCATTERED,STANDARD,DENSE}] [-p] [-j] [-n] name

# Generate a CE SRD subsector

# positional arguments:
#   name                  Subsector Name

# optional arguments:
#   -h, --help            show this help message and exit
#   --sector SECTOR       Parent Sector Name (default: Placeholder)
#   --letter {A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P}
#                         Subsector Letter (default: A)
#   --density {RIFT,SPARSE,SCATTERED,STANDARD,DENSE}
#                         subsector density (default: STANDARD)
#   -p, --writepng        Write the subsector data to a PNG file
#   -j, --writejson       Write the subsector data to a JSON file
#   -n, --nonames         Do not add mainworld names to the PNG file

# Import modules here

# Python modules

import argparse
import sys

# App modules

import TR_Constants
import TR_Support
import TR_CE_Subsector
import TR_Imaging

# Parse command line arguments

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    Generate a CE SRD subsector 
    """)
    parser.add_argument("name", default='subsec', help="Subsector Name")
    parser.add_argument("--sector", default='Placeholder', help="Parent Sector Name (default: %(default)s)")
    parser.add_argument("--letter", \
        choices=TR_Constants.SUBSECLETTERS, \
        default = 'A', help="Subsector Letter (default: %(default)s)")
    parser.add_argument("--density", \
        choices=TR_Constants.DENSITY_VALUES, \
        default = 'STANDARD', help="subsector density (default: %(default)s)")
    parser.add_argument("-p", "--writepng", action="store_true", \
        help="Write the subsector data to a PNG file")
    parser.add_argument("-j", "--writejson", action="store_true", \
        help="Write the subsector data to a JSON file")
    parser.add_argument("-n", "--nonames", action="store_true", \
        help="Do not add mainworld names to the PNG file")

# Process the arguments

args = parser.parse_args()
ARG_NAME    = args.name
ARG_SECTOR  = args.sector
ARG_LETTER  = args.letter
ARG_DENSITY = args.density
ARG_JSON    = args.writejson
ARG_PNG     = args.writepng
ARG_NONAMES  = args.nonames

# Convert density values to integers for lookup

stellarDensity = TR_Constants.DENSITY_VALUES.index(ARG_DENSITY)


# Create and generate the subsector
# Parameters will be eventually available as command line arguments

print("Generating " + ARG_NAME + " Subsector (" + ARG_SECTOR + "/" + ARG_LETTER + ")")
print("Stellar Density = " + ARG_DENSITY)
print()

s1 = TR_CE_Subsector.Subsector(ARG_NAME, ARG_SECTOR, ARG_LETTER, stellarDensity, 3)
s1.genSubSec()
print("```")
s1.printSubSec()
print("```")

# Write to an output SEC file - once again this will be passed by a command line argument in the future

print("Writing subsector data to " + ARG_NAME + ".uwp")
with open("subsec.uwp", 'w', encoding='utf-8') as f: f.write(s1.writeSubSec())

if ARG_JSON:
    print("Writing subsector data to " + ARG_NAME + ".json")
    with open("subsec.json", 'w', encoding='utf-8') as j: j.write(s1.writeSubSecJSON())

if ARG_PNG:
    addnames = not ARG_NONAMES
    pngfile = ARG_NAME + ".png"
    print("Writing subsector data to " + pngfile)
    TR_Imaging.drawHexMap(s1, pngfile, addnames)


