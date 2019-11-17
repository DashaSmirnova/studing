import tkinter as tk
import random
     
pressed = False
     
class Example(tk.Frame):
        def __init__(self, root):
            tk.Frame.__init__(self, root)
            self.canvas = tk.Canvas(self, width=400, height=400, background="bisque")
            self.xsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
            self.ysb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
            self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
            self.canvas.configure(scrollregion=(0,0,1000,1000))
     
            self.xsb.grid(row=1, column=0, sticky="ew")
            self.ysb.grid(row=0, column=1, sticky="ns")
            self.canvas.grid(row=0, column=0, sticky="nsew")
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
     
            #Plot some rectangles
            #self.canvas.create_text(50,10, anchor="nw", text="Click and drag to move the canvas\nScroll to zoom.")
            a = 7*40 # Ширина 
            b = 4*40 # Высота 
            R = 2*40 # Большой радиус 
            r=1*40 #радиус в центре 
            # Прямоугольник 
            self.canvas.create_rectangle(10, 10, a +10 , b +10, 
                outline="black",  width=2)
            # Дуги на концах прямоугольника
            # Верхняя левая
            self.canvas.create_arc(10 - R,10 - R, 10 + R, 10 + R, start=0, 
                extent=-90, outline="black", fill = "gray",width=1)
            # Нижняя левая
            self.canvas.create_arc(10 - R,10 +  b - R, 10  + R, 10 + b + R, start=0, 
                extent=90, outline="black",fill = "gray", width=1)
            # Верхняя правая
            self.canvas.create_arc(10 - R + a,10 - R, 10 + R+ a, 10 + R, start=-90, 
                 extent=-90, outline="black",fill = "gray", width=1)
           # Нижняя правая
            self.canvas.create_arc(10 - R + a,10 - R + b, 10 + R+ a, 10 + R + b, start=90, extent=90, outline="black",fill = "gray", width=1)
            # Центральный круг
            self.canvas.create_oval(a//2 + 10 - r, b//2+ 10-r, a/2 + 10 +r, b//2+10+r, outline="black", fill = "gray",
                width=1)   


            # This is what enables using the mouse:
            self.canvas.bind("<ButtonPress-1>", self.move_start)
            self.canvas.bind("<B1-Motion>", self.move_move)
     
            self.canvas.bind("<ButtonPress-2>", self.pressed2)
            self.canvas.bind("<Motion>", self.move_move2)
     
            #linux scroll
            self.canvas.bind("<Button-4>", self.zoomerP)
            self.canvas.bind("<Button-5>", self.zoomerM)
            #windows scroll
            self.canvas.bind("<MouseWheel>",self.zoomer)
            # Hack to make zoom work on Windows
            root.bind_all("<MouseWheel>",self.zoomer)
     
        #move
        def move_start(self, event):
            self.canvas.scan_mark(event.x, event.y)
        def move_move(self, event):
            self.canvas.scan_dragto(event.x, event.y, gain=1)
     
        #move
        def pressed2(self, event):
            global pressed
            pressed = not pressed
            self.canvas.scan_mark(event.x, event.y)
        def move_move2(self, event):
            if pressed:   
                self.canvas.scan_dragto(event.x, event.y, gain=1)        
     
        #windows zoom
        def zoomer(self,event):
            if (event.delta > 0):
                self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
            elif (event.delta < 0):
                self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
            self.canvas.configure(scrollregion = self.canvas.bbox("all"))
     
        #linux zoom
        def zoomerP(self,event):
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
            self.canvas.configure(scrollregion = self.canvas.bbox("all"))
        def zoomerM(self,event):
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
            self.canvas.configure(scrollregion = self.canvas.bbox("all"))
     
if __name__ == "__main__":
        root = tk.Tk()
        Example(root).pack(fill="both", expand=True)
        root.mainloop()
