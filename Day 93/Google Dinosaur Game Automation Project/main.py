import pyautogui as pg
import time

url = "elgoog.im/t-rex/"  # t rex game without needing to be offline, open this link, run the program and then go back to the webpage manually

# IMPORTANT, THIS WORKS ON A 1920X1080 MONITOR, WITH OPERA GX AS THE BROWSER, CHANGING BROWSERS MIGHT ALTER THE LOCATION OF THE PIXEL AND MAKE THE JUMP INEFFECTIVE

while True:
    time.sleep(0.01)  # any longer and it might skip the smaller cactii

    # used get current mouse position function to get the coordinates for when the dinosaur needs to jump, this works if the tab is fullscreen and in focus
    # with no obstructions such as mouse cursor
    jumper = pg.pixelMatchesColor(840, 388, (83, 83, 83))  # the color of the pixels are 83, 83, 83 in RGB

    if jumper:
        pg.press('space')
        print("Jumped")
        jumper = False  # reset jumper if triggered just in case, not needed though
