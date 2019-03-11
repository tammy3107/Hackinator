#!/usr/bin/python3
import tkinter as tk
#from tkinter import ttk
HEIGHT = 800
WIDTH = 800

def on_func():
	print("Status: Active")
	status.config(text="Status: Active")
	status.config(fg="green")
def off_func():
	print("Status: Inactive")
	status.config(text="Status: Inactive")
	status.config(fg="red")

root = tk.Tk()
root.title("XXX  PEACE KEEPER  XXX")

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="camo.PPM")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


live_frame = tk.Frame(root,bg="#091722",bd=5)
live_frame.place(relx=0.05,rely=0.05,relwidth=0.6,relheight=0.45)

live_label = tk.Label(live_frame)
live_label.place(relwidth=1,relheight=1)

button_frame = tk.Frame(root,bg="#091722",bd=5)
button_frame.place(relx=0.7,rely=0.05,relwidth=0.25,relheight=0.1)

on = tk.Button(button_frame,text = " ON ", bg="#54625B", fg="white",highlightbackground="#54625B",command=lambda:on_func())
on.place(relwidth=0.5,relheight=1)
off = tk.Button(button_frame,text = " OFF ", bg="#54625B", fg="white",highlightbackground="#54625B",command=lambda:off_func())
off.place(relx=0.5,relwidth=0.5,relheight=1)

status = tk.Label(root,text="Status: Active ",font=("Courier", 20),bg="#54625B",fg="green")
status.place(relx=0.7,rely=0.35,relwidth=0.25,relheight=0.1)


gps_frame = tk.Frame(root,bg="#091722")
gps_frame.place(relx=0.05,rely=0.5,relwidth=0.6,relheight=0.45)

gps_label = tk.Label(gps_frame)
gps_label.place(relwidth=1,relheight=1)

pos = tk.Label(root,text="Position",font=("Courier", 20),bg="#091722",fg="white")
pos.place(relx=0.68,rely=0.55,relwidth=0.3,relheight=0.1)

lat_frame = tk.Frame(root,bg="#091722",bd=5)
lat_frame.place(relx=0.68,rely=0.65,relwidth=0.3,relheight=0.1)

lat_label = tk.Label(lat_frame,bg="#7B857B",text="Latitude: ",font=("Courier", 20))
lat_label.place(relwidth=1,relheight=1)

lon_frame = tk.Frame(root,bg="#091722",bd=5)
lon_frame.place(relx=0.68,rely=0.745,relwidth=0.3,relheight=0.1)

lon_label = tk.Label(lon_frame,bg="#7B857B",text="Longitude: ",font=("Courier", 20))
lon_label.place(relwidth=1,relheight=1)

root.mainloop()