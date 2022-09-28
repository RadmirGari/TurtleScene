from Timmy import chessOutline, squareWhite, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon, triangle, sky
import turtle
import random
turtleColors = ["red", "blue", "fuchsia", "purple", "green", "yellow", "aqua", "chartreuse", "darkgoldenrod", "darkviolet", "gainsboro", "lavenderblush", "skyblue", "chocolate4", "DarkOrchid3", "DeepPink", "DarkViolet", "brown3", "burlywood4", "wheat1", "seashell2", "honeydew4", "honeydew1", "honeydew", "LightSeaGreen", "gold", "firebrick", "firebrick2", "goldenrod3", "DodgerBlue", "DodgerBlue3", "LightSalmon4", "lightpink2", "gray0", "hotpink3", "gray0", "hotpink2", "indianred", "firebrick", "firebrick4", "DarkRed"]
turtleShape = ["circle", "arrow", "triangle", "turtle", "classic", "square"]
def drawDashedLine():
    turtle.pu()
    turtle.pd()
    turtle.forward(10)
    turtle.pu()
    turtle.forward(10)
def drawSpirograph():
    circles = 0
    while circles < 361:
        turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.pd()
        turtle.circle(80)
        turtle.right(1)

def drawDamienHirstPainting(CircleRadius, ColorPalet2, ColorPalet):
    turtle.pu()
    x = -200
    y = -200
    drawing = True
    while drawing:
        circle = 0
        turtle.goto(x, y)
        while circle < 1:
            turtle.color(random.randint(ColorPalet2, ColorPalet), random.randint(ColorPalet2, ColorPalet), random.randint(ColorPalet2, ColorPalet))

            turtle.pd()
            turtle.begin_fill()
            turtle.circle(CircleRadius)
            turtle.pu()
            turtle.end_fill()
            x += 50
            circle += 1
            if x == 250:
                x = -200
                y += 50
                if y == 250:
                    drawing = False

def drawAll10Shapes():
    turtle.colormode(255)
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.pd()
    turtle.circle(-50)
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    triangle(150)
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    square(100, 90)
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pentagon()
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    hexagon()
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    heptagon()
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    octagon()
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    nonagon()
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    decagon()
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.pu()

def drawHouse():
    turtle.pu()
    turtle.goto(random.randint(-300, 300), -20)
    turtle.pd()
    turtle.fillcolor("burlywood4")
    turtle.begin_fill()
    square(80, 90)
    turtle.end_fill()
    turtle.left(60)
    turtle.fillcolor("burlywood")
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(20)
    turtle.setheading(0)
    triangle()
    turtle.end_fill()
    turtle.pu()
    turtle.setheading(0)
    turtle.right(180)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(16)
    turtle.pd()
    turtle.fillcolor("lightblue")
    turtle.begin_fill()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.end_fill()
    turtle.pu()
    turtle.setheading(0)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(60)
    turtle.pd()
    turtle.fillcolor("firebrick3")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(16)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(16)
    turtle.end_fill()
    turtle.pu()
def drawBird():
    turtle.pu()
    randomX = random.randint(-300, 300)
    randomY = random.randint(100, 300)
    turtle.goto(randomX, randomY)
    turtle.pd()
    turtle.circle(10, 180)
    turtle.right(180)
    turtle.circle(10, 180)
    turtle.right(180)
    turtle.pu()
def drawSun():
    turtle.pu()
    turtle.pencolor("yellow")
    turtle.goto(random.randint(-200, -100), random.randint(200, 400))
    turtle.fillcolor("Yellow")
    turtle.begin_fill()
    turtle.pd()
    turtle.circle(50)
    turtle.end_fill()
    turtle.pu()
    turtle.pencolor("black")

