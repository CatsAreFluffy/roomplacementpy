#Room Placement Python v0.0.1
#Not equivalent to any Room Placement Scratch version
#https://scratch.mit.edu/projects/137918573/
import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.scale=2
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.draw=tk.Canvas(self,width=480*self.scale,height=360*self.scale)
        self.draw.pack()
        def place(event):
            return self.draw.create_rectangle(event.x-10,event.y-10,event.x+10,event.y+10)
        self.draw.bind("<Button-1>",place)
    def say_hi(self):
        print("hi there, everyone!")
root = tk.Tk()
app = Application(master=root)
app.mainloop()
