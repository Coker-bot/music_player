import tkinter as tk
import pygame
import os
import pyautogui as pe
from tkinter.filedialog import askdirectory
import time
import glob
import random

t=tk.Tk()
t.title('MusicPlayer')
t.geometry('450x450')
t.configure(bg='white')
t.resizable(0,0)
iconbitmap=('C:/Users/OA/Desktop/my music player/logo 133.png')
t.iconbitmap()
frame=tk.Frame(bg='white',pady=10)
frame.pack()


directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tk.Listbox(frame, font ="Helvetica 12 bold", bg="yellow",selectmode= tk.SINGLE)


for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()


def Folder():
    music=os.startfile('C:/Users/OA/Music')
def play_btn():
    os.startfile('C:/Users/OA/Music')
#def pause_btn():

def shuffle():
    os.chdir(directory)
    song_list = []
    for file in os.listdir(directory):
        if file.endswith('.mp3'):
            
            song_list.append(file)
    pygame.mixer.init()
    pygame.mixer.music.load(song_list[0])
    pygame.mixer.music.play()
        # Wait for the music to play before exiting 
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(5)


def play():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

pygame.mixer.init()

    
    
    

click_btn=tk.PhotoImage(file='C:/Users/OA/Pictures/logo 133.png')
label=tk.Label(frame,image=click_btn,bg='white')
label.grid(row=0,column=1)

click=tk.PhotoImage(file='C:/Users/OA/Pictures/play.png')
btn1=tk.Button(frame,image=click,bg="white",bd=0,command=play)
btn1.grid(row=1,column=0)
l0=tk.Label(frame,text='Play',font=('tahoma',8,'bold'),fg='black',bg='white')
l0.grid(row=2,column=0)

click0=tk.PhotoImage(file='C:/Users/OA/Pictures/R.png')
btn2=btn1=tk.Button(frame,image=click0,bg="white",bd=0,command=pause)
btn2.grid(row=1,column=1)
l1=tk.Label(frame,text='Pause',font=('tahoma',8,'bold'),fg='black',bg='white')
l1.grid(row=2,column=1)

click1=tk.PhotoImage(file='C:/Users/OA/Pictures/shuffle.png')
btn3=btn1=tk.Button(frame,image=click1,bg="white",bd=0,command=shuffle)
btn3.grid(row=1,column=2)
l2=tk.Label(frame,text='Shuffle',font=('tahoma',8,'bold'),fg='black',bg='white')
l2.grid(row=2,column=2)

Button4 = tk.Button(frame,text='Continue',command=unpause,bg="black",fg="white",bd=4)
Button4.grid(row=4,column=1,pady=10)

folder_btn=tk.Button(frame,text='Open Play-List',font=('tahoma',8,'bold'),fg='white',bg='black',bd=5,command=Folder)
folder_btn.grid(row=6,column=1,pady=5)



l3=tk.Label(frame,text="Coker's Ltd. Incooperation With Dthes-Tekh",font=('tahoma',8,'bold'),fg='black',bg='white')
l3.grid(row=8,columnspan=5,pady=5)

var = tk.StringVar()
songtitle = tk.Label(frame, font="Helvetica 12 bold", textvariable=var)


                     






    





