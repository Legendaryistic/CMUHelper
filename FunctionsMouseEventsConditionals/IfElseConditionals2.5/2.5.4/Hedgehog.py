app.background = 'cornflowerBlue'

spikes = Star(200, 335, 130, 30, fill='saddleBrown', roundness=80)

# body
Circle(140, 330, 15, fill='navajoWhite', border='tan', borderWidth=5)
Circle(260, 330, 15, fill='navajoWhite', border='tan', borderWidth=5)
Oval(200, 310, 160, 110, fill='tan', align='top')

# eyes
Circle(175, 360, 7)
Circle(225, 360, 7)

# nose
RegularPolygon(200, 390, 15, 3, rotateAngle=180)

leftEyebrow = Line(155, 345, 170, 345, rotateAngle=-15)
rightEyebrow = Line(245, 345, 230, 345, rotateAngle=15)

def drawAnimal(animal):
    if animal == 'porcupine':
        spikes.fill = gradient("saddleBrown","saddleBrown","saddleBrown", "tan")
        
    else:
        spikes.points = 60
        
    # Change the number of spikes if it is a hedgehog and the fill if it is not.
    ### Place Your Code Here ###
    pass

def onMousePress(mouseX, mouseY):
    if spikes.points != 60:
        spikes.radius = 250
        spikes.roundness = 40
       
    leftEyebrow.rotateAngle = 30
    rightEyebrow.rotateAngle = -30
    # Puff the spikes if it is a porcupine.
    # Change the eyebrows to make it disturbed.
    ### Place Your Code Here ###
    pass

def onMouseRelease(mouseX, mouseY):
    spikes.radius = 130
    spikes.roundness = 80
    leftEyebrow.rotateAngle = -15
    rightEyebrow.rotateAngle = 15
    # Change the puff and eyebrows back to the original state.
    ### Place Your Code Here ###
    pass
