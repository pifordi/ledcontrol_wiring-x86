from wiringx86 import GPIOGalileo as Galileo

gpio = Galileo(debug = True)

def pinnumber(pin):
    if pin >= 14 or pin <=1:
	return "Pin is not defined";
    else:
	return pin;

def turnmode(level):
    if level == "on":
	level = gpio.HIGH
    elif level == "off":
	level = gpio.LOW
    else:
	return "Turn mode is not defined";
	
    return level;

while True:
    pin = int(raw_input("Enter pin number between 2-13: "))
    level = raw_input("Enter turn mode on/off: ")

    gpio.pinMode(pinnumber(pin), gpio.OUTPUT)
    gpio.digitalWrite(pinnumber(pin), turnmode(level))
