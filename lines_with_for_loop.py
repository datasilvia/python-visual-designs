import py5

def setup():
    py5.size(980, 980) 
    py5.background(240) 

    numbers = [1, 13, 21, 42]
    for n in numbers:
        py5.line(n * 10, 50, 250, 250) # X position start (Horizontal), Y position start (Vertical), X position end (Horizontal), Y position end (Vertical)


    num = [10, 20, 30, 40, 50, 60] 
    for n in num: # The same as writting: for n in range(10, 70, 10):
        py5.line(n * 10, 275, n * 12, 450)


    for n in range(10, 70, 2):
        py5.line(n * 10, 475, n * 12, 750)

    
    for n in range(10, 70, 4):
        py5.line(n * 10, 775, n * 5, 950)

    

py5.run_sketch()