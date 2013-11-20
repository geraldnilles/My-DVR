#---------------------
# Commercial Hunting 
#
# These functions are for finding and removing commercials from videos
#-----------------------

#-------------
# Tunable Variables
#-------------

# Minimum time screen must be black before (in ms)
BLACK_FRAME_MINIMUM_PERIOD = 100

# Commercial to Show Ratio Range
SHOW_TO_COMM_MIN = 2
SHOW_TO_COMM_MAX = 4

# Audio Amplitude RMS
AUDIO_AMPLITUDE_AVERAGE_PERIOD = 5 # in seconds
AUDIO_AMPLITUDE_THRESHOLD = -5 # in dB


# Creates a list of commercial locations
def flag_commercials(video)
	# Look for Black Frames
	black_frame_list = find_black_frames(video)
	# Find the black frames that are exactly 15, 30 or 60 second apart
	# Look for Channel Logo on bottom
	# Look for TV Rating (for example TV-MA, TV-14) 
	# (usually shows this when returning from commerical break)
	# Look at Audio Volume (TV commericals are usually louder and more 
	# constant (less time between dialog)



# Removes commercials from the video file
def cut_commericals(video,cut_list)
	pass


