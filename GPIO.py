class GPIO:
    global PATH
    PATH = "/sys/class/gpio/"
    def __init__(self,pin_number):
        self.pin_number = pin_number

    def openPin(self):
        file = open(PATH + "export",'w')
        file.write(str(self.pin_number))
        file.close()
        
    def closePin(self):
        file = open(PATH + "unexport",'w')
        file.write(str(self.pin_number))
        file.close()

    def setDirection(self,direction):
        file = open(PATH + "gpio" + str(self.pin_number) + "/direction",'w')
        file.write(str(direction))
        file.close()

    def setValue(self,value):
        file = open(PATH + "gpio" + str(self.pin_number) + "/value",'w')
        file.write(str(value))
        file.close()
        
    def getDirection(self):
        file = open(PATH + "gpio" + str(self.pin_number) + "/direction",'r')
        direction = file.read()
        file.close()
        return direction
    
    def getValue(self):
        file = open(PATH + "gpio" + str(self.pin_number) + "/value",'r')
        value = file.read()
        file.close()
        return value

    def high(self):
        self.setValue(1)

    def low(self):
        self.setValue(0)

    def input(self):
        self.setDirection("in")

    def out(self):
        self.setDirection("out")
