import turtle 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
scr=turtle.Screen();
t=turtle.Turtle();
scr.setup(800,600)
scr.bgcolor('black')
for x in range(360): 
    t.pencolor(colors[x%6]) 
    t.width(x/100 + 1) 
    t.forward(x) 
    t.left(59)
turtle.bye()