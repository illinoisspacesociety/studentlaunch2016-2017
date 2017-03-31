from datetime import datetime, timedelta
import RPi.GPIO as GPIO

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
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(CLK, GPIO.OUT, GPIO.HIGH)
	GPIO.setup(DO, GPIO.OUT, GPIO.LOW)
	GPIO.setup(CS, GPIO.OUT, GPIO.HIGH)
	GPIO.setup(DI, GPIO.IN)
	
def get_data(ch):
	data = 0
	i = 0
	t = datetime.now()
	GPIO.OUTPUT(CS, GPIO.LOW)
	GPIO.output(DO, START)
	t = clk_cycle(t)
	GPIO.output(DO, ch[0])
	t = clk_cycle(t)
	GPIO.output(DO, ch[1])
	t = clk_cycle(t)
	GPIO.output(DO, ch[2])
	t = clk_cycle(t)
	while(i<8):
		t = clk_cycle(t)
		data = (data << i) | GPIO.input(DI)
	GPIO.output(CS, GPIO.HIGH)
	t = clk_cycle(t)
	return data
	
def clk_cycle(t):
	ms = 0
	while(ms1 < MIN_P):
		t1 = datetime.now()
		dt = t1 -t
		ms1 = dt.microseconds
	GPIO.output(CLK, 1)
	while(ms2 < 10):
		t2 = datetime.now()
		dt = t2 -t1
		ms2 = dt.microseconds
	GPIO.output(CLK, 0)
	return t2
	
gpio_init()
data = get_data(CH3)
print data
