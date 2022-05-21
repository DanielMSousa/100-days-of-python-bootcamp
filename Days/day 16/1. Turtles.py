from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")

#faz com que o programa continue
# rodando até que você clique na tela

timmy.forward(100)

my_screen = Screen()

print(my_screen.canvheight)

my_screen.exitonclick()