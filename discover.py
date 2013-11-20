
import ctypes




## Returns a List of Device IDs
def find_devices():
	# Create an Array of 10 devices
	devices = (hdhomerun_discover_device * 5)()

	# Search for devices
	num_devices = libhdhomerun.hdhomerun_discover_find_devices_custom( 
			ctypes.c_long(0), # Filter IP Address (0 ==> no filter) 
			ctypes.c_long(0x00000001), # Filter Device Type (None)
			ctypes.c_long(0xFFFFFFFF), # Filter Device ID (None)
			devices , # Search result Array
			ctypes.c_int(5)) # Max Num of results Allowed
		
	if num_devices <= 0:
		print "No devices Found"
		return -1

	print "Number of Devices:",num_devices
	print "Device Type:",hex(devices[0].device_type)
	print "IP:", hex(devices[0].ip_addr)
	print "ID:", hex(devices[0].device_id)

	return devices



def run():
	print repr(libhdhomerun)
	print find_devices()

run()


