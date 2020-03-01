from tkinter import *

from tkinter import messagebox
from video import random_video, random_movie

window = Tk()

def display_info(mood):
    url = random_video(mood)
    film = random_movie(mood)
    formatted_string = 'your video: ' + url + '\n' + 'your movie: ' + film
    movie_text.config(state=NORMAL)
    movie_text.delete("1.0", END)
    movie_text.insert(END, formatted_string)
    movie_text.config(state=DISABLED)

def display_happy_info():
    display_info('happy')


def display_sad_info():
    display_info('sad')


def display_angry_info():
    display_info('angry')


def display_stressed_info():
    display_info('stressed')

movie_text = Text(window, height = 4,width = 50)
movie_text.place(x = 300, y = 300)
movie_text.config(state = DISABLED)



btnHappy = Button(window, text='Happy', fg='black', bg='#FFD700', command=display_happy_info)
btnHappy.place(x=180, y=100)

btnSad = Button(window, text='Sad', fg='black', bg='#5F7C92', command=display_sad_info)
btnSad.place(x=250, y=100)

btnAngry = Button(window, text='Angry', fg='black', bg='#AB2D2D', command=display_angry_info)
btnAngry.place(x=300, y=100)

btnStressed = Button(window, text='Stressed', fg='black', bg='#874894', command=display_stressed_info)
btnStressed.place(x=365, y=100)

lbl = Label(window, text='Click on your current mood.', fg='black', font=("Times New Roman", 16))
lbl.place(x=180, y=50)

# txtfield = Entry(window, text='This is Entry Widget', bd=5)
# txtfield.place(x=225, y=150)

window.title('Hello Python')
window.geometry("500x300+25+25")
window.mainloop()
