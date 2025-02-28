import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)      
bgcolor("black") 
penup()          
goto(0, -200)    
pendown()        
color("red")     

for i in range(0, 628, 1):  
    x = hearta(i * 0.1) * 20  
    y = heartb(i * 0.1) * 20  
    goto(x, y)

done()
