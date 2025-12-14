# background
Line(200, 0, 200, 400, fill='steelBlue', lineWidth=400, opacity=40,
     dashes=(2, 23))
Line(50, 0, 50, 400, fill='crimson', opacity=60)

def stickFigure(x, y, size):
    # The parameters (x, y) is where where the head and body of the stick figure
    # meet.

    # head
    Circle(x, y - size, size)

    # Draw the stick figure's body, and arms. We have drawn the head and legs
    # for you.
    ### Place Your Code Here ###
    Line(x,y,x,y+size*2,lineWidth=2)
    Line(x-size,y,x,y+size, lineWidth = 2)
    Line(x,y+size,x+size,y,lineWidth = 2)
    # legs
    Line(x, y + 2 * size, x - size, y + 3 * size)
    Line(x, y + 2 * size, x + size, y + 3 * size)

##### Place your code above this line, code below is for testing purposes #####
# test case:
stickFigure(200, 200, 25)
