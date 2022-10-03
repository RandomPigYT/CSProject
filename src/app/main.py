import os, sys
import tkinter

# Necessary code to allow importing modules from parent directory
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from window import window as w
from chess import chess as ch


def main():
    # a: Window = w.Window(1080, 1920, "Game launcher");

    ch.chess()

    # a.window.mainloop();


if __name__ == "__main__":
    main()
