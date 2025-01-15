import py5

def setup():
    py5.size(980, 980) # This is the size of the canvas
    py5.background(200, 0, 200) # Background color(R,G,B)
    # py5.rect_mode(CENTER)     # By adding this, coordenades will reference the CENTER of the figure
    # py5.rect(width / 2, heigth / 2, 200, 50)   # By adding this, the figure will be centered on the canvas
    py5.fill(0, 200, 0)         # This is the color(R,G,B) that will fill the figure
    py5.stroke(255, 0, 0)       # Stroke references the color of the border of the figure
    py5.stroke_weight(8)        # Weight is how thick (in pixels) the figure border will be
    # py5.no_stroke()           # Without the border

    py5.rect(100, 100, 200, 50) # Rect references a rectangle. The four values are: X position(Horizontal), Y position(Vertical), length, heigth

    # If we don't specify new attributes for the ellipse, it will have the attributes defined above, in this case, the same as the rectangle)
    py5.ellipse(200, 200, 100, 25) # Ellipse references an ellipse. The four values are: X position of the center, Y position of the center, length, heigth. When lenght=height we get a CIRCLE
    
   
    py5.arc(200, 300, 50, 50, 0, py5.HALF_PI)
    py5.no_fill()
    py5.arc(200, 300, 60, 60, py5.HALF_PI, py5.PI)
    py5.arc(200, 300, 70, 70, py5.PI, py5.PI+py5.QUARTER_PI)
    py5.arc(200, 300, 80, 80, py5.PI+py5.QUARTER_PI, py5.TWO_PI)
    #py5.line()
    py5.line(300, 200, 85, 75)
    py5.line(300, 200, 85, 20)
    py5.stroke(126)
    py5.line(85, 20, 85, 75)
    py5.stroke(255)
    py5.line(85, 75, 30, 75)
   
    #py5.lines()
    import numpy as np
    random_lines = 100 * np.random.rand(50, 4)
    py5.lines(random_lines)
    #py5.point()
    #py5.no_smooth()
    py5.point(400, 75)
    py5.point(400, 20)
    py5.point(600, 75)
    py5.point(500, 75)

    #py5.point()
    
    #py5.quad()
    #py5.square()
    #py5.triangle()
    #py5.circle()



py5.run_sketch()