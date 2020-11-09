from turtle import *

speed(-1)

color_list= ['red'
,'blue',
'brown' ,
 'yellow', 
 'green', 
 'grey', 
 'purple']

edge = 1

for edge in range (2,7,1):
    print(edge)
    for i in range(edge):
        begin_fill(color_list)
        forward(100)
        left(360/edge)

mainloop ()
