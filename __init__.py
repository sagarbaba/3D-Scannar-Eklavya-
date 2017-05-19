import numpy as np
import cv2
import Tkinter as tk
import Image, ImageTk
import os
import ttk
import v4l2
import fcntl 
import os 
import sys

def main():
	VideoDeviceNumber=0
	f=open("Temp.txt",'r')
	str=f.read()
	f.close()
	if (str==''):
		VideoDeviceNumber=0
	else:
		VideoDeviceNumber=int(str)
	AddressList=[]
	CamList=[]
	CamDict={}
	DeviceList=os.listdir("/dev") #it will return a list of the contents inside /dev
	for i in DeviceList:
		temp=i
		if (temp[:5]=='video'):
			AddressList.append(i) #the video devices are added to CamList
	for i in AddressList:
		vd = open("/dev/"+i, 'rw') 
		cp = v4l2.v4l2_capability()
		fcntl.ioctl(vd, v4l2.VIDIOC_QUERYCAP, cp) 
		CamList.append(cp.card)
		CamDict[cp.card]=i
	def SelectedDevice():
		print VideoDeviceName.get()
		TempString=CamDict[VideoDeviceName.get()]
		k=open("Temp.txt",'w')
		k.write(TempString[5:6])
		k.close()
		root.destroy()	
	root = tk.Tk()
	root.title("Webcam Interface")
	menubar = tk.Menu(root)
	filemenu = tk.Menu(menubar, tearoff=0)
	filemenu.add_command(label="Exit", command=root.quit)
	menubar.add_cascade(label="File", menu=filemenu)
	editmenu = tk.Menu(menubar, tearoff=0)
	#editmenu.add_command(label="Settings")
	menubar.add_cascade(label="Settings", menu=editmenu)
	VideoDeviceName=tk.StringVar()
	for i in CamList:
		editmenu.add_radiobutton(label=i, variable=VideoDeviceName, command=SelectedDevice)
	helpmenu = tk.Menu(menubar, tearoff=0)
	helpmenu.add_command(label="About")
	menubar.add_cascade(label="Help", menu=helpmenu)
	root.config(menu=menubar)
	imageFrame = tk.Frame(root, width=640, height=480)
	imageFrame.grid(row=0, column=0, padx=10, pady=2)
	lmain = tk.Label(imageFrame)
	lmain.grid(row=0, column=0)
	cap = cv2.VideoCapture(VideoDeviceNumber)
	def show_frame():
		_, frame = cap.read()
		#frame = cv2.flip(frame, 1)
		#cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
		#img = Image.fromarray(cv2image)
		img = Image.fromarray(frame)
		imgtk = ImageTk.PhotoImage(image=img)
		lmain.imgtk = imgtk
		lmain.configure(image=imgtk)
		lmain.after(10, show_frame) 
	show_frame()
	root.mainloop()

