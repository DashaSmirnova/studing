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
            #inputWindow()            

     
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


# Второе окно со вводом данных             
'''
def inputWindow():
    def printNum(height):
        #global height
        print(height.get())
        print(1)
    height = tk.StringVar()
    window = tk.Tk()
    window.geometry('400x400')
    window.title('Второе окно')
    lab_height  = tk.Label( window, text="Введи высоту(b)")
    lab_height.pack()
    
    entry = tk.Entry(window, textvariable=height)
    entry.pack()
    but = tk.Button(window, text='Нарисовать фигуру и рассчитать площадь', command=printNum(height))

  #  but.bind('<Button->', printNum())
    but.pack()

    #val = StringVar()
   # val.set(val_.get())
    #entry = Entry(window, textvariable=val)
    #entry.pack()
 
    window.mainloop()
    
'''
def newWindow():
                    global root
                    root = tk.Tk()
                    Example(root).pack(fill="both", expand=True)
                    #window.mainloop()
                    #root.destroy()
def inputWindow():
                def display_full_name():
                    tk.messagebox.showinfo("GUI Python", height.get() + " " + width.get())
                    global root
                    try:
                        root.destroy()
                    except:
                        pass
                    #window.mainloop()
                    newWindow()

                    #inputWindow()
                    #root.mainloop()

                window = tk.Tk()
                height = tk.StringVar( window)
                width = tk.StringVar( window)
                r = tk.StringVar( window)
                R = tk.StringVar( window)
                
                height_label = tk.Label(window,text="Введите ширину:")
                width_label = tk.Label(window,text="Введите высоту:")
                r_label = tk.Label(window,text="Введите радиус внутреннего круга:")
                R_label = tk.Label(window,text="Введите радиус кругов: по краям")
                 
                height_label.grid(row=0, column=0, sticky="w")
                width_label.grid(row=1, column=0, sticky="w")
                r_label.grid(row=2, column=0, sticky="w")
                R_label.grid(row=3, column=0, sticky="w")
                
                height_entry = tk.Entry(window,textvariable=height)
                width_entry = tk.Entry(window,textvariable=width)
                r_entry = tk.Entry(window,textvariable=r)
                R_entry = tk.Entry(window,textvariable=R)
                
                height_entry.grid(row=0,column=1, padx=5, pady=5)
                width_entry.grid(row=1,column=1, padx=5, pady=5)
                r_entry.grid(row=2,column=1, padx=5, pady=5)
                R_entry.grid(row=3,column=1, padx=5, pady=5)     
                 
                message_button = tk.Button(window,text="Click Me", command=display_full_name)
                message_button.grid(row=5,column=1, padx=5, pady=5, sticky="e")
                window.mainloop()
           
    
if __name__ == "__main__":
        root = tk.Tk()
        Example(root).pack(fill="both", expand=True)
        inputWindow()
        root.mainloop()
        
