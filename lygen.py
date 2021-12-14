# importing only those functions
# which are needed

from tkinter import *
from tkinter.ttk import *
from lyrics_extractor import SongLyrics
import tkinter as tk
from tkinter import messagebox

# creating tkinter window
root = Tk()
root.title('Lyrics Generator')
root.configure(bg = '#5B9AE6')
root.geometry('600x760')

#background image
bg = PhotoImage(file = "C:/Users/kris/Desktop/ACP FINAL_PROJ/bg.png")
  
# Show image using label
label = Label( root, image = bg)
label.place(x = -65, y = 0)

#set window icon
root.iconphoto(False, tk.PhotoImage(file='C:/Users/kris/Desktop/ACP FINAL_PROJ/ICON.png'))

#functio to get lyrics using api & message box if song not found
def get_lyrics():
	try:
		extract_lyrics = SongLyrics("AIzaSyAv8FlMaTUVdZGc1sAES-X-DUUU8WVrQoE", "0f52a8efe958a2a24")
		temp = extract_lyrics.get_lyrics(str(songInput.get()))
		res = temp['lyrics']
		result.set(res)
	except:
		messagebox.showinfo("LyGen", "Song not found")
	
result = StringVar()

label1 = tk.Label(root, text = "Search Lyrics",
font = ('Century Gothic', 12))
label1.config(bg = "#82bac1", fg = "#E53D00")
label1.place(x = 50, y = 50) 


songInput = Entry(root, width = 30, font = ('Century Gothic', 12))
songInput.place(x = 155, y = 50)

label2 = tk.Label(root, width = 50, textvariable = result,
font = ('Century Gothic', 8))
label2.config(bg = "#82bac1", fg = "#262626")
label2.place(x = 145, y = 85)


# Adding widgets to the root window
label3 = tk.Label(root, text = 'Lyrics Generator', 
font = ('Century Gothic', 18))
label3.config(bg = "#82bac1", fg = "#E53D00")
label3.pack(side = TOP, pady = 10)


# Creating a photoimage object to use image
photo = PhotoImage(file = r"C:/Users/kris/Desktop/ACP FINAL_PROJ/search.png")

# Resizing image to fit on button
photoimage = photo.subsample(5, 5)

#button search, inserted w/ image
#using the function get_lyrics in command
searchbtn = tk.Button(root, text = 'Search', image = photoimage, command=get_lyrics, compound = LEFT)
searchbtn.config(fg = "#E53D00", bg = "#82bac1", font = ('Century Gothic', 8))
searchbtn.place(x = 440, y = 45)

root.resizable(False, False)

mainloop()
