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


btnHappy = Button(window, text='Happy', fg='black', bg='#f2f077', command=happymovie, height=1, width=8)
btnHappy.place(x=195, y=120)

btnSad = Button(window, text='Sad', fg='black', bg='#8692b8', command=sadmovie, height=1, width=8)
btnSad.place(x=280, y=120)

btnAngry = Button(window, text='Angry', fg='black', bg='#ad4040', command=angrymovie, height=1, width=8)
btnAngry.place(x=360, y=120)

btnStressed = Button(window, text='Stressed', fg='black', bg='#b059ba', command=stressedmovies, height=1, width=8)
btnStressed.place(x=445, y=120)

btnExit = Button(window, text='Exit Page', fg='black', bg='#bababa', command=closewindow, height=1, width=8)
btnExit.place(x=320, y=280)

lbl = Label(window, text='Click on Your Current Mood', fg='black', bg='#d2f7f4', font=("Calibri", 20))
lbl.place(x=203, y=50)

movie_text = Text(window, height=4, width=65, bg='#d2f7f4')
movie_text.place(x=90, y=180)
movie_text.config(state=DISABLED)

window.title('Hearts In Motion')
window.geometry("700x380+25+25")
window.configure(bg='#d2f7f4')
window.mainloop()
