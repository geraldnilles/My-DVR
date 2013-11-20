import subprocess
import ctypes
import libcommand_center as libcc

#----------------
# Define C Structs
#---------------

# Devcie Struct for HDHomeRun Discover function
class hdhomerun_discover_device(ctypes.Structure):
	_fields_ = [
			("ip_addr",ctypes.c_long),
			("device_id",ctypes.c_long),
			("device_type",ctypes.c_long),
			("tuner_count",ctypes.c_char)
		]

#--------------
# Define C Library
#-------------

libhdhomerun = ctypes.CDLL("libhdhomerun.so")


## Returns a List of Device IDs
def discover_devices():
	# Create an Array of 5 devices
	devices = (hdhomerun_discover_device * 5)()

	# Search for devices and put them in the array
	num_devices = libhdhomerun.hdhomerun_discover_find_devices_custom( 
			ctypes.c_long(0), # Filter IP Address (0 ==> no filter) 
			ctypes.c_long(0x00000001), # Filter Device Type (None)
			ctypes.c_long(0xFFFFFFFF), # Filter Device ID (None)
			devices , # Search result Array
			ctypes.c_int(5)) # Max Num of results Allowed
		
	if num_devices <= 0:
		print "No devices Found"
		return None

	print "Number of Devices:",num_devices

	# Prepare the Message
	output = []
	for i in range(num_devices):
		d = {}
		d["ip"] = hex(devices[i].ip_addr) # TODO Convert to IP string
		d["id"] = hex(devices[i].device_id)
		output.append(d)

	# Set devices to command center
	req = {
		"source":"device_manager",
		"message":"OK",
		"devices":output
		}
	libcc.send_recv(output)

	return output

def loop_forever():
	last_discover = 0
	tuners = None
	while True:
		if time.time() > last_discover + 60*10:
			discover_devices()

		
		time.sleep(60)

if __name__ == "__main__":
	loop_forever()
