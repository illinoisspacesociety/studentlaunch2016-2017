from datetime import datetime, timedelta
import RPi.GPIO as GPIO

test_op = 0
test_clock_in = 0
test_data = 1

#VCC (14) to power
#SARS (11) to power
#CLK (12) to Pi
#DO (10) to Pi
#DI (8) to Pi
#CS (1) to Pi
#GND (7) to ground
#CH0 () to acc
#CH1 () to acc
#CH2 () to acc
#CH3 () to acc

CLK = 2
DI = 4
DO = 15
CS = 3
MIN_P = 3

START = 1
CH0 = [1,0,0]
CH1 = [1,1,0]
CH2 = [1,0,1]
CH3 = [1,1,1]

def gpio_init():
	#GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(CLK, GPIO.OUT)
	GPIO.setup(DI, GPIO.OUT)
	GPIO.setup(CS, GPIO.OUT)
	GPIO.setup(DO, GPIO.IN)
	GPIO.output(CLK, 1)
	GPIO.output(DI, GPIO.LOW)
	GPIO.output(CS, GPIO.HIGH)
	
def get_data(ch):
	data = 0
	i = 0
	t = datetime.now()
	GPIO.output(CS, GPIO.LOW)
	GPIO.output(DI, START)
	t = clk_cycle(t)
	GPIO.output(DI, ch[0])
	t = clk_cycle(t)
	GPIO.output(DI, ch[1])
	t = clk_cycle(t)
	GPIO.output(DI, ch[2])
	t = clk_cycle(t)
	print "Data Start"
	while(i<8):
		t = clk_cycle(t)
		data = (data << i) | GPIO.input(DI)
		print GPIO.input(DI)
		i += 1
	GPIO.output(CS, GPIO.HIGH)
	t = clk_cycle(t)
	return data
	
def clk_cycle(t):
	ms1 = 0
	ms2 = 0
	#print "Startig CLK Cycle"
	while(ms1 < MIN_P):
		t1 = datetime.now()
		dt = t1 -t
		ms1 = dt.microseconds
		#print "\tFirst Loop"
	GPIO.output(CLK, 1)
	while(ms2 < MIN_P):
		t2 = datetime.now()
		dt = t2 -t1
		ms2 = dt.microseconds
		#print "\t\tSecond Loop"
	GPIO.output(CLK, 0)
	return t2
	
if(test_clock_in):
	gpio_init()
	#data = get_data(CH0)
	#print data
	#t = datetime.now()
	#GPIO.output(CLK, 0)
	i = 0
	out = 0
	changes = 0
	while(i<100000):
		i += 1
		out1 = GPIO.input(CLK)
		if(out!=out1):
			changes += 1
		out = out1
	#clk_cycle(t)
	print changes
	GPIO.cleanup()

if(test_op):
	gpio_init()
	data = get_data(CH0)
	print data
	t = datetime.now()
	GPIO.output(CLK, 1)
	GPIO.cleanup()

if(test_data):
	gpio_init()
	i = 0
	j = 0
	while(i<1000):
		GPIO.output(DI, GPIO.HIGH)
		j += GPIO.input(DO)
		i += 1
	print j
	GPIO.cleanup()
