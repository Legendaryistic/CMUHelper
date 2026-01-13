app.background = gradient('midnightBlue', 'royalBlue', start='top')

Rect(50, 10, 300, 380, fill=gradient('whiteSmoke', 'white', start='top'))
essay = Line(200, 20, 200, 30, lineWidth=250, dashes=True)

pageNumber = Label(1, 335, 375, size=20)

def onKeyPress(key):
    essay.y2 += 10
    if essay.y2 + 10 == 400:
        pageNumber.value += 1
        essay.y2 = 30
        
    pass
    
