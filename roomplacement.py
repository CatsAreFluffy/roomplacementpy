#Room Placement Python v0.0.3
#Not equivalent to any Room Placement Scratch version
#https://scratch.mit.edu/projects/137918573/
import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.scale=2
        self.objects=[]
        self.selected=0
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.draw=tk.Canvas(self,width=480*self.scale,height=360*self.scale,background="#eeeeee")
        self.draw.pack()
        def place(event):
            if self.selected==0:
                self.objects+=[[self.draw.create_rectangle(event.x-32*self.scale,event.y-42*self.scale,event.x+32*self.scale,event.y+42*self.scale,fill="#cc8800",outline="#cc8800"),\
                                self.draw.create_rectangle(event.x-30*self.scale,event.y-20*self.scale,event.x+30*self.scale,event.y+40*self.scale,fill="#ff0000",outline="#ff0000"),\
                                self.draw.create_rectangle(event.x-30*self.scale,event.y-40*self.scale,event.x+30*self.scale,event.y-20*self.scale,fill="#ffffff",outline="#ffffff")]]
            elif self.selected==1:
                self.objects+=[[self.draw.create_rectangle(event.x-20*self.scale,event.y-20*self.scale,event.x+20*self.scale,event.y+20*self.scale,fill="#cc8800",outline="#cc8800"),\
                                self.draw.create_rectangle(event.x-10*self.scale,event.y- 5*self.scale,event.x+10*self.scale,event.y+20*self.scale,fill="#eeeeee",outline="#eeeeee")]]
            elif self.selected==2:
                self.objects+=[[self.draw.create_rectangle(event.x-40*self.scale,event.y-30*self.scale,event.x+40*self.scale,event.y+30*self.scale,fill="#e6e6ff",outline="#aaaaaa",width=2)]]
            print(self.objects)
        self.draw.bind("<Button-1>",place)
        def nextobject(event):
            self.selected+=1
            self.selected%=3
            print(self.selected)
        def prevobject(event):
            self.selected-=1
            self.selected%=3
            print(self.selected)
        self.master.bind("<Right>",nextobject)
        self.master.bind("<Left>", prevobject)
root = tk.Tk()
app = Application(master=root)
app.mainloop()
