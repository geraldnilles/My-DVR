#!/usr/bin/env python

import os
import uuid
import time
import libcommand_center as libcc
import argparse
import subprocess


def record(device_id, tuner_number, length, filename):
	tempname = libcc.RECORD_MPEG_FOLDER+str(uuid.uuid1())
	
	"""
	libcc.send_recv({
		"source":"recorder",
		"message":"Recording Started on Tuner "+str(tuner_number)
		})
	"""
	print "Recording Started"

	proc = subprocess.Popen([
				"hdhomerun_config",
				device_id,
				"save",
				"/tuner"+str(tuner_number),
				tempname],
			stdout=subprocess.PIPE,
			stdin=subprocess.PIPE,
			stderr=subprocess.PIPE)

	# Keep track of the start time.
	start_time = time.time()
	# Loop for as long as the process is alive
	while proc.poll() == None:
		# Check if the recording is complete
		if time.time()-start_time > length:
			# Report Completion to Command Center
			# Send the Kill signal
			proc.kill() # or proc.terminate?
			"""libcc.send_recv({
				"source":"recorder",
				"message":"Recording Finished on Tuner "
					+str(tuner_number)
				})
			"""
			print "Recording Finished"
			break # Stop the loop
	
		# Read the STDOUT
		# Report back to Command Ctner
		#resp = update_progress(tuner,filename)
		#if resp["message"] == "KILL":
		#	# Report KILL to Command Center
		#	proc.terminate()
		#	break
		time.sleep(5)
		print int((time.time()-start_time)/length*100),"percent"

	# Wait for the proc to finish up
	proc.wait()

	# Move from Temp directory to Recordings directory
	os.rename(tempname,libcc.RECORD_MPEG_FOLDER+filename)

def change_channel(device_id, tuner_number, channel):
	proc = subprocess.Popen([	"hdhomerun_config",
				device_id,
				"set",
				"/tuner"+str(tuner_number)+"/vchannel",
				str(channel)])

	proc.wait()
	return proc.poll()

if __name__ == "__main__":
	# Parse Arguments 
	parser = argparse.ArgumentParser(description=
			"Record Stream from HDHomeRun Prime Tuner")
	parser.add_argument("-i","--id",
				help="HDHomeRune Device ID Hex String",
				required=True)
	parser.add_argument("-t","--tuner",
				help="Tuner Number to use", 
				type=int,
				default=0)
	parser.add_argument("-l","--length",
				help="Length of recording (in seconds)",
				type=int,
				default=60*60)
	parser.add_argument("-c","--channel",
				help="Virtual Channel to Record",
				type=int)
	parser.add_argument("-o","--outfile",
				help="Output MPEG file name",
				required=True)

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
			parser.print_usage()
			exit()
	

	# Check if a channel is given
	if args.channel != None:
		ret = change_channel(args.id,args.tuner,args.channel)
		if ret != 0:
			print "There was an issue changing the channel"		
			exit(-1)

	# Record the Stream
	record(args.id, args.tuner , args.length, args.outfile)


