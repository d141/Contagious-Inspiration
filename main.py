# This is a sample Python script.
import pyautogui
import random
import time
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def move_mouse(iterations):
    # Use a breakpoint in the code line below to debug your script.
    i=0
    while i<iterations:
        x = random.randrange(1, 1000)
        y = random.randrange(1, 1000)
        pyautogui.moveTo(x, y, duration = 1)
        time.sleep(30)
        i+=1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    move_mouse(800)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
