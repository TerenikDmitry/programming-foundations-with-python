import turtle

def draw_square(turtle_obj, length):
	for i in range(0,4):
			turtle_obj.forward(length)
			turtle_obj.right(90)

def draw_rhombus(turtle_obj, length, angle):
	for i in range(0,2):
			turtle_obj.forward(length)
			turtle_obj.right(angle)
			turtle_obj.forward(length)
			turtle_obj.right(180 - angle)

def draw_art():
	screen = turtle.Screen()
	screen.setup(width=.5, height=.5, startx=None, starty=None)
	screen.bgcolor("#5B13FF")
	screen.title("Drawing")

	brad = turtle.Turtle()
	brad.shape("circle")
	brad.color("#FFFFFF")
	brad.speed(.2)
	for x in range(0,36):
		draw_rhombus(brad, 60, 40)
		brad.right(10)
	brad.right(90)
	brad.forward(175)

	screen.exitonclick()

draw_art()