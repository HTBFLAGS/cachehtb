import turtle
turtle.penup()
turtle.goto(-100,100)
turtle.color(“black”)

#First draw orange box. Instruct pen that it has to fill # FF9933 (orange) color.  Change its position to left 90 degrees. Move 90 pixels forward. Turn 90 degrees right and move 600 pixels forward. Turn right 90 degrees, move 90 pixels, again turn right 90 degrees and move 600 pixels forward. Here your orange section is completed and now instruct pen to stop coloring.

#orange

turtle.pendown()
turtle.begin_fill()
turtle.fillcolor(“#FF9933”)
turtle.left(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(600)
turtle.end_fill()

#white and Ashoka Chakra

#Remember we have to draw ashoka chakra. So when your pen is half way down drawing the line of white section, draw a circle and then continue your journey of drawing line. Here, horizontal line is of 600 pixels and vertical is of 90 pixes for each section of flag. So once pen reaches 300 pixels, initiate a circle with a radius of 45 pixels (vertical line length/2 = 90pixels/2 = 45pixels). Remember to fill it with blue colour.

turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(300)
turtle.begin_fill()
turtle.fillcolor(“blue”)
turtle.circle(45)
turtle.end_fill()
turtle.forward(300)
turtle.left(90)
turtle.forward(90)

#come back to the start of line 3
turtle.penup()
turtle.goto(-100,10)
turtle.right(180)

#green
turtle.begin_fill()
turtle.fillcolor(“#138808”)
turtle.pendown()
turtle.forward(90)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(90)
turtle.end_fill()

#come back to line 4
turtle.penup()
turtle.goto(-100,-80)
turtle.right(180)