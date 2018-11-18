import time
import sys

def waiting(send):
	s = '.'
	sys.stdout.write( 'Sending' )
	while True:
	        sys.stdout.write( s )
	        sys.stdout.flush()
	        time.sleep(0.5)