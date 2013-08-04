# RCN Setup

When activating my cablecard, i had to ask RCN to "hit" my device a few times. Initially, the device was not responding since it was behind a few splitters.  After rearranging the device (placing on the other side of the splitter), the CableCard was properly activated.

# Channel setup
First, set the tuner to a certain frequency
	hdhomerun_config <device_id> set /tuner0/channel auto:<frequency>

Next, you can determine the available programs on that frequency by looking at the stream info
	hdhomerun_config <device_id> get /tuner0/streaminfo

Finally, chose the program number
	hdhomerun_config <device_id> set /tuner0/program <num>

# Record a Tuner
Raw Recording to the disk
	hdhomerun_config <device_id> save /tuner0 [filename]

Instead of recording the large version first, you can feed it directly to ffmpeg
	hdhomerun_config <device_id> save /tuner0 - | ffmpeg -i - [trans-filename]
