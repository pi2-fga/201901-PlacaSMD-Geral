#!/usr/bin/python
"""\
Simple g-code streaming script
"""
 
import serial
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p','--port',help='Input USB port',required=True)
parser.add_argument('-f','--file',help='Gcode file name',required=True)
args = parser.parse_args()
 
## show values ##
print ("USB Port: %s" % args.port )
print ("Gcode file: %s" % args.file )

def removeComment(string):
	if (string.find(';')==-1):
		return string
	else:
		return string[:string.index(';')]
 
# Open serial port
#s = serial.Serial('/dev/ttyACM0',115200)
s = serial.Serial(args.port,9600)
print ( 'Abrindo porta serial' )
 
# Open g-code file
#f = open('/media/UNTITLED/shoulder.g','r');
f = open(args.file,'r');
print ( 'Abrindo gcode' )
 
# Wake up 
s.write(("\r\n\r\n").encode('utf-8')) # Hit enter a few times to wake the Printrbot
time.sleep(3)   # Wait for Printrbot to initialize
s.flushInput()  # Flush startup text in serial input
print ( 'Enviando gcode' )
 
# Stream g-code
for line in f:
	l = line
	l = l.strip() # Strip all EOL characters for streaming
	if  (l.isspace()==False and len(l)>0) :
		print ( 'Enviando: ' + l )
		s.write(l) # Send g-code block
		grbl_out = s.read(10) # Wait for response with carriage return
		print ( ' : ' + grbl_out.strip() )
		#command = s.read()
		#print str(command)
 
# Wait here until printing is finished to close serial port and file.
input("  Pressione <Enter> para sair.")
 
# Close file and serial port
f.close()
s.close()
