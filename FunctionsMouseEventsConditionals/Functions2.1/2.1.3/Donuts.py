# background
Rect(0, 0, 400, 400, fill='honeydew')

def drawDonut(centerX, centerY, donutColor, frostingColor):
    # Change the color of the donut and the frosting to use the function's
    # parameters.
    ### Fix Your Code Here ###
    Circle(centerX, centerY, 80, fill=donutColor)
    Star(centerX, centerY, 75, 15, fill=frostingColor, roundness=90)

    # Draw the donut hole.
    ### Place Your Code Here ###
    Circle(centerX,centerY,20,fill = 'honeydew')

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawDonut(200, 200, 'wheat', 'hotPink')
