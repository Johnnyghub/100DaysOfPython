from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pdfminer.high_level import extract_text
import pyttsx3 as tts

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

text = extract_text(filename)  # extracts the text from a PDF file

engine = tts.init()  #initialize text to speech engine
engine.setProperty("rate", 225)  # sets the speaking rate to 225, default 125, I prefer very fast speech :)
engine.save_to_file(text, f"./Audios/{filename.split('/')[-1].split('.')[0]}.mp3")  # save file as the pdf filename but with .mp3 at the end
engine.runAndWait()  #  this executes it all essentially

print("Check the Audios folder to find your mp3 file!")
