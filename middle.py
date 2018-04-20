import setup
from setup import RPL
z = 3
rear = 17
left = 1
right = 0
while z == 3:
    while RPL.readDistance(rear) > 70000:
        RPL.servoWrite(1,2500)
        RPL.servoWrite(0,1499)
    while RPL.readDistance(rear) > 40000:
        RPL.servoWrite(1,1500)
        RPL.servoWrite(0,500)

    if RPL.readDistance(rear) < 1000:
        RPL.servoWrite(0,0)
        RPL.servoWrite(1,0)
        z = 5

print "Task Complete"
