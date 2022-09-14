import time

import pyautogui
import keyboard

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings
def fullCombo():

        time.sleep(2)
        countr = 0;

        while True:


                        time.sleep(0.1)
                        keyboard.press('1')
                        time.sleep(0.2)
                        keyboard.release('1')
                        time.sleep(0.1)
                        keyboard.press('2')
                        time.sleep(0.4)
                        keyboard.release('2')
                        time.sleep(0.1)
                        keyboard.press('3')
                        time.sleep(0.2)
                        keyboard.release('3')
                        time.sleep(0.1)
                        keyboard.press('4')
                        time.sleep(0.2)
                        keyboard.release('4')
                        time.sleep(0.1)
                        keyboard.press('tab')
                        time.sleep(0.2)
                        keyboard.release('tab')



def soloCombo():


        time.sleep(3)
        keyboard.press('insert')
        time.sleep(0.1)
        keyboard.release('insert')

        time.sleep(2)
        countr = 0;
        while True:

                        time.sleep(0.1)
                        keyboard.press('1')
                        time.sleep(0.1)
                        keyboard.release('1')
                        time.sleep(0.1)
                        keyboard.press('2')
                        time.sleep(0.1)
                        keyboard.release('2')
                        time.sleep(0.1)
                        keyboard.press('tab')
                        time.sleep(0.1)
                        keyboard.release('tab')



if __name__ == '__main__':

    soloCombo()