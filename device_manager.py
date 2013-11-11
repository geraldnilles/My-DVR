
def loop_forever():
	last_scan = 0
	tuners = None
	while True:
		if time.time()-last_can > 60*60 or tuners == None:
			# Look for devices on the network
			tuners = scan_for_tuners()

		for t in tuners:
			# Gets the tuner status and updates t
			update_tuner_status(t)

		# Send Tuner list to Command Center

		# CHill for a minute
		time.sleep(60)
		
