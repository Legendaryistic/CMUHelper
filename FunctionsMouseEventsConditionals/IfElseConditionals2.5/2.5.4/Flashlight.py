# background
Rect(0, 0, 400, 400)

def turnOnFlashlight(intensity):
    # Check how large intensity is.
    # Draw triangles of different colors to represent light.
    ### Place Your Code Here ###

    # flashlight
   
    
    if intensity >= 90:
        Polygon(200,230, 20,0,380,0, fill = rgb(170,170,170))
        Polygon(200,230, 50,0,350,0, fill = rgb(220,220,220))
        Polygon(200,230,80,0,320,0,fill = rgb(240,240,240))
        Polygon(200,230,120,0,280,0,fill = 'white')
        Rect(195, 230, 10, 60, fill=rgb(68, 68, 68))
        RegularPolygon(200, 225, 15, 3, fill=rgb(68, 68, 68), rotateAngle=180)
        Oval(200, 218, 24, 5, fill='white')
    elif intensity >= 60:
        Polygon(200,230, 20,0,380,0, fill = rgb(170,170,170))
        Polygon(200,230, 50,0,350,0, fill = rgb(220,220,220))
        Polygon(200,230,80,0,320,0,fill = rgb(240,240,240))
        Rect(195, 230, 10, 60, fill=rgb(68, 68, 68))
        RegularPolygon(200, 225, 15, 3, fill=rgb(68, 68, 68), rotateAngle=180)
        Oval(200, 218, 24, 5, fill='white')
    elif intensity >= 30:
        Polygon(200,230, 20,0,380,0, fill = rgb(170,170,170))
        Polygon(200,230, 50,0,350,0, fill = rgb(220,220,220))
        Rect(195, 230, 10, 60, fill=rgb(68, 68, 68))
        RegularPolygon(200, 225, 15, 3, fill=rgb(68, 68, 68), rotateAngle=180)
        Oval(200, 218, 24, 5, fill='white')
    elif intensity > 0:
        Polygon(200,230, 20,0,380,0, fill = rgb(170,170,170))
        Rect(195, 230, 10, 60, fill=rgb(68, 68, 68))
        RegularPolygon(200, 225, 15, 3, fill=rgb(68, 68, 68), rotateAngle=180)
        Oval(200, 218, 24, 5, fill='white')
    else:
        Rect(195, 230, 10, 60, fill=rgb(68, 68, 68))
        RegularPolygon(200, 225, 15, 3, fill=rgb(68, 68, 68), rotateAngle=180)
        Oval(200, 218, 24, 5, fill='white')
    

##### Place your code above this line, code below is for testing purposes #####
# test case:
turnOnFlashlight(0)
