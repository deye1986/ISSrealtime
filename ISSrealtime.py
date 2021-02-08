import tkinter as tk
from PIL import Image, ImageTk 
import sys,math
import json
import urllib.request


"""GUI"""
window = tk.Tk()
window.title("Realtime ISS Location") #Window title
window.resizable(width=False, height=False)
window.geometry("617x490")
#map_a = Image.open("") #Images
#background = ImageTk.PhotoImage(map_a) #background

canvas = tk.Canvas(window, width = "617", height = "490") #
canvas.create_image(0,0,image = False, anchor = "nw")
canvas.pack(side='top', fill='both', expand = "yes")

#text
text = canvas.create_text(500,420,text = "Number of occupants ", font=("arial", 12),fill = "darkblue")


#function

def update_location():
    red = "#f50505"

    info_iss = urllib.request.urlopen("http://api.open-notify.org/iss-now.json")
    crew = urllib.request.urlopen("http://api.open-notify.org/astros.json")


    occupants = json.load(crew)
    position = json.load(info_iss)

    number = occupants["number"]
    text_1 = canvas.create_text(600,420,text = number, font=("arial", 20),fill = "darkblue")
    print(position["iss_position"])
    x=float(position["iss_position"]["longitude"])
    y=float(position["iss_position"]["latitude"])

    #convert the coordinates
    x = 1.51 * x + 272 
    y = -2.67 * y + 240 

    x1, y1 = (x - 5), (y - 5)
    x2, y2 = (x + 5),(y + 5)
    canvas.create_oval(x1, y1, x2, y2, fill=red)
    canvas.update()

while(1):
    update_location()

window.mainloop()
