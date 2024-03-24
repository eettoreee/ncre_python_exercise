import turtle

# 注意起始的角度，可以依据最后的形态推断
# 本题最终的角度在水平向右，即seth(0)

turtle.pensize(2)
d = 72
for i in range(5):
    turtle.seth(d)
    d += 72
    turtle.fd(200)

# turtle.exitonclick()    # 点击画面时画布才会消失
# turtle.mainloop()
turtle.done()  # 一般使用done函数来避免程序退出
