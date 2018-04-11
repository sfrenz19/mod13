import setup
from setup import RPL
z = 3
rear = 17
left = 1
right = 0
while z == 3
    while RPL.readDist(rear) > 70000:
        RPL.servoWrite(0,2500)
        RPL.servoWrite(1,1499)
    while RPL.readDist(rear) > 40000:
        RPL.servoWrite(0,1500)
        RPL.servoWrite(1,500)

    if RPL.readDist(rear) > 1000:
        RPL.servoWrite(0,0)
        RPL.servoWrite(1,0)
        z = 5

print "Task Complete"
