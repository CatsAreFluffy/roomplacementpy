#Room Placement Python v0.1
#Roughly equivalent to Room Placement 0.1
#https://scratch.mit.edu/projects/137120650/
import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.scale=1
        self.wscale=1
        self.oscale=2
        self.wscale*=self.scale
        self.oscale*=self.scale
        self.objects=[]
        self.selected=0
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.draw=tk.Canvas(self,width=480*self.wscale,height=360*self.wscale,background="#eeeeee")
        self.draw.pack()
        def place(event):
            if self.selected==0:
                self.objects+=[[self.draw.create_rectangle(event.x-32*self.oscale,event.y-42*self.oscale,event.x+32*self.oscale,event.y+42*self.oscale,fill="#cc8800",outline="#cc8800"),\
                                self.draw.create_rectangle(event.x-30*self.oscale,event.y-20*self.oscale,event.x+30*self.oscale,event.y+40*self.oscale,fill="#ff0000",outline="#ff0000"),\
                                self.draw.create_rectangle(event.x-30*self.oscale,event.y-40*self.oscale,event.x+30*self.oscale,event.y-20*self.oscale,fill="#ffffff",outline="#ffffff")]]
            elif self.selected==1:
                self.objects+=[[self.draw.create_rectangle(event.x-20*self.oscale,event.y-20*self.oscale,event.x+20*self.oscale,event.y+20*self.oscale,fill="#cc8800",outline="#cc8800"),\
                                self.draw.create_rectangle(event.x-10*self.oscale,event.y- 5*self.oscale,event.x+10*self.oscale,event.y+20*self.oscale,fill="#eeeeee",outline="#eeeeee")]]
            elif self.selected==2:
                self.objects+=[[self.draw.create_rectangle(event.x-40*self.oscale,event.y-30*self.oscale,event.x+40*self.oscale,event.y+30*self.oscale,fill="#e6e6ff",outline="#aaaaaa",width=2)]]
            elif self.selected==3:
                self.objects+=[[self.draw.create_rectangle(event.x-20*self.oscale,event.y-30*self.oscale,event.x+20*self.oscale,event.y+30*self.oscale,fill="#000000",outline="#000000"),\
                                self.draw.create_oval     (event.x+11*self.oscale,event.y- 4*self.oscale,event.x+18*self.oscale,event.y+ 3*self.oscale,fill="#eeeeee",outline="#eeeeee")]]
            print(self.objects)
        self.draw.bind("<Button-1>",place)
        def nextobject(event):
            self.selected+=1
            self.selected%=4
            print(self.selected)
        def prevobject(event):
            self.selected-=1
            self.selected%=4
            print(self.selected)
        self.master.bind("<Right>",nextobject)
        self.master.bind("<Left>", prevobject)
root = tk.Tk()
app = Application(master=root)
app.mainloop()
