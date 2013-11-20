import libcommand_center as libcc
import random

def find_mpeg2():
	# Get a list of all files i nthe IN_FOLDER
	recordings = os.listdir(libcc.RECORD_MPEG_FOLDER)
	# Grab the .mpeg files from this list
	mpegs = []
	for r in recordings:
		if rsplit(r,".")[-1] == "mpeg":
			mpegs.append(r)
	
	# Randomply pick an MPEG
	if len(mpegs) == 0:
		return None

	return random.choice(mpegs)

def convert_to_h264(fn):
	# If Temporary file exists, delete it
	if os.exists(libcc.TRANSCODE_TEMP_FILENAME):
		os.remove(libcc.TRANSCODE_TEMP_FILENAME)

	# Get Video Length in seconds

	# Get Base filename
	base_fn = rsplit(fn,".",1)[0]
	# Start the Transcoding
	proc = subprocess.Popen(libcc.TRANSCODE_COMMAND+
				[
					"-i",libcc.RECORD_MPEG_FOLDER+fn,
					libcc.TRANSCODE_TEMP_FILENAME
				]
			)

	start_time = time.time()
	while( time.time() < start_time + TIMEOUT):
		ret = proc.poll()
		if ret != None:
			# TODO Check if Return code is successful
			os.remove(libcc.RECORD_MPEG_FOLDER+fn)
			os.rename(libcc.TRANSCODE_TEMP_FILENAME,
				libcc.TRANSCODE_OUT_FOLDER+base_fn+"."
				+libcc.CONTAINER)
			return
		
		# Send update to command center
		time.sleep(10)

	# Timeout has been reached

	# Kill process and remove the temp file
	proc.kill()
	proc.wait()

	os.remove(TRANSCODE_TEMP_FILENAME)

	# Communicate Error to Commadn Center
	req = {
		"source":"transcoder",
		"message":"Error - Transcoding of %s Timed Out."%base_fn
		}


def loop_forever():
	while True:
		# Grab an MPEG from the IN_FOLDER
		filename = find_mpeg2()
		# If nothing, wait for a minute
		if filename == None:
			time.sleep(60)
		else:
			# Convert the MPEG to H264
			convert_to_h264(filename)
			time.sleep(10)


if __name__ == "__main__":
	loop_forever()
	
