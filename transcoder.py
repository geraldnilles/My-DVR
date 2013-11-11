
def find_mpeg2():
	recordings = os.listdir(RECORDING_FOLDER)
	for r in recordings:
		if r.split(r,".")[-1] == "mpeg":
			return r
	return None

def convert_to_h264(fn):
	# Get Video Length in seconds

	subprocess.Popen(["avconv","-i",RECORDING_FOLDER+fn])
	# Get COnversion progress
	# Report Conversion progress to Command Center



def loop_forever():
	while True:
		filename = find_mpeg2()
		if filename == None:
			time.sleep(60)
		else:
			convert_to_h264(filename)
			time.sleep(10)
	
