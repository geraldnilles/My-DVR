
XML_REQUEST_TMPL = ""

SCHEDULES_DIRECT_URL = ""

def fetch_xml_file():
	# See https://github.com/dsoprea/PySchedules/blob/master/pyschedules/retrieve.py for details on how to fetch XML
	
	# Perpare Request XML
	#    - Replace Start and End Date/Time in the Template

	# Create an HTTP Authenticator Handler using Username/password
	#    - Use the urllib2 library

	# Request XML file with GZIP encoding

	# Decompress GZIP

	# Return XML

def download_listing():
	# Download the LIst XML file
	text = fetch_xml_file()

	# Get a list of Recording Rules from the Command Center

	# Create an XMLParser Object
	parser = XMLParser(rec_rules)

	parser.feed()
	
def schedule_recording(channel,start_time,end_time,name):
	# Send this scheudling data back to the Command Center


class XMLParser():
	
	def on_entry_start():
		# Clear current show info
		self.curr* = ""

	def on_entry_end():
		for r in rules:
			if r["name"] == self.curr_name and self.curr_resolution == r["resolution"]:
				if r["new"] == True:
					if self.new == True:
						schedule_recording()
				else:
					schedule_recording()
	def on_show_name(text):
		# Check if Show Name is matches one of the rules

	def on_original_air_date(text):
		# Check if Show is New or Not

	def on_channel_resolution(text):
		# Check if Channel is HD or not

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
		
