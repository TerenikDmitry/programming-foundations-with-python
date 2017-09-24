import turtle

def draw_square(turtle_obj):
	for i in range(0,4):
			turtle_obj.forward(75)
			turtle_obj.right(90)

def draw_rhombus(turtle_obj):
	for i in range(0,2):
			turtle_obj.forward(70)
			turtle_obj.right(40)
			turtle_obj.forward(70)
			turtle_obj.right(140)

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
		draw_rhombus(brad)
		brad.right(10)
	brad.right(90)
	brad.forward(175)

	screen.exitonclick()

draw_art()