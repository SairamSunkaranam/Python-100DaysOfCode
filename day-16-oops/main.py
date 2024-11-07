# from turtle import Turtle, Screen
#
# tummy = Turtle()
# tummy.color("pink")
# tummy.shape("turtle")
# tummy.shapesize(10)
#
# tummy.speed(1)
# tummy.forward(100)
#
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align["Pokemon Name"] = "l"
table.align["Type"] = "r"

# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_row(["Adelaide", 1295, 1158259, 600.5])

print(table)

