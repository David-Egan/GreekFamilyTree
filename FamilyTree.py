import turtle
from math import sqrt, tan, radians

## Classes ##
class Brother:
    def __init__(self, tree, row, column, bigColumn, status, pledgeClass, roll, name):
        self.tree = tree
        self.roll = roll
        self.name = name
        self.row = row
        self.column = column
        self.bigColumn = bigColumn
        self.status = status
        self.pledgeClass = pledgeClass

class Card:
    def __init__(self, base_coord, width, height):
        self.base_x = base_coord[0]
        self.base_y = base_coord[1]
        self.width = width
        self.height = height
        self.setColor("none")
        self.setTextColor("black")
        self.setTilt(0)

    def setColor(self, fill):
        self.fillcolor = fill

    def setTilt(self, tilt):
        self.tilt = tilt
        self.tiltDiff = self.height/tan(radians(90-self.tilt))

    def setTextColor(self, color):
        self.textColor = color

    def drawCard(self, brother):
        self.drawBG()
        self.drawOutline()
        self.drawShadow()
        mybox.drawName(brother)
        mybox.drawFlag()
        mybox.drawPledgeClass(brother)

    def drawBG(self):
        v1 = (self.base_x-(self.width/2), self.base_y)
        v2 = (self.base_x-(self.width/2)+self.tiltDiff, self.base_y+self.height)
        v3 = (v2[0]+self.width, v2[1])
        v4 = (v1[0]+self.width, v1[1])
        self.quadPoly(v1, v2, v3, v4, self.fillcolor)

    def drawOutline(self):
        self.setColor("#003050")
        thick = 1
        v1 = (self.base_x-(self.width/2), self.base_y)
        v2 = (self.base_x-(self.width/2)+self.tiltDiff, self.base_y+self.height)
        v3 = (v2[0]+thick, v2[1])
        v4 = (v1[0]+thick, v1[1])
        self.quadPoly(v1, v2, v3, v4, self.fillcolor)
        v1 = v2
        v2 = (v1[0]+self.width, v1[1])
        newDiff = (self.height-thick)/tan(radians(90-self.tilt))
        v4 = (self.base_x-(self.width/2)+newDiff, self.base_y+self.height-thick)
        v3 = (v4[0]+self.width, v4[1])
        self.quadPoly(v1, v2, v3, v4, self.fillcolor)

    def drawShadow(self):
        self.setColor("#003050")
        thick = 10
        v1 = (self.base_x-(self.width/2), self.base_y)
        newDiff = thick/tan(radians(90-self.tilt))
        v2 = (v1[0]+newDiff, v1[1]-thick)
        v3 = (v2[0]+self.width, v2[1])
        v4 = (v1[0]+self.width, v1[1])
        self.quadPoly(v1, v2, v3, v4, self.fillcolor)
        v1 = (self.base_x+(self.width/2), self.base_y)
        v2 = (self.base_x+(self.width/2)+self.tiltDiff, self.base_y+self.height)
        v3 = (v2[0]+newDiff, v2[1]-thick)
        v4 = (v1[0]+newDiff, v1[1]-thick)
        self.quadPoly(v1, v2, v3, v4, self.fillcolor)

    def drawName(self, brother):
        fname = brother.name.split(' ')[0]
        lname = brother.name.split(' ')[1]

        t.penup()
        t.color(self.textColor)
        t.goto(self.base_x + 30, self.base_y + 26)
        t.write(str(brother.roll)+" "+fname, align="center", font=("Overpass", 20, "normal"))
        t.goto(self.base_x + 30, self.base_y + 6)
        t.write(lname, align="center", font=("Overpass", 20, "normal"))

    def drawFlag(self):
        thick=10
        t.penup()
        v1 = (self.base_x-(self.width/2), self.base_y)
        newDiff = thick/tan(radians(90-self.tilt))
        v2 = (v1[0]-newDiff, v1[1]+thick)
        v3 = (v1[0]+newDiff, v1[1]+thick)
        v4 = v1
        self.quadPoly(v1, v2, v3, v4, "#003050")
        thick = 20
        newDiff = thick/tan(radians(90-self.tilt))
        v1 = v2
        v2 = (v1[0]+newDiff, v2[1]+thick)
        v3 = (v2[0]+40, v2[1])
        v4 = (v1[0]+40, v1[1])
        self.quadPoly(v1, v2, v3, v4, "#003050")

    def drawPledgeClass(self, brother):
        t.color("white")
        letter1 = chr(ord("\u0390") + divmod(brother.pledgeClass,24)[0])
        letter2 = chr(ord("\u0390") + divmod(brother.pledgeClass,24)[1])
        if brother.pledgeClass == 0:
            letter1 = chr(ord("\u0390") + 25)
            letter2 = "C"
        greek_char = letter1 + letter2
        if ord(letter1) == 912:
            greek_char = letter2

        t.goto(self.base_x-(self.width/2)+20, self.base_y+11)
        t.write(greek_char,align="center",font=("Ariel", 15, "normal"))


    def quadPoly(self, v1, v2, v3, v4, fillcolor):
        t.penup()
        t.goto(v1)
        t.pendown()
        if fillcolor != "none":
            t.color(fillcolor, fillcolor)
            t.begin_fill()
        t.goto(v2)
        t.goto(v3)
        t.goto(v4)
        t.goto(v1)
        t.end_fill()
        t.penup() 





