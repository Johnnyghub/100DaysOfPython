from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageDraw, ImageFont

window = Tk()
window.title("Image Watermarker")
window.resizable(False, False)

filetypes = ('Image .jpg', 'Image .png', 'Image .gif', 'Image .jpeg')

filename = fd.askopenfilename(  # choose the image file you want from the types listed above
    title='Open a file',
    initialdir='Photos/',
    filetypes=filetypes
)

im = Image.open(filename)  # open that image with Pillow
tk_image = ImageTk.PhotoImage(im)  # and pass it to ImageTk

draw = ImageDraw.Draw(im)  # this is used to draw 2D vectors over an image
text = 'Johnny Watermark'

font = ImageFont.truetype('arial.ttf', 50)
textwidth, textheight = draw.textsize(text, font)

x = (tk_image.width()/2) - (textwidth/2)  # get center of image on x axis
y = (tk_image.height()/2) - (textheight/2)  # get center of image on y axis

draw.text((x, y), text, font=font)  # draw the watermark
im.show()

# filename is the whole path, but we wanna change folders so split it by / and get only the actual file name and save it
im.save(f'Watermarked_Photos/{filename.split("/")[-1]}')  # save the image in watermarked images folder

window.mainloop()
