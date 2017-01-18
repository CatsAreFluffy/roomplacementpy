#Room Placement Python v0.1.1
#Roughly equivalent to Room Placement 0.1
#https://scratch.mit.edu/projects/137120650/
import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.scale=1
        self.wscale=2
        self.oscale=2
        self.wscale*=self.scale
        self.oscale*=self.scale
        self.objects=[]
        self.selected=0
        self.blockx=0
        self.blocky=0
        self.originx=240*self.wscale
        self.originy=180*self.wscale
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.draw=tk.Canvas(self,width=480*self.wscale,height=360*self.wscale,background="#eeeeee")
        self.draw.pack()
        self.blockparts=[self.draw.create_rectangle(self.originx-10*self.oscale,self.originy-10*self.oscale,self.originx+10*self.oscale,self.originy+10*self.oscale,fill="#1111ee",outline="#111111")]
        def place(event):
            if self.selected==0: #bed
                self.objects+=[[self.draw.create_rectangle(event.x-32*self.oscale,event.y-42*self.oscale,event.x+32*self.oscale,event.y+42*self.oscale,fill="#cc8800",outline="#cc8800"),\
                                self.draw.create_rectangle(event.x-30*self.oscale,event.y-20*self.oscale,event.x+30*self.oscale,event.y+40*self.oscale,fill="#ff0000",outline="#ff0000"),\
                                self.draw.create_rectangle(event.x-30*self.oscale,event.y-40*self.oscale,event.x+30*self.oscale,event.y-20*self.oscale,fill="#ffffff",outline="#ffffff")]]
            elif self.selected==1: #table
#                self.objects+=[[self.draw.create_rectangle(event.x-20*self.oscale,event.y-20*self.oscale,event.x+20*self.oscale,event.y+20*self.oscale,fill="#cc8800",outline="#cc8800"),\
#                                self.draw.create_rectangle(event.x-10*self.oscale,event.y- 5*self.oscale,event.x+10*self.oscale,event.y+20*self.oscale,fill="#eeeeee",outline="#eeeeee")]]
                self.objects+=[[self.draw.create_rectangle(event.x-20*self.oscale,event.y-20*self.oscale,event.x-10*self.oscale,event.y+20*self.oscale,fill="#cc8800",outline="#cc8800"),\
                                self.draw.create_rectangle(event.x-10*self.oscale,event.y-20*self.oscale,event.x+10*self.oscale,event.y- 5*self.oscale,fill="#cc8800",outline="#cc8800"),\
                                self.draw.create_rectangle(event.x+10*self.oscale,event.y-20*self.oscale,event.x+20*self.oscale,event.y+20*self.oscale,fill="#cc8800",outline="#cc8800")]]
            elif self.selected==2: #window
                self.objects+=[[self.draw.create_rectangle(event.x-40*self.oscale,event.y-30*self.oscale,event.x+40*self.oscale,event.y+30*self.oscale,fill="#e6e6ff",outline="#aaaaaa",width=2)]]
            elif self.selected==3: #door
                self.objects+=[[self.draw.create_rectangle(event.x-20*self.oscale,event.y-30*self.oscale,event.x+20*self.oscale,event.y+30*self.oscale,fill="#000000",outline="#000000"),\
                                self.draw.create_oval     (event.x+11*self.oscale,event.y- 4*self.oscale,event.x+18*self.oscale,event.y+ 3*self.oscale,fill="#eeeeee",outline="#eeeeee")]]
            elif self.selected==4: #carpet
                self.objects+=[[self.draw.create_oval     (event.x-40*self.oscale,event.y-40*self.oscale,event.x+40*self.oscale,event.y+40*self.oscale,fill="#99aaff",outline="#0000ff",width=50)]]
            for i in self.blockparts:
                self.draw.tag_raise(i)
            print(self.objects)
        self.draw.bind("<Button-1>",place) #click to place
        def nextobject(event):
            self.selected+=1
            self.selected%=5
            print(self.selected)
        def prevobject(event):
            self.selected-=1
            self.selected%=5
            print(self.selected)
        self.master.bind("<Right>",nextobject)
        self.master.bind("<Left>", prevobject)
        def moveblock(event,x,y):
            for i in self.blockparts:
                self.draw.move(i,x*self.oscale,y*self.oscale)
        self.master.bind("<a>",lambda x:moveblock(x,-5,0))
        self.master.bind("<d>",lambda x:moveblock(x,5,0))
        self.master.bind("<w>",lambda x:moveblock(x,0,-5))
        self.master.bind("<s>",lambda x:moveblock(x,0,5))
root = tk.Tk()
app = Application(master=root)
app.mainloop()
