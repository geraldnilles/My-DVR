import os
import uuid
import time.sleep
import libcommand_center as libcc

MPEG_FOLDER = "/mnt/raid/Recordings/.mpeg/"

def record(device_id, tuner_number, legnth, filename):
	tempname = libcc.RECORD_MPEG_FOLDER+str(uuid.uuid1())

	libcc.send_recv({
		"source":"recorder",
		"message":"Recording Started on Tuner "+str(tuner_number)
		})

	proc = subprocess.Popen([
				"hdhomerun_config",
				deviceID,
				"save",
				"/tumer"+str(tuner_number),
				tempname])

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
	parser = argparse.ArgumentParser(description=
			"Record Stream from HDHomeRun Prime Tuner")
	parser.add_argument("--id",help="HDHomeRune Device ID Hex String")
	parser.add_argument("--tuner",
				help="Tuner Number to use", 
				type=int,
				default=0)
	parser.add_argument("--length",
				help="Length of recording (in seconds)",
				type=int,
				default=60*60)
	parser.add_argument("--outfile",
				help="Output MPEG file name")

	args = parser.parse_args()

	# TODO Verify the ID hex value is correct
	if len(args.id) != 8:
		print "Error! Tuner ID value is not the correct length."
		parser.print_usage()
		exit()

	for x in args.id:
		if x not in [	"A","B","C","D","E","F",
				"a","b","c","d","e","f",
				"1","2","3","4","5","6","7","8","9","0"]:
			print "Error! Tuner ID is not a Hex value"
			parser.pring_usage()
			exit()
	

	# Record the Stream
	record(args.id, args.tuner , args.length, args.outfile)

