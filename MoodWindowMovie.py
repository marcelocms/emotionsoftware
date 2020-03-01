from tkinter import *
from tkinter import messagebox
import random

window = Tk()


def closewindow():
    exit()


happyMovies = ['Grown Ups', 'Blended', 'Ride Along', 'Daddy Day Care', 'Are We There Yet?', 'Matilda']
sadMovies = ['Titanic', 'Marley and Me', 'The Fault in Our Stars', 'The Last Song', 'The Notebook', 'Me Before You']
angryMovies = ['The Karate Kid', 'Avengers', 'Fast and Furious', 'Saw', 'Escape Room', 'The Shallows']
stressedMovies = ['Aladdin', 'Moana', 'Tangled', 'Hercules', 'Pinocchio', 'Peter Pan']


def happymovie():
    movie = random.randint(0, 5)
    messagebox.showinfo('Information for mood', happyMovies[movie])


def sadmovie():
    movie = random.randint(0,5)
    messagebox.showinfo('Information for mood', sadMovies[movie])


def angrymovie():
    movie = random.randint(0,5)
    messagebox.showinfo('Information for mood', angryMovies[movie])


def stressedmovies():
    movie = random.randint(0,5)
    messagebox.showinfo('Information for mood', stressedMovies[movie])


btnHappy = Button(window, text='Happy', fg='black', bg='#FFD700', command=happymovie)
btnHappy.place(x=180, y=100)

btnSad = Button(window, text='Sad', fg='black', bg='#5F7C92', command=sadmovie)
btnSad.place(x=250, y=100)

btnAngry = Button(window, text='Angry', fg='black', bg='#AB2D2D', command=angrymovie)
btnAngry.place(x=300, y=100)

btnStressed = Button(window, text='Stressed', fg='black', bg='#874894', command=stressedmovies)
btnStressed.place(x=365, y=100)

btnExit = Button(window, text='Exit Page', fg='black', bg='grey', command=closewindow)
btnExit.place(x=275, y=150)

lbl = Label(window, text='Click on your current mood.', fg='black', font=("Times New Roman", 16))
lbl.place(x=180, y=50)

# txtfield = Entry(window, text='This is Entry Widget', bd=5)
# txtfield.place(x=225, y=150)

window.title('Hello Python')
window.geometry("600x200+25+25")
window.mainloop()