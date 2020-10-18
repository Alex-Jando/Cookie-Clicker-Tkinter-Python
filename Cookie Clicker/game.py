from tkinter import *
from PIL import ImageTk, Image
import threading
from tkinter import messagebox
import time
from tkinter import PhotoImage
from tkinter import ttk
#---------------------------------------------------------------------------

cookies = 0

root = Tk()
root.title("Cookie Clicker")
root.resizable()
root.resizable(width=False, height=False)
root.iconphoto(True, PhotoImage(file='icon.png'))
tabControl = ttk.Notebook(root)
cookieTab = ttk.Frame(tabControl)
shopTab = ttk.Frame(tabControl)
tabControl.add(cookieTab, text="Cookie")
tabControl.add(shopTab, text="Shop")
tabControl.grid(row=0, column=0, sticky="w")
#---------------------------------------------------------------------------

def bake():

	global cookies

	cookies += 1
	cookieCounter1.config(text=f"Cookies: {cookies}")
	cookieCounter2.config(text=f"Cookies: {cookies}")

#Granny

def newGranny():

	global cookies

	while True:
		time.sleep(1)
		cookies += 5
		cookieCounter1.config(text=f"Cookies: {cookies}")
		cookieCounter2.config(text=f"Cookies: {cookies}")

def addGranny():

	global cookies

	if cookies >= 100:

		gran = threading.Thread(target=newGranny)
		gran.setDaemon(True)
		gran.start()

		cookies -= 100


	else:
		messagebox.showinfo("Granny", "Sorry you don't have enough cookies to hire a granny")

#Clicker

def newClicker():

	global cookies

	while True:
		time.sleep(1)
		cookies += 1
		cookieCounter1.config(text=f"Cookies: {cookies}")
		cookieCounter2.config(text=f"Cookies: {cookies}")

def addClicker():

	global cookies

	if cookies >= 10:

		click = threading.Thread(target=newClicker)
		click.setDaemon(True)
		click.start()

		cookies -= 10


	else:
		messagebox.showinfo("Clicker", "Sorry you don't have enough cookies to make a clicker")

#rat

def newRat():

	global cookies

	while True:
		time.sleep(1)
		cookies += 10
		cookieCounter1.config(text=f"Cookies: {cookies}")
		cookieCounter2.config(text=f"Cookies: {cookies}")

def addRat():

	global cookies

	if cookies >= 1000:

		rats = threading.Thread(target=newRat)
		rats.setDaemon(True)
		rats.start()

		cookies -= 1000


	else:
		messagebox.showinfo("Rat", "Sorry you don't have enough cookies to buy a rat")

#mario

def newMario():

	global cookies

	while True:
		time.sleep(1)
		cookies += 100
		cookieCounter1.config(text=f"Cookies: {cookies}")
		cookieCounter2.config(text=f"Cookies: {cookies}")

def addMario():

	global cookies

	if cookies >= 10000:

		mariotime = threading.Thread(target=newMario)
		mariotime.setDaemon(True)
		mariotime.start()

		cookies -= 10000


	else:
		messagebox.showinfo("Mario", "Sorry you don't have enough cookies to hire a Mario")

#---------------------------------------------------------------------------

cookieTitle = Label(cookieTab, text="Cookie Clicker", font=("Arial", 24))
shopTitle = Label(shopTab, text="Shop", font=("Arial", 24))

cookieImg = ImageTk.PhotoImage(Image.open("cookie.png"))
cookieCliackable = Button(cookieTab, image = cookieImg, command = bake)

cookieCounter1 = Label(cookieTab, text=f"Cookies: {cookies}", font=("Arial", 12))
cookieCounter2 = Label(shopTab, text=f"Cookies: {cookies}", font=("Arial", 12))

grannyImg = Image.open("granny.jpg")
grannyImg = ImageTk.PhotoImage(grannyImg.resize((100, 100), Image.ANTIALIAS))
granny = Button(shopTab, image = grannyImg, command = addGranny, padx=5, pady=5)
grannyTitle = Label(shopTab, text="Granny: 100 Cookies", font=("Arial", 12), padx=5, pady=5)

clickerImg = Image.open("clicker.jpg")
clickerImg = ImageTk.PhotoImage(clickerImg.resize((100, 100), Image.ANTIALIAS))
clicker = Button(shopTab, image = clickerImg, command = addClicker, padx=5, pady=5)
clickerTitle = Label(shopTab, text="Clicker: 10 Cookies", font=("Arial", 12), padx=5, pady=5)

ratImg = Image.open("rat.png")
ratImg = ImageTk.PhotoImage(ratImg.resize((100, 100), Image.ANTIALIAS))
rat = Button(shopTab, image = ratImg, command = addRat, padx=5, pady=5)
ratTitle = Label(shopTab, text="Rat: 1000 Cookies", font=("Arial", 12), padx=5, pady=5)

marioImg = Image.open("mario.jpg")
marioImg = ImageTk.PhotoImage(marioImg.resize((100, 100), Image.ANTIALIAS))
mario = Button(shopTab, image = marioImg, command = addMario, padx=5, pady=5)
marioTitle = Label(shopTab, text="Mario: 10000 Cookies", font=("Arial", 12), padx=5, pady=5)

cookieTitle.grid(row=1, column=0)
cookieCliackable.grid(row=2, column=0)
cookieCounter1.grid(row=3, column=0)

shopTitle.grid(row=0, column=0, columnspan=2)

clickerTitle.grid(row=1, column=0)
clicker.grid(row=2, column=0)

grannyTitle.grid(row=3, column=0)
granny.grid(row=4, column=0)

ratTitle.grid(row=1, column=1)
rat.grid(row=2, column=1)

marioTitle.grid(row=3, column=1)
mario.grid(row=4, column=1)

cookieCounter2.grid(row=5, column=0, columnspan=2)


#---------------------------------------------------------------------------
root.mainloop()

print("MADE BY: Alex-Jando")