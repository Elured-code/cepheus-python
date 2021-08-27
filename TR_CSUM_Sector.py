import random
import TR_Constants
import TR_Support


class stellarHex:

    stars = []

    def __init__(self, *args):
        if not args: self.objectPresent = False
        else: self.objectPresent = args[0]
        
    
    def checkSystemPresence(self, subsectorType):
        if subsectorType in TR_Constants.CSUM_DENSITY_MAP:
            x = TR_Support.D100Roll()
            y = TR_Constants.CSUM_DENSITY_MAP[subsectorType]
            if x <= y: returnBoolean = True
            else: returnBoolean = False
            return returnBoolean
        else:
            print("ERROR:  Invalid Subsector Type")
            exit(8)

            

    
thisHex = stellarHex(False)

print(thisHex.checkSystemPresence("SCATTERED"))


