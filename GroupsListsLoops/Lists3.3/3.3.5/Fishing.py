app.background = 'royalBlue'
Rect(0, 0, 100, 400, fill='sandyBrown')

def drawFishingPole(yOffset):
    Line(50, yOffset + 80, 140, yOffset + 25, fill='maroon', lineWidth=4)
    Line(55, yOffset + 79, 65, yOffset + 73, lineWidth=8)
    Line(57, yOffset + 79, 64, yOffset + 74, fill='white', lineWidth=8)
    Line(65, yOffset + 73, 140, yOffset + 27, fill='white', lineWidth=1)
    Line(140, yOffset + 27, 315, yOffset + 80, fill='white', lineWidth=1)
    Circle(140, yOffset + 25, 2, fill='maroon')

def drawBite(yOffset):
    Oval(315, yOffset + 80, 40, 35, fill=None, border='midnightBlue')
    Oval(315, yOffset + 80, 30, 25, fill=None, border='midnightBlue')
    Oval(315, yOffset + 80, 20, 15, fill=None, border='midnightBlue')

def drawFishing(numberOfPoles, indexOfBite):
    centerY = 55
    drawBite((indexOfBite+1)*centerY)
    for i in range(1,numberOfPoles+1):
        drawFishingPole(centerY * (i))
    
    
    # Create numberOfPoles many fishing poles. Exactly one of the poles has a
    # bite, and is determined by the indexOfBite parameter. Draw the bite for
    # that pole.
    ### (HINT: Each fishing pole is drawn 55 pixels below the last.)
    ### (HINT: We've given you functions to draw both the poles and the bite.)
    ### Place Your Code Here ###
    

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawFishing(6, 0)
