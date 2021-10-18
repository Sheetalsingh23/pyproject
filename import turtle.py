import turtle

turtle.color('blue')
style = ('Arial', 50, 'italic')
turtle.write('Happy Birthday!\nTo you my friend', font=style, align='center')
x = ['red', 'green', 'yellow', 'pink', 'violet']
turtle.right(75)
turtle.color('violet')
turtle.forward(100)
for i in range(5):
    turtle.color(x[i])
    turtle.right(144)
    turtle.forward(100)
turtle.hideturtle()
turtle.exitonclick()
