app.background = 'lightSteelBlue'

def drawIceCream(iceCreamFlavorList):
    # ice cream cone
    Polygon(175, 290, 225, 290, 200, 360, fill='peru')

    # This stores the centerY of the next ice cream scoop.
    centerY = 275

    # Loop through the colors in the iceCreamFlavorList and draw each scoop onto
    # the cone.
    ### (HINT: The centerY of the ice cream scoops decrease by 25 on each
    #          loop iteration.)
    ### Fix Your Code Here ###
    for color in iceCreamFlavorList:
        Circle(200, centerY, 30, fill=color)
        centerY -= 25

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawIceCream([ 'saddleBrown', 'pink', 'snow' ])
