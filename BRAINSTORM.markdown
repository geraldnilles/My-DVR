Brainstorm
==========

# Roll Out

## Recorder
Create a tool for starting recrodings.  You specify the tuner number, and how long you want to record, and an output filename.  It will spawn a thread that records the provided tuner for the given period of time and then stops.

You can also specify if you want to transcode using FFMPEG or just save the raw video file.


	record_tuner(tuner_number, length, filename):
		lock the tuner;
		Spawn a recording thread;
		while(1):
			check_tuner_status
			check_time --> kill thread and break over limit
		kill thread

	recording_thread(tuner_number,filename)
		hdhomerun_config [id] save tuner_number filename

		

## Time-Based Manager
This will be a basic time-based scheduler.  You will provide the channel number and how long you want to record.  It will decide which tuner to use, change the channel, and start the recording.

The HDHomeRun Prime allows you to lock and unlock tuners.  I think that will be a good way to deciding whether or not a Tuner is in Use. 

	record_channel(channel, length, filename):


## TV LIsting Schedule
THis will use online TV listing database to schedule recordings.


## Streamer
This will input the TV stream, transcode to h264, and forward the output stream to a destination port.  This will be used to stream live TV to the 

## Commercial Skipping
The ability to skip commericals of my recordings.  
