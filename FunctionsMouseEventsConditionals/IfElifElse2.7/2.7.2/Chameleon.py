# background
Rect(0, 0, 200, 400, fill='blueViolet', opacity=70)
Rect(200, 0, 200, 400, fill='limeGreen', opacity=50)

chameleon = Polygon(215, 170, 235, 130, 250, 145, 280, 110, 330, 105, 360, 135,
                    370, 175, 350, 230, 330, 220, 320, 200,  345, 215, 335,
                    175, 250, 175, 240, 180, fill='limeGreen')

def onMousePress(mouseX, mouseY):
    chameleon.centerX = mouseX
    chameleon.centerY = mouseY
    
    if chameleon.centerX < 150:
        chameleon.fill = 'blueViolet'
    elif 250<chameleon.centerX:
        chameleon.fill = 'limeGreen'
    else:
        chameleon.fill = gradient('blueViolet', 'limeGreen', start = 'left')
        # Move the chameleon to the location of your mouse click.
    ### Place Your Code Here ###
    

    # Change the fill of chameleon based on mouseX value.
    ### (HINT: Use conditionals!)
    ### Place Your Code Here ###
    pass
