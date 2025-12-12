app.background = gradient('sienna', 'chocolate')

Line(35, 200, 365, 200, fill='sienna', lineWidth=400, dashes=(30, 70))

def drawCabbage(x, y):
    cabbage = Group(
        Star(200, 200, 30, 8, fill='seaGreen', rotateAngle=30, roundness=80),
        Star(200, 200, 25, 8, fill='mediumSeaGreen', rotateAngle=50, roundness=80),
        Star(200, 200, 18, 8, fill='paleGreen', rotateAngle=70, roundness=80)
        )
    cabbage.centerX = x
    cabbage.centerY = y

def drawCabbages():
    for i in range(8):
        for j in range(5):
            drawCabbage(0 + j*100, 0+i*55)
    # Draw 8 rows of cabbages, each with 5 cabbages using a for loop. In each loop
    # you should manually draw 5 cabbages (1 per column). They should all be 100
    # pixels apart horizontally, 55 pixels apart vertically.
    ### (HINT: You should only need to write 5 calls to drawCabbage()!)
    ### Place Your Code Here ###
    pass

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawCabbages()
