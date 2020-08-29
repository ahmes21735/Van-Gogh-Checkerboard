################################################
#### Van Gogh Checkerboard Coding Challenge ####
#### By Sarah Ahmed ############################
#### March 16th, 2020 ##########################
################################################
from tkinter import*
from time import*
from random import*
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=800, background="floral white" )
screen.pack()

#start with each row
for row in range(8):
     #fill grid by moving down columns across a row
    for col in range(8):
        x1col = 80 + col*80 #move to the next column
        y1row = 80 + row*80  #when the first row is complete, move down to the next row
        x2col = 160 + col*80
        y2row = y1row + 80
        colourPicker = row + col

        for n in range(80): #fill each box with random squares
            x = randint(x1col, x2col)
            y = randint(y1row, y2row)
            d = randint(2, 5) # randomize the width of each box

            if colourPicker %2 == 0: #deciding the colours (through determining even and odd)
                paint = screen.create_rectangle(x, y, x + d, y + d, fill = "#ffa69e", outline = "#ffa69e")

            else:
                paint = screen.create_rectangle(x, y, x + d, y + d, fill = "#aed9e0", outline = "#aed9e0")
