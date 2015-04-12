class GPIOProcessor:
      
    class GPIO:

        PATH = "/sys/class/gpio/"
	def __init__(self,pin_number):
	    self.pin_number = pin_number

	def open(self):
	    file = open(PATH + "export",'w')
	    file.write(str(pin_number))
	    file.close()
