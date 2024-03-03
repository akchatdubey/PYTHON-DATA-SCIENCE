from turtle import *
speed(0)
 
def polygon(side,size):
    for i in range(side):
        fd(100)
        lt(360/side) 
        
        
polygon(3,150)
polygon(4,100)
polygon(5,75)
polygon(6,75)
polygon(side=6,size=50)
polygon(7,120)
mainloop()
 