print("Cao Văn Dũng")
print("MSSV:235752020710031")
print("#####################")
import turtle
colors = ["red","green","orange","purple","pink","yellow"]
painter = turtle.Turtle()
painter.pensize(3)
for i in range(10):
    color = choices(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0)
