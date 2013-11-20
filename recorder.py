import os
import uuid
import time.sleep
import libcommand_center as libcc

MPEG_FOLDER = "/mnt/raid/Recordings/.mpeg/"

def record(device_id, tuner_number, legnth, filename):
	tempname = libcc.RECORD_MPEG_FOLDER+uuid.uuid().digest()

	libcc.send_recv({
		"source":"recorder",
		"message":"Recording Started on Tuner "+str(tuner_number)
		})

	proc = subprocess.Popen([
				"hdhomerun_config",
				deviceID,
				"save",
				"/tumer"+str(tuner_number),
				tempname]
			)

	# Keep track of the start time.
	start_time = time.time()
	# Loop for as long as the process is alive
	while proc.poll() == None:
		# Check if the recording is complete
		if time.time()-starttime > length:
			# Report Completion to Command Center
			# Send the Kill signal
			proc.kill() # or proc.terminate?
			libcc.send_recv({
				"source":"recorder",
				"message":"Recording Finished on Tuner "
					+str(tuner_number)
				})
			break # Stop the loop
	
		# Read the STDOUT
		# Report back to Command Ctner
		#resp = update_progress(tuner,filename)
		#if resp["message"] == "KILL":
		#	# Report KILL to Command Center
		#	proc.terminate()
		#	break
		time.sleep(5)

	# Wait for the proc to finish up
	proc.wait()

	# Move from Temp directory to Recordings directory
	os.rename(tempname,libcc.RECORD_MPEG_FOLDER+filename)

if __name__ == "__main__":
	# Parse Arguments 
	
	# Record
	record(device_id, tuner_number ,length,filename)
