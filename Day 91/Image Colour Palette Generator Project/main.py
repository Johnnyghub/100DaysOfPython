from colorthief import ColorThief
from tkinter import *
from tkinter.filedialog import askopenfilename

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

color_thief = ColorThief(filename)  # get the color data for this image using the ColorThief package

top_colors = color_thief.get_palette(color_count=11)  # 11 gives a 10 color palette

window = Tk()
window.minsize(width=100, height=500)
window.title('Palette')

canvas = Canvas(window, width=200, height=500)
canvas.pack()

x1 = 0
y1 = 0
x2 = 200  # display rectangle at full width
y2 = 50  # each pixel will be 50 pixels tall

color_blocks = []

for color in top_colors:  # iterate through the colors of the canvas and turn each one into a rectangle
    this_color = '#%02x%02x%02x' % color  # convert the RGB tuple to hecadecimal data using the format operator, need to specify each color as 2 digits incase it is 0
    color_blocks.append(canvas.create_rectangle(x1, y1, x2, y2, fill=this_color, width=0))
    y1 += 50
    y2 += 50  # move down 50 pixels to display the next color to create a palette card aesthetic

window.mainloop()