def drawTree():
    turtle.pu()
    turtle.fillcolor("brown")
    randomX = random.randint(-300, 300)
    randomY = random.randint(10,100)
    turtle.goto(randomX, -100)
    turtle.pd()
    turtle.begin_fill()
    turtle.forward(9)
    turtle.left(90)
    turtle.forward(randomY)
    turtle.left(90)
    turtle.forward(9)
    turtle.left(90)
    turtle.forward(randomY)
    turtle.right(90)
    turtle.right(90)
    turtle.forward(randomY)
    turtle.end_fill()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(60)
    turtle.right(135)
    turtle.forward(84.84)
    turtle.right(90)
    turtle.forward(84.84)
    turtle.right(135)
    turtle.forward(60)
    turtle.end_fill()


def drawChessBoard():
    trueOrFalse = True
    turtle.pu()
    turtle.goto(-320, 320)
    chessOutline()
    turtle.goto(-256, 320)
    x = 0
    while trueOrFalse:
        squareWhite()
        x += 1
        if x == 4:
            trueOrFalse = False
    turtle.goto(-320, 256)
    x = 0
    trueOrFalse = True
    while trueOrFalse:
        squareWhite()
        x += 1
        if x == 4:
            trueOrFalse = False
    turtle.goto(-256, 192)
    x = 0
    trueOrFalse = True
    while trueOrFalse:
        squareWhite()
        x += 1
        if x == 4:
            trueOrFalse = False
    turtle.goto(-320, 128)
    x = 0
    trueOrFalse = True
    while trueOrFalse:
        squareWhite()
        x += 1
        if x == 4:
            trueOrFalse = False
    turtle.goto(-256, 64)
    x = 0
    trueOrFalse = True
    while trueOrFalse:
        squareWhite()
        x += 1
        if x == 4:
            trueOrFalse = False
    turtle.goto(-320, 0)
    x = 0
    trueOrFalse = True
    while trueOrFalse:
        squareWhite()
        x += 1
        if x == 4:
            trueOrFalse = False
    turtle.goto(-256, -64)
    x = 0
    trueOrFalse = True
    while trueOrFalse:
        squareWhite()
        x += 1
        if x == 4:
            trueOrFalse = False
    turtle.goto(-320, -128)
    x = 0
    trueOrFalse = True
    while trueOrFalse:
        squareWhite()
        x += 1
        if x == 4:
            trueOrFalse = False
    turtle.goto(0, -300)


def landscape():
    turtle.pu()
    turtle.color("skyblue")
    turtle.fillcolor("skyblue")
    turtle.begin_fill()
    sky()
    turtle.end_fill()
    turtle.pu()
    numberOfBirds = 0
    numberOfTrees = 0
    whyMe = 0
    turtle.left(90)
    numberOfMountains = 0
    drawSun()
    while numberOfBirds < 9:
        drawBird()
        numberOfBirds += 1
    turtle.right(90)
    while numberOfTrees < 11:
        drawTree()
        numberOfTrees += 1
        whyMe += 1
        if whyMe == 1:
            turtle.left(180)
            whyMe = 0
    drawHouse()
turtle.speed(9999999)
turtle.colormode(255)
askingTurtle = True
while askingTurtle:
    whatToDraw = input('What do you want me to draw? Type "Landscape", "spirograph", "DamienHirstPainting", "10Shapes", "chessboard": ').lower()
    if whatToDraw == "landscape":
        landscape()
        turtle.pu()
        turtle.goto(random.randint(-400, 400), random.randint(-300, 300))
        turtle.colormode(255)
        while True:
            turtle.right(random.randrange(40, 100))
            turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            turtle.shape(turtleShape[random.randint(0, 5)])
    elif whatToDraw == "spirograph":
        drawSpirograph()
    elif whatToDraw == "damienhirstpainting":
        drawDamienHirstPainting(10, 0, 255)
    elif whatToDraw == "10shapes":
        drawAll10Shapes()
    elif whatToDraw == "chessboard":
        drawChessBoard()
    turtle.hideturtle()
    turtle.exitonclick()
    playOrNot = input("Do you want to ask again? Y or N").lower()
    if playOrNot == "n":
        askingTurtle = False

print("Cya later alligator")