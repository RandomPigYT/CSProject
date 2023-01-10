# importing webbrowser module
import webbrowser
# importing all files from tkinter module
from tkinter import *

import os
import sys
# Necessary code to allow importing modules from parent directory
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from chess import chess
from connect4 import connect4
from pong import gagans_pong
from snek import snekg
from tictactoe import ticTacToe
from tug_of_war import tugOfWar_v2

# creating root
root = Tk()
# setting GUI title
root.title("Game Launcher")
root.config(bg = "#000000")
# setting GUI geometry
root.geometry("1080x1080")

root.state('normal')



def chessg():
    chess.chess()

def c4g():
    connect4.connectfour()

def pongg():
    gagans_pong.pong()

def snekGame():
    snekg.snek()

def tttg():
    ticTacToe.tictactoe()

def tofg():
    tugOfWar_v2.tugOfWar()


Label(root,bg='black' , text="Game Launcher", font="Mojangles 30 bold",foreground="white").pack()
Label(root, bg = 'black' , text="Choose Your Game",font="Mojangles 15 bold", foreground = 'white').pack()

chessg_button = Button(root,text="Chess", command=chessg,font="LUCIDA 15 bold").pack(padx=20,pady=20)

pongg_button = Button(root, text="Pong", command=pongg,font="LUCIDA 15 bold").pack(padx=20,pady=20)

snekg_button = Button(root, text="Snake", command=snekGame,font="LUCIDA 15 bold").pack(padx=20,pady=20)

c4g_button = Button(root, text="Connect 4", command=c4g,font="LUCIDA 15 bold").pack(padx=20,pady=20)

tttg_button = Button(root, text="Tic Tac Toe", command=tttg,font="LUCIDA 15 bold").pack(padx=20,pady=20)

towg_button = Button(root, text="Tug Of War", command=tofg,font="LUCIDA 15 bold").pack(padx=20,pady=20)


#running the mainloop()
root.mainloop()
