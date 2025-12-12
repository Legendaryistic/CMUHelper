app.background = 'snow'

app.opacities = [ 100, 90, 70, 60, 50, 40, 30, 20, 20, 10, 10, 10, 10 ]

def drawPawPrint(x, y, opacity):
    Oval(x, y, 20, 16, fill='darkGray', opacity=opacity)
    Oval(x - 12, y - 8, 6, 8, fill='darkGray', opacity=opacity)
    Oval(x - 4, y - 14, 6, 8, fill='darkGray', opacity=opacity)
    Oval(x + 4, y - 14, 6, 8, fill='darkGray', opacity=opacity)
    Oval(x + 12, y - 8, 6, 8, fill='darkGray', opacity=opacity)

def onMousePress(mouseX, mouseY):
    for i in range(len(app.opacities)):
        drawPawPrint(mouseX + ((-1)**i*20), mouseY + 30*i, app.opacities[i])
    # For every value in the app.opacities list, draw a paw print with that opacity.
    # - The first paw print should be 20 pixels to the right of the mouse.
    # - The second should be 20 pixels left and 30 pixels down from the mouse.
    # - Each print after should alternate left and right and 30 pixels below the
    #   previous.
    ### (HINT: You can tell if a number i is even or odd by checking if i % 2
    #          is 0 or 1!)
    ### (HINT: We've provided a drawPawPrint function above.)
    ### Place Your Code Here ###
    pass
