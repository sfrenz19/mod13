import setup
from setup import RPL
import time
start = time.time()

x = 0
while x <= 5:
    start = time.time()
    z = 7
    while z == 7:
        current = time.time()

        if current - start < 50:
            RPL.servoWrite(1,500)
            RPL.servoWrite(0,2500)
        elif current - start > 50 and current - start < 100:
            RPL.servoWrite(1,2500)
            RPL.servoWrite(0,500)
        if current - start > 100:
            z = 9
    x +=1
    print "loop %s" % x
