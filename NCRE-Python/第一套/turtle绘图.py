from turtle import *

fillcolor('red')
begin_fill()
for i in range(3):
    seth(i*120)
    forward(100)
end_fill()
done()

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)
