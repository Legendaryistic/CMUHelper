app.background = 'black'
app.stepsPerSecond = 20

Label('Click on the canvas to add stars.', 200, 15, fill='white', size=18)
Label('Press left arrow key to undo.', 200, 35, fill='white', size=18)
Label('Press right arrow key to redo.', 200, 55, fill='white', size=18)

app.stars = [ ]
app.removedStars = [ ]
app.colors = [ 'fuchsia', 'yellow', 'aqua', 'lawnGreen', 'ghostWhite' ]
app.colorIndex = 0

def undo():
    if len(app.stars) != 0:
        app.stars[-1].visible = False
        app.removedStars.append(app.stars.pop())
    # Pop the last star from app.stars and add it to app.removedStars.
    # Also make it invisible.
    ### (HINT: Make sure that there is a star to remove!)
    ### Place Your Code Here ###
    pass

def redo():
    if len(app.removedStars) != 0:
        app.removedStars[-1].visible = True
        app.stars.append(app.removedStars.pop())
    # Pop the last star from app.removedStars and add it to app.stars.
    ### (HINT: Make sure that there is a star to add back!)
    ### Place Your Code Here ###
    pass

def onMousePress(mouseX, mouseY):
    # Adds a star with the next color at the mouse press location.
    color = app.colors[app.colorIndex]
    app.stars.append(
        Star(mouseX, mouseY, 35, 5, fill=None, border=color, borderWidth=4,
             roundness=60)
        )

    # Updates what the next color will be.
    app.colorIndex += 1
    if (app.colorIndex == len(app.colors)):
        app.colorIndex = 0

def onKeyPress(key):
    if key == 'left':
        undo()
    elif key == 'right':
        redo()
    # Undo when the left key is pressed. Redo when the right key is pressed.
    ### Place Your Code Here ###
    pass
