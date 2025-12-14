app.background = 'black'

leftVolumeBar = Line(75, 300, 75, 400, lineWidth=100, dashes=True,
                     fill=gradient('black', 'red', 'orange', 'yellow',
                                   'lawnGreen', start='top'))
centerVolumeBar = Line(200, 300, 200, 400, lineWidth=100, dashes=True,
                       fill=gradient('black', 'red', 'orange', 'yellow',
                                     'lawnGreen', start='top'))
rightVolumeBar = Line(325, 300, 325, 400, lineWidth=100, dashes=True,
                      fill=gradient('black', 'red', 'orange', 'yellow',
                                    'lawnGreen', start='top'))

def setVolumeBars(newLeftBarY1, newCenterBarY1, newRightBarY1):
    
    # Set each volume bar to new y1 value.
    leftVolumeBar.y1 = newLeftBarY1
    centerVolumeBar.y1 = newCenterBarY1
    rightVolumeBar.y1 = newRightBarY1

def onMouseMove(mouseX, mouseY):
    if mouseX < 125:
        setVolumeBars(mouseY, 400-mouseY, 400 - mouseY)
    elif mouseX < 275:
        setVolumeBars(400-mouseY, mouseY, 400 - mouseY)
    else:
        setVolumeBars(400-mouseY, 400 - mouseY, mouseY)
    # Change the height of volume bars based on which volume bar the mouse is above.
    ### (HINT: The volume bars are set at either a height of mouseY or
    #          400 - mouseY.)
    ### Place Your Code Here ###
    pass
