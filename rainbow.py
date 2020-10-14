#importing turtle package
#“Turtle” is a Python feature like a drawing board,
# which lets us command a turtle to draw all over it! 
#We can use functions like turtle.forward(…) and turtle.right(…) 
#which can move the turtle around.
import turtle
# create a new drawing board(window)-->scr and a turtle object-->pen
scr=turtle.Screen();
pen=turtle.Turtle();

#setting the colors for drawing rainbow
col=['violet','indigo','blue','green','yellow','orange','red']

#setting screen feature and pen configuration
scr.setup(800,600)
scr.bgcolor('black')
pen.right(90)                    #trutle turns clockwise
pen.width(10)                    #set thickness
pen.speed(7)                     #drawing speed

# method to form semi-circles as in a rainbow
def drawSemicircle(colr, radius, position):
    pen.color(colr)             #set the color each time
    pen.circle(radius,-180)     #draw a circle
    pen.up()                    #picks up turtle pen
    pen.setpos(position,0)      #move turtle pen to this position
    pen.down()                  #puts down the turtle pen
    pen.right(180)              #turns the turtle clock wise

#loop to draw the seven semi circles
for i in range(7):
    drawSemicircle(col[i],10*(i+8),-10*(i+1))
#exit turtle window
turtle.bye();