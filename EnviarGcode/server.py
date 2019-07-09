import eel
import time
import serial
import time
import argparse

eel.init('web')

@eel.expose
def getTime():
    return time.strftime('%c')

@eel.expose    
def enviarGcode(gcode):
	s = serial.Serial('/dev/ttyUSB0',9600,timeout=5)
	time.sleep(2) 
	#s = serial.Serial('/dev/ttyACM0',9600)
	print ( 'Abrindo porta serial' )
	
	f = open(gcode,'r') 
	print ( 'Abrindo gcode' )   
	time.sleep(3)   					  # Wait for Printrbot to initialize
	s.flushInput()
	s.flushOutput()  					  # Flush startup text in serial input
	print ( 'Enviando gcode' )
	
	for line in f:
		l = line
		l = l.rstrip('\r\n')					  # Strip all EOL characters for streaming
		if  (len(l)>0) :
			for b in l: 								
				d = bytearray(b'b')
				s.write(b)
				s.flush()
				s.flushInput()
				s.flushOutput() 
					
		s.flush() 
		grbl_out = s.readline()
		while(b'done' not in grbl_out): 
			grbl_out = s.readline()
			time.sleep(2)
			print ( ' : ' + grbl_out )
			
		s.flushInput()
		s.flushOutput()
	
	# Close file and serial port
	f.close()
	s.close()		

eel.start('main.html')
