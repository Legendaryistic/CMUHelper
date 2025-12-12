app.background = 'azure'

app.colors = [ 'mediumVioletRed', 'chocolate', 'limeGreen', 'dodgerBlue' ]
app.index = 0

balloons = Group()

def drawCircularBalloon(cx, cy, color):
    balloon = Group(
        Line(200, 200, 200, 300, fill='gainsboro'),
        Oval(200, 200, 60, 70, fill=color),
        Circle(200, 235, 4, fill=color)
        )
    balloon.centerX = cx
    balloon.centerY = cy
    balloons.add(balloon)

def drawSquareBalloon(cx, cy, color):
    balloon = Group(
        Line(200, 200, 200, 300, fill='gainsboro'),
        Rect(200, 200, 60, 60, fill=color, align='center'),
        Circle(200, 235, 4, fill=color)
        )
    balloon.centerX = cx
    balloon.centerY = cy
    balloons.add(balloon)

def onMousePress(mouseX, mouseY):
        
    # Get a color for the balloon from the app.colors list. There is also an
    # app.index custom property that tracks which color should be picked.
    ### Place Your Code Here ###
    app.color = app.colors[app.index]
    # Now draw the balloon using the color you just got. Every second balloon
    # should be square.
    ### (HINT: We have created two functions above that draw the two different
    #          balloon shapes.)
    ### Place Your Code Here ###
    if app.index % 2 == 0:
        drawCircularBalloon(mouseX, mouseY, app.color)
    else:
        drawSquareBalloon(mouseX, mouseY, app.color)

    # Updates the current index for the next time we press the mouse.
    app.index += 1
    app.index = app.index % 4
