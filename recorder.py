

def record(tuner, legnth, filename):
	proc = subprocess.Popen("hdhomerun_config...")

	start_time = time.time()
	# Loop for as long as the process is alive
	while proc.poll() == None:
		if time.time()-starttime > length:
			# Report Completion to Command Center
			proc.terminate() # or proc.kill?
			break
		# Read the STDOUT
		# Report back to Command Ctner
		resp = update_progress(tuner,filename)
		if resp["message"] == "KILL":
			# Report KILL to Command Center
			proc.terminate()
			break


	proc.wait()

	# Move from Temp directory to Recordings directory

