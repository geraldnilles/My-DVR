import libcommand_center as libcc
import time
import asyncore


# Once a connection is established (using the Connection_handler), this will
# handle reading and writing to the connection.
class Message_Handler(asyncore.dispatcher):
	def __init__(self,sock,db):
		# Initialize the Handler using the given socket
		asyncore.dispatcher.__init__(self,sock)

		# Create buffers for sending/reeiving data from TCP sockets
		self.read_buffer = ""
		self.write_buffer = ""

		# Keep track of the DB reference
		self.db = db

	def writable(self):
		if len(write_buffer) > 0:
			return True

		return False

	def handle_write(self):
		# Send the write buffer over the socket
		sent = self.send(self.write_buffer)
		# Clear the part of the write buffer that was sent
		self.write_buffer[sent:]

	# This method reads chuncks of data from the subprocesses
	def handle_read(self):
		# Read stream data to the buffer
		self.read_buffer += self.recv(1024)
		# Attempt to decode the buffer into a JSON packet
		req, size = libcc.pkt_to_json(self.read_buffer)
		# If the request object is None, return and wait for more data
		if req == None:
			return
		else:
			# Packet was created successfully
			self.prepare_response(req)
			# Adjust the read_buffer
			self.read_buffer = self.read_buffer[size:]
	
	def prepare_response(self,req):
		# Eventually, this wil parse the request and create a valid 
		# response.  For now, it will jsut respond with the default 
		# packet

		resp = {
				"source":"command_center",
				"message":"OK"
				}

		if resp["messsage"] != None:
			self.write_buffer += libcc.json_to_pkt(resp)


# This handler will listen for new Unix Socket connections
class Connection_Handler(asyncore.dispatcher):
	def __init__(self):
		# Initialize the original class
		asyncore.dispatcher.__init__(self)

		# Delete the Unix socket if it already exists
		if(os.path.exists(libcc.UNIX_SOCKET_PATH)):
			os.remove(libcc.UNIX_SOCKET_PATH)
	
		# Create a Unix socket to listen to
		self.create_socket(socket.AF_UNIX, socket.SOCK_STREAM)
		self.bind(libcc.UNIX_SOCKET_PATH)
		self.listen(5)

		# Initialize the Database(s)
		self.db = {
			"tuners":[],
			"events":[]
				}

	def handle_accept(self):
		# Create a new Message handler
		sock,addr = self.accept()
		Message_Handler(sock,self.db) # Send a reference to the DB
	
	def _write_db(self):
		# Write DB to Disk
		pass # Do nothign now




if __name__ == "__main__":
	ch = Connection_Handler()
	ps = libcc.get_process_list()


	watchdog_period = 10 #seconds
	watchdog_time = time.time() + watchdog_period
	while(1):
		# Wait for connections
		asyncore.loop(timeout=1,count=10)

		# After 10 timeouts, verify that its been at least 10 seconds
		if time.time() > watchdog_time:
			# Reset the timer
			watchdog_time = time.time() + watchdog_period
			
			# Check processes
			libcc.check_processes(ps)
			cc._write_db()
			
