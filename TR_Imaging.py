

import math
import testTR_Subsector
import TR_Constants
from pathlib import Path

try:
    import wx.lib.wxcairo as wxcairo
    import cairo
    haveCairo = True
except ImportError:
    haveCairo = False

def drawHexMap(subsector, filename):      
    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, 600, 840)
    ctx = cairo.Context(ims)

    # print(ims.get_width())
    # print(ims.get_height())

    # Set a background color
    ctx.save()
    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.paint()
    ctx.restore()
    



    
    # Write out a hex map

    # Draw the hex grid

    i = 1
    j = 1

    # Determine the hex size parameters from the radius

    HEXRAD = 22
    width = HEXRAD * 2
    height = width * math.sqrt(3) * 0.5

    for i in range(1, 9):
        for j in range(1, 11):

            # Find the horizontal centre

            centrex = ((3 * i) - 1) * width/2 + 20
            centrey = ((2 * j) - 1) * height + 20

            # Add offsets to allow for space at the sides

            # centrex += (width/2)
            # centrey += (height/2)

            # Every second column will be offset by half a hex

            if i % 2 == 0: centrey += height

            # Round to integer values

            # centrex = round(centrex, 0)
            # centrey = round(centrey, 0)

            # Now create the hexagon

            # First, define each vertex in the hex

            hexagon = []
            for a in range(1, 7):
                point = []

                angle_deg = 60 * a - 60
                angle_rad = math.pi / 180 * angle_deg
                pointx = centrex + width * math.cos(angle_rad)
                pointy = centrey + width * math.sin(angle_rad)

                # Add the vertices' x and y coords to the point list
                # Round and cast to integer as implicit conversion is deprecated

                point.append(pointx)
                point.append(pointy)

                # Add each point to the hexagon list

                hexagon.append(point)

            # Now draw the hexagon onto the graphics context

            ctx.set_source_rgba(0.7, 0.7, 0.7)
            ctx.set_line_width(1.5)            

            # Move to the first point and draw the sides

            ctx.move_to(hexagon[0][0], hexagon[0][1])
            ctx.line_to(hexagon[1][0], hexagon[1][1])
            ctx.line_to(hexagon[2][0], hexagon[2][1])
            ctx.line_to(hexagon[3][0], hexagon[3][1])
            if i == 1 or j == 1: ctx.line_to(hexagon[4][0], hexagon[4][1])
            else: ctx.move_to(hexagon[4][0], hexagon[4][1])
            if j == 1 or j == 1: ctx.line_to(hexagon[5][0], hexagon[5][1])
            else: ctx.move_to(hexagon[5][0], hexagon[5][1])
            if i == 8 or j == 1: ctx.line_to(hexagon[0][0], hexagon[0][1])
            else: ctx.move_to(hexagon[0][0], hexagon[0][1])
            ctx.close_path()



            ctx.stroke()

            # Draw hex location labels

            ctx.select_font_face("Sans", cairo.FONT_SLANT_ITALIC,
            cairo.FONT_WEIGHT_NORMAL)
            ctx.set_font_size(9)
        
            loclabel = str(i).zfill(2) + str(j).zfill(2)
            xbearing, ybearing, twidth, theight, dx, dy = ctx.text_extents(loclabel)

            ctx.move_to(centrex - twidth/2, centrey - HEXRAD *1.25)

            ctx.show_text(loclabel)
            ctx.stroke()

            # Add a line on the bottom left and top right corners

            # Get the start and end points from the relevant hexes

            # Bottom left

            if i == 1 and j == 10:
                c1x = hexagon[2][0]
                c1y = hexagon[2][1]
                c2x = int(round(hexagon[2][0] - width/2, 0))
                c2y = int(round(hexagon[2][1] + height, 0))

            # Top right

            if i == 8 and j == 1:
                c3x = hexagon[5][0]
                c3y = hexagon[5][1]
                c4x = int(round(hexagon[5][0] + width/2, 0))
                c4y = int(round(hexagon[5][1] - height, 0))
                    
    # Draw the lines

    ctx.move_to(c1x, c1y)
    ctx.line_to(c2x, c2y)
    ctx.move_to(c3x, c3y)
    ctx.line_to(c4x, c4y)

    ctx.stroke()    
    
    # Draw a rectangle with no fill to contain the hex map

    ctx.set_line_width(4) 
    ctx.rectangle(c2x, c4y, c4x-c2x, c2y-c4y) 
    ctx.stroke()

    for world in subsector.contents:
        # print(world.starList)

        # Extract the world coordinates from the location field

        i = int(world.loc[:2])            
        j = int(world.loc[2:])

        # print(world.loc, end='')

        # Determine the hex centre point for the world

        centrex = ((3 * i) - 1) * width/2 + 20
        centrey = ((2 * j) - 1) * height + 20

        # print('-' + str(i) + ' ' + str(j) + '-', end='')

        # Add offsets to allow for space at the sides

        # centrex += (width/2)
        # centrey += (height/2)

        # add the vertical offset for every second column

        if i % 2 == 0: centrey += height




        # Display the mainworld name

        if world.worldname not in TR_Constants.NON_STARSYSTEMS:

            
            # Set the text font for the Starport data

            ctx.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
                cairo.FONT_WEIGHT_BOLD)
            ctx.set_source_rgb(1, 0, 0)
            ctx.set_font_size(12)

            # Get the starting point for the starport and show the world value

            xbearing, ybearing, twidth, theight, dx, dy = ctx.text_extents(world.starPort)
            ctx.move_to(centrex - dx/2, centrey - HEXRAD + theight)
            ctx.show_text(world.starPort)
            ctx.stroke()

            # Draw the world circle.  Will be extended to display the appropriate icon
            
            # If the mainworld siz = 0 then use a dashed line
            if world.siz == 0: 
                ctx.set_dash([2, 3])
                ctx.set_source_rgb(0, 0, 0)
                ctx.set_line_width(4)
            else: 
                ctx.set_dash([1, 0])
                ctx.set_line_width(1)
            ctx.set_source_rgba(0.6, 0.6, 0.6)
            ctx.arc(centrex, centrey, HEXRAD/3, 0, 2*math.pi)

            # If the world has free water fill the circle

            if world.hyd >= 1 and world.atm not in ['A', 'B', 'C']:
                ctx.set_source_rgb(0, 0, 0.5)
                ctx.fill()

            # ctx.set_line_width(1)

            ctx.stroke()

            xbearing, ybearing, twidth, theight, dx, dy = ctx.text_extents(world.worldname)
            ctx.move_to(centrex - dx/2, centrey + HEXRAD + theight)
            ctx.set_source_rgb(0.4, 0.4, 0.4)
            namelabel = world.worldname
            if world.pop >= 9: namelabel = namelabel.upper()
            
            ctx.show_text(namelabel)
            ctx.stroke()        
        
            # Display gas giants if present

            if world.nGiants > 0 :

                ctx.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
                    cairo.FONT_WEIGHT_NORMAL)
                ctx.set_font_size(10)
                ctx.move_to(centrex + HEXRAD*0.8, centrey - HEXRAD*0.8)
                ctx.show_text('G')
                ctx.stroke()

            # Display bases if present

            if world.bCode != " ":

                ctx.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
                    cairo.FONT_WEIGHT_NORMAL)
                ctx.set_font_size(10)
                ctx.move_to(centrex + HEXRAD*0.8, centrey + HEXRAD*0.8)
                ctx.show_text(world.bCode)
                ctx.stroke()  

        # Draw Brown Dwarf iconography

        elif world.worldname == 'Brown Dwarf':

            # Add the Brown Dwarf symbol

            ctx.set_line_width(1) 
            ctx.set_source_rgba(0.7, 0.2, 0.2)
            ctx.arc(centrex, centrey, HEXRAD/5, 0, 2*math.pi)
            ctx.fill()
            ctx.stroke()

            # Now add the label
            bdlabel = 'BD'
            ctx.select_font_face("Sans", cairo.FONT_SLANT_ITALIC,
                cairo.FONT_WEIGHT_NORMAL)
            ctx.set_source_rgb(0, 0, 0)
            ctx.set_font_size(10)
            xbearing, ybearing, twidth, theight, dx, dy = ctx.text_extents(bdlabel)

            ctx.move_to(centrex + HEXRAD/1.5, centrey + theight/2)
            ctx.set_source_rgb(0.4, 0.4, 0.4)  
            ctx.show_text(bdlabel)        
            ctx.stroke()  

        elif world.worldname == 'Rogue Planet':

            # Add the Rogue symbol

            ctx.set_line_width(1) 
            ctx.set_source_rgba(0.7, 0.7, 0.7)
            ctx.arc(centrex, centrey, HEXRAD/5, 0, 2*math.pi)

            ctx.stroke()

            # Now add the label
            bdlabel = 'RP'
            ctx.select_font_face("Sans", cairo.FONT_SLANT_ITALIC,
                cairo.FONT_WEIGHT_NORMAL)
            ctx.set_source_rgb(0, 0, 0)
            ctx.set_font_size(10)
            xbearing, ybearing, twidth, theight, dx, dy = ctx.text_extents(bdlabel)

            ctx.move_to(centrex + HEXRAD/1.5, centrey + theight/2)
            ctx.set_source_rgb(0.4, 0.4, 0.4)  
            ctx.show_text(bdlabel)        
            ctx.stroke()  

        elif world.worldname == 'Neutron Star':

            # Add neutron star symbol

            ctx.set_line_width(1) 
            ctx.set_source_rgba(0.3, 0.3, 0.3)
            ctx.arc(centrex, centrey, HEXRAD/5, 0, 2*math.pi)
            ctx.stroke()
            ctx.move_to(centrex, centrey - HEXRAD/4)
            ctx.line_to(centrex, centrey + HEXRAD/4)

            # Now add the label
            bdlabel = 'n'
            ctx.select_font_face("Sans", cairo.FONT_SLANT_ITALIC,
                cairo.FONT_WEIGHT_NORMAL)
            ctx.set_source_rgb(0, 0, 0)
            ctx.set_font_size(10)
            xbearing, ybearing, twidth, theight, dx, dy = ctx.text_extents(bdlabel)

            ctx.move_to(centrex + HEXRAD/1.5, centrey + theight/2)
            ctx.set_source_rgb(0.4, 0.4, 0.4)  
            ctx.show_text(bdlabel)        
            ctx.stroke()   
        
        elif world.worldname == 'Black Hole':

            # Add black hole symbol

            ctx.set_source_rgba(0, 0, 0, 1)
            ctx.set_line_width(1) 
            ctx.move_to(centrex - HEXRAD/2, centrey)
            ctx.line_to(centrex + HEXRAD/2, centrey)
            ctx.stroke()
            ctx.set_source_rgba(0.3, 0.3, 0.3)
            ctx.arc(centrex, centrey, HEXRAD/4, 0, 2*math.pi)
            ctx.fill()
            ctx.arc(centrex, centrey, HEXRAD/3, 0, 2*math.pi)
            ctx.stroke()


            # Now add the label
            bdlabel = '\u03A9'
            ctx.select_font_face("Sans", cairo.FONT_SLANT_ITALIC,
                cairo.FONT_WEIGHT_NORMAL)
            ctx.set_source_rgb(0, 0, 0)
            ctx.set_font_size(10)
            xbearing, ybearing, twidth, theight, dx, dy = ctx.text_extents(bdlabel)

            ctx.move_to(centrex + HEXRAD/1.5, centrey + theight/2)
            ctx.set_source_rgb(0.4, 0.4, 0.4)  
            ctx.show_text(bdlabel)        
            ctx.stroke()  

        elif world.worldname == 'Anomaly':

           # Add anomaly symbol


            ctx.set_line_width(1) 
            ctx.set_source_rgba(0.7, 0, 0, 1)
            ctx.arc(centrex, centrey, HEXRAD/5, 0, 2*math.pi)
            ctx.fill()
            ctx.stroke()      
   


            # Now add the label
            bdlabel = '?'
            ctx.select_font_face("Sans", cairo.FONT_SLANT_ITALIC,
                cairo.FONT_WEIGHT_NORMAL)
            ctx.set_source_rgb(0, 0, 0)
            ctx.set_font_size(10)
            xbearing, ybearing, twidth, theight, dx, dy = ctx.text_extents(bdlabel)

            ctx.move_to(centrex + HEXRAD/1.5, centrey + theight/2)
            ctx.set_source_rgb(0.4, 0.4, 0.4)  
            ctx.show_text(bdlabel)        
            ctx.stroke()    

        elif world.worldname in ['Nebula', 'Stellar Nursery']:

            # Now add the label
            if world.worldname == 'Stellar Nursery': bdlabel = 'STL NURSERY' 
            else: bdlabel = 'NEBULA'
            ctx.select_font_face("Sans", cairo.FONT_SLANT_ITALIC,
                cairo.FONT_WEIGHT_NORMAL)
            ctx.set_source_rgb(0, 0, 0)
            ctx.set_font_size(10)
            xbearing, ybearing, twidth, theight, dx, dy = ctx.text_extents(bdlabel)

            ctx.move_to(centrex - twidth/2, centrey + theight/2)
            ctx.set_source_rgb(0.4, 0.4, 0.4)  
            ctx.show_text(bdlabel)        
            ctx.stroke()   

            width = HEXRAD * 2
            height = width * math.sqrt(3) * 0.5

            # print(width, height)

            hexagon = []
            for a in range(1, 7):
                point = []

                angle_deg = 60 * a - 60
                angle_rad = math.pi / 180 * angle_deg
                pointx = centrex + (width * math.cos(angle_rad))
                pointy = centrey + (width * math.sin(angle_rad))

                # Add the vertices' x and y coords to the point list
                # Round and cast to integer as implicit conversion is deprecated

                point.append(pointx)
                point.append(pointy)

                # print(centrex, centrey, point)

                # Add each point to the hexagon list

                hexagon.append(point)

            # Now draw the hexagon onto the graphics context           

            # Move to the first point and draw the sides
 
            ctx.set_source_rgba(0, 0, 0, 0.2)
            ctx.move_to(hexagon[0][0], hexagon[0][1])
            ctx.line_to(hexagon[1][0], hexagon[1][1])
            ctx.line_to(hexagon[2][0], hexagon[2][1])
            ctx.line_to(hexagon[3][0], hexagon[3][1])
            ctx.line_to(hexagon[4][0], hexagon[4][1])
            ctx.line_to(hexagon[5][0], hexagon[5][1])
            ctx.line_to(hexagon[0][0], hexagon[0][1])
            
            ctx.close_path() 
            ctx.fill()   
            ctx.stroke()     




        ctx.set_source_rgba(0.7, 0.7, 0.7)



    ims.write_to_png(str(filename))

def genSubSec():

    subsector = testTR_Subsector.Subsector("CEEX", "TestSub", "TestSec", "B", 4)
    subsector.genSubSec()
    for world in subsector.contents:
        if world.worldname in TR_Constants.NON_STARSYSTEMS : 
            print(world.worldname + ' ', end = '')
            print(world.loc)
    return subsector



def main():

    for i in range(1, 5): 
        thissubsec = genSubSec() 
        filename = Path("c:/temp/image" + f'{i:03d}' + ".png")
        # open(filename, "w").close()
        drawHexMap(thissubsec, filename)
        print('Writing ', end='')
        print(filename)
    
    

        
        
if __name__ == "__main__":    
    main()