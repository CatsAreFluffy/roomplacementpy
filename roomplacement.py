#Room Placement Python v0.0.2
#Not equivalent to any Room Placement Scratch version
#https://scratch.mit.edu/projects/137918573/
import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.scale=2
        self.objects=[]
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.draw=tk.Canvas(self,width=480*self.scale,height=360*self.scale,background="#eeeeee")
        self.draw.pack()
        def place(event):
            self.objects+=[[self.draw.create_rectangle(event.x-32*self.scale,event.y-42*self.scale,event.x+32*self.scale,event.y+42*self.scale,fill="#aa6600",outline="#aa6600"),\
                           self.draw.create_rectangle(event.x-30*self.scale,event.y-20*self.scale,event.x+30*self.scale,event.y+40*self.scale,fill="#ff0000",outline="#ff0000"),\
                           self.draw.create_rectangle(event.x-30*self.scale,event.y-40*self.scale,event.x+30*self.scale,event.y-20*self.scale,fill="#ffffff",outline="#ffffff")]]
            print(self.objects)
        self.draw.bind("<Button-1>",place)
root = tk.Tk()
app = Application(master=root)
app.mainloop()
