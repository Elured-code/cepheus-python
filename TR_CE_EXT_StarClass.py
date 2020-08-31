#
# Cepheus Engine Extended - Star Class
#
# About:
#
# This class holds data for a single star or other object in a system

#
# Version:  0.1
# Author:   Michael Bailey
# Date:     20 August 2020
#

# Imports

import sys
from tinydb import TinyDB, Query




# Local constants

ALLOWED_SPECTRAL_CLASSES = ['O', 'B', 'A', 'F', 'G', 'K', 'M', 'T', 'L', 'Y']
ALLOWED_LUMINOSITY_CLASSES = ['I', 'Ia', 'Ib', 'II', 'III', 'IV', 'V', 'VI', 'D', 'BD', 'Neutron Star', 'Black Hole', 
    'Stellar Nursery', 'Nebula', 'Rogue Planet']



class Star:

# Setters and getters
    
    @property
    def spectralClass(self):
        return self.__spectralClass

    @property
    def luminosityClass(self):
        return self.__luminosityClass

    @property
    def starMass(self):
        return self.__starMass

    @property
    def starLuminosity(self):
        return self.__starLuminosity

    @property
    def starDiameter(self):
        return self.__starDiameter

    @property
    def starRocheLimit(self):
        return self.__starRocheLimit

    @property
    def starHZone(self):
        return self.__starHzone

    @property
    def starFrostLine(self):
        return self.__starFrostLine

    @property
    def starOuterLimit(self):
        return self.__starOuterLimit

    @spectralClass.setter
    def spectralClass(self, spectralClass):

        # Check for valid classes and throw an exception if not found
        # May put more validation in here later

        # if spectralClass[0] != '' and spectralClass[0] not in ALLOWED_SPECTRAL_CLASSES:
        #     raise ValueError('Invalid spectral class ' + spectralClass[0])
        # elif len(spectralClass) >1 and spectralClass[1] != '' and int(spectralClass[1]) not in range(0, 11):
        #     raise ValueError('Invalid spectral class decimal ' + spectralClass[1])
        # else: self.__spectralClass = spectralClass

        self.__spectralClass = spectralClass
    
    @luminosityClass.setter
    def luminosityClass(self, luminosityClass):

        # Once again check for valid values

        # if luminosityClass != '' and luminosityClass not in ALLOWED_LUMINOSITY_CLASSES:
        #     raise ValueError('Invalid luminosity class ' + luminosityClass)
        # else: self.__luminosityClass = luminosityClass

        self.__luminosityClass = luminosityClass

    @starMass.setter
    def starMass(self, starMass):
        self.__starMass = starMass

    @starLuminosity.setter
    def starLuminosity(self, starLuminosty):
        self.__starLuminosity = starLuminosty

    @starMass.setter
    def starMass(self, starMass):
        self.__starMass = starMass

    @starDiameter.setter
    def starDiameter(self, starDiameter):
        self.__starDiameter = starDiameter

    @starRocheLimit.setter
    def starRocheLimit(self, starRocheLimit):
        self.__starRocheLimit = starRocheLimit

    @starHZone.setter
    def starHZone(self, starHZone):
        self.__starHZone = starHZone

    @starFrostLine.setter
    def starFrostLine(self, starFrostLine):
        self.__starFrostLine = starFrostLine

    @starOuterLimit.setter
    def starOuterLimit(self, starOuterLimit):
        self.__starOuterLimit = starOuterLimit

# Initialiser

    def __init__(self, sClass, sLum):
        self.spectralClass = sClass
        self.luminosityClass = sLum


# Query the star database to get relevant values

    def get_starDetails(self, Class, Lum):
        rd = {}
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

# Test Code

try:
    s1 = Star('F7', 'V')


    st = s1.get_starDetails(s1.spectralClass, s1.luminosityClass)

    print(st['mass'])

except ValueError as e:
    print(repr(e))
    exc_type, exc_value, tb = sys.exc_info()
    if tb is not None:
        prev = tb
        curr = tb.tb_next
        while curr is not None:
            prev = curr
            curr = curr.tb_next
        print(prev.tb_frame.f_locals)

