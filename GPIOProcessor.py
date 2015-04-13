from GPIO import GPIO

class GPIOProcessor:

    def __init__(self):
        self.GPIOList = []
        from GPIO import GPIO
        
    def getPin(self, pin_number):
        pin = GPIO(pin_number)
        pin.openPin()
        self.GPIOList.append(pin)
        return pin

    def getPin21(self):
        return self.getPin(6)

    def getPin22(self):
        return self.getPin(7)

    def getPin23(self):
        return self.getPin(206)

    def getPin24(self):
        return self.getPin(207)

    def getPin25(self):
        return self.getPin(186)

    def getPin26(self):
        return self.getPin(189)

    def getPin27(self):
        return self.getPin(22)

    def getPin28(self):
        return self.getPin(23)

    def cleanup(self):
        for pin in self.GPIOList:
            pin.input()
            pin.closePin()
            self.GPIOList.remove(pin)
        







        
        
