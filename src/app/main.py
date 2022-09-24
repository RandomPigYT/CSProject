import os, sys

# Necessary code to allow importing modules from parent directory
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from window import window as w

def main():
    a = w.Window(1080, 1920, "Game launcher")
    


if __name__ == "__main__":
    main();
