
def download_listing():
	# Download the LIst XML file
	# Load as an eTree file?
	return listing

def loop_forever():
	# Initialize Loop Variables
	last_download = 0;
	listing = None
	while True:
		# If Listing data is old, refresh it
		if time.time() - last_download > 60*60 or listing == None:
			listing = download_listing()

		# Get a list of rules from the command center
		recording_rules = get_rules()

		# Check each recording rule for a list of matches
		for rule in recording_rules:
			matches = find_matches(listing, rule)
			# For each match, scheudle a recording with the 
			# command center
			for m in matches:
				schedule_recording(m)

		# Sleep for 1 minute
		time.sleep(60)
		
