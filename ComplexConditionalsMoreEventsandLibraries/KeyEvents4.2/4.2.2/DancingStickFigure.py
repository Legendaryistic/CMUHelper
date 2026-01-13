app.background = gradient('azure', 'lightBlue', 'blue')

# face and body
Circle(200, 135, 25)
Line(200, 160, 200, 240)
Label(')', 203, 145, fill='white', size=20, rotateAngle=90, bold=True)
Circle(190, 130, 3, fill='white')
Circle(210, 130, 3, fill='white')

# upper arms
leftArm = Line(200, 185, 150, 175)
rightArm = Line(200, 185, 250, 175)

# legs
Line(200, 240, 230, 300)
Line(200, 240, 170, 300)

def toggleLeftArm():
    if leftArm.y2 != 175:
        leftArm.y2 = 175
    else:
        leftArm.y2 = 125
    # Move the left arm down if currently up, up if down.
    ### (HINT: Use the y2 value to check the arm position and modify it.)
    ### Place Your Code Here ###
    pass

def toggleRightArm():
    if rightArm.y2 != 175:
        rightArm.y2 = 175
    else:
        rightArm.y2 = 125
    # Move the right arm down if currently up, up if down.
    ### Place Your Code Here ###
    pass

def onKeyPress(key):
    if key == 'left':
        toggleLeftArm()
    elif key == 'right':
        toggleRightArm()
    # On left and right key press, call the corresponding helper function.
    ### Place Your Code Here ###
    pass
