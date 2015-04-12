from GPIO import GPIO
import time



x = GPIO(6)
x.openPin()
print x.getDirection()
x.setDirection("out")
print x.getDirection()
for i in range(0,9):
    x.setValue(1)
    print x.getValue()
    time.sleep(.5)
    x.setValue(0)
    print x.getValue()
    time.sleep(.5)


x.closePin()
