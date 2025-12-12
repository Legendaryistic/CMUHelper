app.background = gradient(rgb(25, 25, 180), rgb(25, 25, 80), start='right-top')

Star(350, 50, 53, 500, fill='maroon')
Star(350, 50, 28, 500, roundness=90)
Rect(0, 365, 400, 135, fill='seaGreen')

mist = Group(
    Star(150, 345, 50, 600, opacity=40, fill='white'),
    Star(175, 351, 48, 600, opacity=30, fill='white'),
    Star(200, 350, 52, 600, opacity=30, fill='white'),
    Star(225, 347, 47, 600, opacity=30, fill='white'),
    Star(250, 353, 51, 600, opacity=40, fill='white')
    )
mist.width = 600

pyramid = Group()

def drawPyramid(blockHeight):
    # Draw the layers leading up to the top of the pyramid.
    ### (HINT: Each layer should have a height of blockHeight.)
    ### Place Your Code Here ###
    for i in range(8):
        pyramid.add(Rect(0,350- (blockHeight * i),350-(i*30),blockHeight, fill = gradient('saddleBrown', 'darkGoldenrod', start = 'top'), border = 'black', borderWidth = 1))
    # Chamber at the top of the pyramid
    Rect(0, pyramid.top - 40, 100, 40,
         fill=gradient('saddleBrown','darkGoldenrod', start='top'),
         border='black', borderWidth=1)
    Rect(0, pyramid.top - 30, 100, 6, fill=None, border='black')
    Rect(0, pyramid.top - 15, 40, 15)

    # Staircase
    Polygon(-5, 380, -5, pyramid.top, 55, pyramid.top, 130, 380,
            fill=gradient('sienna', 'goldenrod', start='top'), border='black')

    mist.toFront()

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawPyramid(30)
