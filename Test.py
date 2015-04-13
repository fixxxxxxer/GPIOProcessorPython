from GPIOProcessor import GPIOProcessor
import time

GP = GPIOProcessor()

x = GP.getPin21()

print x.getValue()
print x.getDirection()

x.out()
print x.getDirection()
for i in range(0,9):
    x.high()
    #print x.getValue()
    time.sleep(.5)
    x.low()
    #print x.getValue()
    time.sleep(.5)



GP.cleanup()
