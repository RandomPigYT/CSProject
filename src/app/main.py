import os, sys
import tkinter

# Necessary code to allow importing modules from parent directory
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from window import window as w
from chess import chess as ch
from tug_of_war import tugOfWar_v2 as tof


def main():
    # a: Window = w.Window(1080, 1920, "Game launcher");

    while True:
        inp = input(
            "Select a game\n1. Chess\n2. Tug of War\n\nEnter q to quit\n\nSelection: "
        )

        if inp == "1":
            ch.chess()
        elif inp == "2":
            tof.tugOfWar()
        elif inp == "q" or inp == "Q":
            break

        else:
            print("Enter a valid selection")

        os.system("clear")

    # a.window.mainloop();


if __name__ == "__main__":
    main()
