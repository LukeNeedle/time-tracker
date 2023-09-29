import requests
from tkinter import *
import datetime

root = Tk()
root.title("Time tracker")
root.geometry('700x205')
root.resizable(0,0)

root.attributes('-topmost', True)
root.attributes('-fullscreen', False)

root.update_idletasks()
size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width/2 - size[0]/2
y = screen_height/2 - size[1]/2
root.geometry("+%d+%d" % (x, y))

def on_closing():
    pass

def confirm():
    doing = task.get()
    time = datetime.datetime.now()
    requests.post(url='http://127.0.0.1:5000/', json={"task": f"{doing}", "timestamp": f"""{time.strftime("%d")}-{time.strftime("%m")}-{time.strftime("%Y")}-{time.strftime("%X")}"""})
    
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

msg = Label(root, text = "What are you doing?")
msg.pack()

task = StringVar()
entry = Entry(root, textvariable = task)
entry.pack()

btn = Button(root, text = 'Submit', command = confirm)
btn.pack()

root.mainloop()