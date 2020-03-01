from tkinter import *
from tkinter import messagebox
import random
from pyyoutube import Api
from video import movie_by_mood, playlists_by_mood, apikey, random_video, random_movie

window = Tk()


def closewindow():
    exit()


def display_info(mood):
    url = random_video(mood)
    film = random_movie(mood)
    formatted_string = 'Watch this video: ' + url + '\n' + 'Watch this movie: ' + film
    movie_text.config(state=NORMAL)
    movie_text.delete("1.0", END)
    movie_text.insert(END, formatted_string)
    movie_text.config(state=DISABLED)


def happymovie():
    display_info('happy')


def sadmovie():
    display_info('sad')


def angrymovie():
    display_info('angry')


def stressedmovies():
    display_info('stressed')


btnHappy = Button(window, text='Happy', fg='black', bg='#FFD700', command=happymovie, height=1, width=8)
btnHappy.place(x=345, y=100)

btnSad = Button(window, text='Sad', fg='black', bg='#5F7C92', command=sadmovie, height=1, width=8)
btnSad.place(x=430, y=100)

btnAngry = Button(window, text='Angry', fg='black', bg='#AB2D2D', command=angrymovie, height=1, width=8)
btnAngry.place(x=510, y=100)

btnStressed = Button(window, text='Stressed', fg='black', bg='#874894', command=stressedmovies, height=1, width=8)
btnStressed.place(x=595, y=100)

btnExit = Button(window, text='Exit Page', fg='black', bg='grey', command=closewindow, height=1, width=8)
btnExit.place(x=470, y=250)

lbl = Label(window, text='Click on your current mood.', fg='black', font=("Times New Roman", 16))
lbl.place(x=380, y=50)

# txtfield = Entry(window, text='This is Entry Widget', bd=5)
# txtfield.place(x=225, y=150)

movie_text = Text(window, height=4, width=65)
movie_text.place(x=240, y=160)
movie_text.config(state=DISABLED)

window.title('Hello Python')
window.geometry("1050x300+25+25")
window.mainloop()
