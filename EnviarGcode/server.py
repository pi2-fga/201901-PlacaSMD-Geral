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
	s = serial.Serial('/dev/ttyACM0',9600)
	print ( 'Abrindo porta serial' )
	
	f = open(gcode,'r') 
	print ( 'Abrindo gcode' )   
	s.write(("\r\n\r\n").encode('utf-8')) # Hit enter a few times to wake the Printrbot
	time.sleep(3)   					  # Wait for Printrbot to initialize
	s.flushInput()  					  # Flush startup text in serial input
	print ( 'Enviando gcode' )
	
	for line in f:
		l = line
		l = l.strip() 					  # Strip all EOL characters for streaming
		if  (l.isspace()==False and len(l)>0) :
			print ( 'Enviando: ' + l )
			s.write(l) 					  # Send g-code block
			grbl_out = s.read(10) 		  # Wait for response with carriage return
			print ( ' : ' + grbl_out.strip() )
		 
	
	# Close file and serial port
	f.close()
	s.close()		

eel.start('main.html')
