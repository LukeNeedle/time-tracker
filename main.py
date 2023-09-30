import requests
from tkinter import *
import datetime

class window():
    def __init__(self):
        self.root = Tk()
        self.root.title("Time tracker")
        self.root.geometry('700x205')
        self.root.resizable(0,0)

        self.root.attributes('-topmost', True)
        self.root.attributes('-fullscreen', False)

        self.root.update_idletasks()
        size = tuple(int(_) for _ in self.root.geometry().split('+')[0].split('x'))
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = screen_width/2 - size[0]/2
        y = screen_height/2 - size[1]/2
        self.root.geometry("+%d+%d" % (x, y))

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        msg = Label(self.root, text = "What are you doing?")
        msg.pack()

        self.task = StringVar()
        entry = Entry(self.root, textvariable = self.task)
        entry.pack()

        btn = Button(self.root, text = 'Submit', command = self.confirm)
        btn.pack()

        self.root.mainloop()
    def on_closing(self):
        requests.post(url='http://127.0.0.1:5000/stop')
        self.root.destroy()

    def confirm(self):
        doing = self.task.get()
        time = datetime.datetime.now()
        requests.post(url='http://127.0.0.1:5000/', json={"task": f"{doing}", "timestamp": f"""{time.strftime("%d")}-{time.strftime("%m")}-{time.strftime("%Y")}-{time.strftime("%X")}"""})
        
        self.root.destroy()