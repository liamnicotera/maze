import turtle as trtl
import random as rand
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

#define variables and turtle for maze 

walls = 0
wall_color = "red"
path_width = 20
wall_length = 0
a = trtl.Turtle()
maze_runner = trtl.Turtle()
a.setheading(90)
a.pensize(5)
a.speed('fastest')
a.hideturtle()


#create maze walls 
wn.tracer(False)
for set in range(41):
    if walls <= 5:
        a.penup()
        a.fd(10)
        a.fd(path_width*2)
        a.fd(60)
        a.forward(wall_length)
        a.left(90)
        wall_length = wall_length + 20
        walls = walls + 1
    else:
        a.pendown()
        door = rand.randint(path_width*2, (wall_length - path_width*2))
        barrier = rand.randint(path_width*2, (wall_length - path_width*2))
        if abs(barrier - door) <= path_width*2:
            door = rand.randint(path_width*2, (wall_length - path_width*2))
            barrier = rand.randint(path_width*2, (wall_length - path_width*2))
        if door < barrier:
            a.fd(door)
            a.penup()
            a.fd(path_width*2)
            a.pendown()
            a.fd(barrier - door)
            a.left(90)
            a.fd(path_width*2)
            a.back(path_width*2)
            a.right(90)
            a.fd(wall_length - door - (barrier - door))
            a.left(90)
            wall_length = wall_length + 20
            walls = walls + 1
        if barrier < door:
            a.fd(barrier)
            a.left(90)    
            a.fd(path_width*2)
            a.back(path_width*2)
            a.right(90)
            a.fd(door - barrier)
            a.penup()
            a.fd(path_width*2)
            a.pendown()
            a.fd(wall_length - barrier - (door - barrier))
            a.left(90)
            wall_length = wall_length + 20
            walls = walls + 1   


#create maze runner
wn.tracer(True)
maze_runner.penup()
maze_runner.goto(-100,75)
maze_runner.setheading(0)
maze_runner.pendown()
maze_runner.showturtle()
maze_runner.speed('fastest')
def up():
    maze_runner.speed('fastest')
    maze_runner.setheading(90)
    maze_runner.speed(1)

def down():
    maze_runner.speed('fastest')
    maze_runner.setheading(270)
    maze_runner.speed(1)

def left():
    maze_runner.speed('fastest')
    maze_runner.setheading(180)
    maze_runner.speed(1)

def right():
    maze_runner.speed('fastest')
    maze_runner.setheading(0)
    maze_runner.speed(1)

def move_runner():
    maze_runner.speed(1)
    for set in range(500):
        maze_runner.fd(7)
        mx = maze_runner.xcor()
        my = maze_runner.ycor()
        if mx > 335:
            maze_runner.hideturtle()
            maze_runner.penup()
            a.clear()
            maze_runner.clear()
            maze_runner.goto(-100,0)
            font_setup = ("Arial", 20, "normal")
            maze_runner.write("Congratulations, you solved the maze!", font=font_setup)
        if mx < -500:
            maze_runner.hideturtle()
            maze_runner.penup()
            a.clear()
            maze_runner.clear()
            maze_runner.goto(-100,0)
            font_setup = ("Arial", 20, "normal")
            maze_runner.write("Congratulations, you solved the maze!", font=font_setup)
        if my > 500:
            maze_runner.hideturtle()
            maze_runner.penup()
            a.clear()
            maze_runner.clear()
            maze_runner.goto(-100,0)
            font_setup = ("Arial", 20, "normal")
            maze_runner.write("Congratulations, you solved the maze!", font=font_setup)
        if my < -335:
            maze_runner.hideturtle()
            maze_runner.penup()
            a.clear()
            maze_runner.clear()
            maze_runner.goto(-100,0)
            font_setup = ("Arial", 20, "normal")
            maze_runner.write("Congratulations, you solved the maze!", font=font_setup)

wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(move_runner, "g")

wn.listen()
wn.mainloop()