app.stars = [ ]
app.colorList = [ 'teal', 'black', 'midnightBlue', 'white', 'indigo' ]

def drawStars(numStars):
    colorIndex = 0
    width = 705

    # Run the following code numStars times to draw all of the rectangles.
    ### Fix Your Code Here ###
    for i in range(numStars):
        color = app.colorList[colorIndex]
        star = Star(200, 200, width, 5, fill=color)
        app.stars.append(star)
    
        colorIndex = (colorIndex + 1) % len(app.colorList)
        width -= (700 / numStars)

def onMousePress(mouseX, mouseY):
    indexStar = 0
    for x in app.stars:
        if indexStar % 2 == 0:
            x.rotateAngle += 5
        else:
            x.rotateAngle -= 5
        indexStar += 1
    # Rotate all of the the stars stored in app.stars. Every star at an
    # even index should rotate 5 degrees clockwise. The rest should rotate
    # counter-clockwise.
    ### Place Your Code Here ###
    pass

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawStars(100)
