app.background = gradient('white', 'silver', start='top')

def drawVeggie(width, height, color):
    # Draw the stem at the top of the veggie.
    ### (HINT: The top of the veggie has a y of 200 minus half the height!)
    ### Place Your Code Here ###
    
    Star(200,200-height/2,50,7,roundness=40,fill=gradient('green','lightGreen'))
    # Draw the veggie itself.
    ### Place Your Code Here ###
    Oval(200,200, width, height, fill=color)

    # This draws the veggie's face.
    Oval(225, 190, 55, 65, fill=gradient('white', 'white', 'gainsboro'))
    Oval(175, 190, 55, 65, fill=gradient('white', 'white', 'gainsboro'))
    Circle(225, 190, 10)
    Circle(175, 190, 10)
    Polygon(175, 230, 225, 230, 205, 250, 195, 250)

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawVeggie(200, 180, gradient('red', 'darkRed', start='left'))
