from quick2wire.i2c import I2CMaster, writing_bytes, reading

test_i2c = 1

if(test_i2c):
	#bus = smbus.SMBus(1)
	address = 0x76
	cmd = 0x00
	press = 0
	with I2CMaster() as master:
		master.transaction(writing_bytes(address,0x40))
		press = master.transaction(writing_bytes(address,cmd),reading(address,3))
	#press = bus.read_block_data(address,0x00)
	#bus.write_byte_data(address,0,0x1E)
	#bus.write_byte_data(address,0,0x00)
	#pres = bus.read_i2c_block_data(address,0,3)
	#stuff = press[0][0]
	for stuff in press[0]:
		print(stuff)
