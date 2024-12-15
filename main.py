import turtle
import random
# import colorgram

# colors = colorgram.extract("image-hirst-spot-painting.jpg", 30)
# print(colors)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

turtle.colormode(255)
color_list = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]
tim = turtle.Turtle()
tim.speed(3)
tim.up()
tim.hideturtle()

x = -230
y = -230

for _ in range(10):
    tim.teleport(x, y)
    tim.dot(20, random.choice(color_list))
    for _ in range(9):
        tim.forward(50)
        tim.dot(20, random.choice(color_list))
    y += 50


screen = turtle.Screen()
screen.exitonclick()