# -*- coding: utf-8 -*-
from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent        
        self.initUI()        
    def initUI(self):
        self.parent.title("Вычисление площади")        
        self.pack(fill=BOTH, expand=1)
        a = 7*40 # Ширина 
        b = 4*40 # Высота 
        R = 2*40 # Большой радиус 
        r=1*40 #радиус в центре 
        canvas = Canvas(self)
        # Прямоугольник 
        canvas.create_rectangle(10, 10, a +10 , b +10, 
            outline="black",  width=2)
        # Дуги на концах прямоугольника
        # Верхняя левая
        canvas.create_arc(10 - R,10 - R, 10 + R, 10 + R, start=0, 
            extent=-90, outline="black", fill = "gray",width=1)
        # Нижняя левая
        canvas.create_arc(10 - R,10 +  b - R, 10  + R, 10 + b + R, start=0, 
            extent=90, outline="black",fill = "gray", width=1)
        # Верхняя правая
        canvas.create_arc(10 - R + a,10 - R, 10 + R+ a, 10 + R, start=-90, 
             extent=-90, outline="black",fill = "gray", width=1)
       # Нижняя правая
        canvas.create_arc(10 - R + a,10 - R + b, 10 + R+ a, 10 + R + b, start=90, extent=90, outline="black",fill = "gray", width=1)
        # Центральный круг
        canvas.create_oval(a//2 + 10 - r, b//2+ 10-r, a/2 + 10 +r, b//2+10+r, outline="black", fill = "gray",
            width=1)   
        canvas.pack(fill=BOTH, expand=1)
   
def main():
    root = Tk()
    ex = Example(root)
    root.geometry("330x220+600+600")
    root.title("Вычисление площади фигуры")
    root.mainloop()  

if __name__ == '__main__':
    main()