## Functions ##
def setRoot():
    t.hideturtle()
    t.speed(0)
    t.penup()

def drawHead(x, y1, y2, width=5, color="#003050"):
    thk = width/2
    v1, v2, v3, v4 = (x-thk,y1), (x-thk,y2+thk), (x+thk,y2+thk), (x+thk,y1)

    t.penup()
    t.color(color)
    t.begin_fill()
    t.goto(v1)
    t.pendown

    t.goto(v2)
    t.goto(v3)
    t.goto(v4)
    t.goto(v1)

    t.end_fill()
    t.penup()

def drawTail(x, y1, y2, width=5, color="#003050"):
    drawHead(x, y1, y2, -width, color)

def drawArm(x1, x2, y, width=5, color="#003050"):
    thk = width/2
    v1, v2, v3, v4 = (x1-thk,y-thk), (x1-thk,y+thk), (x2+thk,y+thk), (x2+thk,y-thk)

    t.penup()
    t.color(color)
    t.begin_fill()
    t.goto(v1)
    t.pendown

    t.goto(v2)
    t.goto(v3)
    t.goto(v4)
    t.goto(v1)

    t.end_fill()
    t.penup()

## ---------------------------- ##


t = turtle;
mybox = Card((0,0),0,0)

def printTreeGraphic(brotherList):
    t = turtle.Turtle()
    setRoot()
    distX = 110
    distY = 110
    global mybox
    for b in brotherList:
        mybox = Card((b.column*distX,150-(b.row*distY)), 180, 60)
        if b.status == 1:
            mybox.setColor("#00a0df")
            mybox.setTextColor("white")
        else:
            mybox.setColor("white")
            mybox.setTextColor("black")
            
        mybox.setTilt(30)
        mybox.drawCard(b)


    ## Save ##
    #t.getscreen().getcanvas().postscript(file = "t1.eps")

    ## END ##
    turtle.done()
    return

## Execute ##
'''
r4 = Brother(4,0,0,0,0,0,4,"Nick Pillon")
r33 = Brother(4,1,0,0,0,0,33,"Chad Rossi")
r40 = Brother(4,2,-2,0,0,3,40,"Vinay Kaushik")
r49 = Brother(4,2,2,0,1,4,49,"James Buxton")
r43 = Brother(4,3,-2,-2,1,4,43,"Ken Postel")
r56 = Brother(4,3,0,2,1,5,56,"Michael Yaeger")
r60 = Brother(4,3,2,2,1,6,60,"Riley Miskewitz")
r76 = Brother(4,3,4,2,0,8,76,"Rahul Sharma")
r67 = Brother(4,4,0,0,1,7,67,"Tim Doores")
brotherList = [r4, r33, r40, r49, r43, r56, r60, r76, r67]

printTreeGraphic(brotherList);
'''
