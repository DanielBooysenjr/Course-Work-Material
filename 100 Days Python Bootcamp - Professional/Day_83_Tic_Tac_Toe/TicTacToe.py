# Main File

from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox
import time


OPTIONS = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

A1 = 31, 119
A2 = 181, 131
A3 = 353, 136
B1 = 30, 231
B2 = 190, 236
B3 = 344, 228
C1 = 42, 343
C2 = 192, 337
C3 = 342, 333


class Main():
    def __init__(self):
        self.self_score = []
        self.opponent_score = []
        self.computers_turn = False
        self.players_turn = True
        self.tictactoe = Tk()
        self.tictactoe.geometry("500x600")
        self.tictactoe.title('Tic Tac Toe')
        self.canvas = Canvas(self.tictactoe, width=800, height=600)
        self.canvas.pack()
        image = Image.open('board.jpg')
        resized_image = image.resize((500, 600))
        self.background = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0,0, anchor=NW, image=self.background)
        self.canvas.bind("<Button-1>", self.check_player_move)
        self.players_move()
        x = Image.open('x.png')
        x_resized_image = x.resize((100, 100))
        self.x = ImageTk.PhotoImage(x_resized_image)
        o = Image.open('o.png')
        o_resized_image = o.resize((100, 100))
        self.o = ImageTk.PhotoImage(o_resized_image)
        self.tictactoe.mainloop()

    # Check player move
    def check_player_move(self, event):
        x = event.x
        y = event.y
        if x > 23 and x < 160 and y > 112 and y < 203:
            if "a1" in OPTIONS:
                OPTIONS.remove('a1')
                self.self_score.append('a1')
                self.canvas.create_image(A1, anchor=NW, image=self.x)
            else:
                print("Invalid Move")
        elif x > 173 and x < 318 and y > 112 and y < 202:
            if "a2" in OPTIONS:
                OPTIONS.remove('a2')      
                self.self_score.append('a2')
                self.canvas.create_image(A2, anchor=NW, image=self.x)
            else:
                print('Invalid Move')
        elif x > 331 and x < 473 and y > 114 and y < 203:
            if "a3" in OPTIONS:
                OPTIONS.remove('a3')      
                self.self_score.append('a3')
                self.canvas.create_image(A3, anchor=NW, image=self.x)
            else:
                print("Invalid Move")
        elif x > 27 and x < 162 and y > 220 and y < 306:
            if 'b1' in OPTIONS:
                OPTIONS.remove('b1')        
                self.self_score.append('b1')
                self.canvas.create_image(B1, anchor=NW, image=self.x)
            else:
                print('Invalid Move')
        elif x > 177 and x < 316 and y > 218 and y < 310:
            if "b2" in OPTIONS:
                OPTIONS.remove('b2')
                self.self_score.append('b2')
                self.canvas.create_image(B2, anchor=NW, image=self.x)
            else:
                print("Invalid Move")
        elif x > 333 and x < 475 and y > 214 and y < 309:
            if "b3" in OPTIONS:
                OPTIONS.remove('b3')
                self.self_score.append('b3')
                self.canvas.create_image(B3, anchor=NW, image=self.x)
            else:
                print("Invalid Move")
        elif x > 26 and x < 152 and y > 323 and y < 413:
            if "c1" in OPTIONS:
                OPTIONS.remove('c1')
                self.self_score.append('c1')
                self.canvas.create_image(C1, anchor=NW, image=self.x)
            else:
                print("Invalid Move")
        elif x > 178 and x < 314 and y > 323 and y < 412:
            if "c2" in OPTIONS:
                OPTIONS.remove('c2')
                self.self_score.append('c2')
                self.canvas.create_image(C2, anchor=NW, image=self.x)
            else:
                print("Invalid Move")
        elif x > 332 and x < 477 and y > 323 and y < 414:
            if "c3" in OPTIONS:
                OPTIONS.remove('c3')
                self.self_score.append('c3')
                self.canvas.create_image(C3, anchor=NW, image=self.x)
            else:
                print("Invalid Move")
        elif len(OPTIONS) <= 0:
            messagebox.showinfo("Info", "Game Ended in Draw")
        else:
            messagebox.showinfo("Out of Bound", "Please click on one of the boxes, you lost a turn")
        self.players_turn = False
        self.computers_move()

    # Computer Move
    def computers_move(self):
        self.computers_turn = True
        if self.computers_turn == True and len(OPTIONS) > 0:
            choice = random.choice(OPTIONS)
            if choice == 'a1':
                self.opponent_score.append('a1')
                self.canvas.create_image(A1, anchor=NW, image=self.o)
            elif choice == 'a2':
                self.opponent_score.append('a2')
                self.canvas.create_image(A2, anchor=NW, image=self.o)
            elif choice == 'a3':
                self.opponent_score.append('a3')
                self.canvas.create_image(A3, anchor=NW, image=self.o)
            elif choice == 'b1':
                self.opponent_score.append('b1')
                self.canvas.create_image(B1, anchor=NW, image=self.o)
            elif choice == 'b2':
                self.opponent_score.append('b2')
                self.canvas.create_image(B2, anchor=NW, image=self.o)
            elif choice == 'b3':
                self.opponent_score.append('b3')
                self.canvas.create_image(B3, anchor=NW, image=self.o)
            elif choice == 'c1':
                self.opponent_score.append('c1')
                self.canvas.create_image(C1, anchor=NW, image=self.o)
            elif choice == 'c2':
                self.opponent_score.append('c2')
                self.canvas.create_image(C2, anchor=NW, image=self.o)
            elif choice == 'c3':
                self.opponent_score.append('c3')
                self.canvas.create_image(C3, anchor=NW, image=self.o)
            OPTIONS.remove(choice)
            
            self.computers_turn = False
            self.check_status()
        elif len(OPTIONS) <= 0:
            messagebox.showinfo("Info", "Game Ended in Draw")
            
    # Player Move
    def players_move(self):
        if self.players_turn == False:
            self.check_status()
            self.computers_move()

    # Check if a player won
    def check_status(self):
        win_conditions = [['a1', 'a2', 'a3'], ['a1', 'b1', 'c1'], ['a1', 'b2', 'c3'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'], ['a3', 'b2', 'c1'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']]
        for condition in win_conditions:
            if all(move in self.self_score for move in condition):
                messagebox.showinfo("Won!", "You Won!")
                return
            elif all(move in self.opponent_score for move in condition):
                messagebox.showinfo("Lost!", "You Lost")
        



game = Main()