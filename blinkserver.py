import BaseHTTPServer
import time
from blink1.blink1 import Blink1

b1 = Blink1()

class SimpleRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print "incoming request: " + self.path
        self.wfile.write('HTTP-1.0 200 Okay\r\n\r\n' + self.path)
		self.wfile.write('\r\n' + modes(self.path))		

def run(server_class=BaseHTTPServer.HTTPServer,
    handler_class=SimpleRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

def doblink(mode, r, g, b):
	print "blink mode received"
	if mode == "flash":
 		b1.fade_to_rgb(1000, 0, 0, 0)
		time.sleep(3)
		b1.fade_to_rgb(1000, r, g, b)
	else:
		b1.fade_to_rgb(1000, r, g, b)
		
	return "ok"

def modes(argument):
	if argument == "/solid/red":
		doblink("solid", 255, 0, 0)
		return "ok"
	elif argument == "/solid/green":
		doblink("solid", 0, 255, 0)
		return "ok"
	elif argument == "/solid/blue":
		doblink("solid", 0, 0, 255)
		return "ok"
	elif argument == "/flash/red":
		doblink("flash", 255, 0, 0)
		return "ok"
	elif argument == "/flash/green":
		doblink("flash", 0, 255, 0)
		return "ok"
	elif argument == "/flash/blue":
		doblink("flash", 0, 0, 255)
		return "ok"
	elif argument == "/clear":
		doblink("solid", 0, 0, 0)
	else:
		return "invalid"
	
run()