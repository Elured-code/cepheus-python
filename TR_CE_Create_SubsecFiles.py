import sys

import TR_Constants
import TR_Support
import TR_CE_Subsector
import TR_Imaging

# Create and generate the subsector
# Parameters will be eventually available as command line arguments



s1 = TR_CE_Subsector.Subsector("TestSub", "TestSec", "B", 3, 5)
s1.genSubSec()
print("```")
s1.printSubSec()
print("```")

# Write to an output SEC file - once again this will be passed by a command line argument in the future

with open("subsec.uwp", 'w', encoding='utf-8') as f: f.write(s1.writeSubSec())
with open("subsec.json", 'w', encoding='utf-8') as j: j.write(s1.writeSubSecJSON())
TR_Imaging.drawHexMap(s1, "subsec.png")


