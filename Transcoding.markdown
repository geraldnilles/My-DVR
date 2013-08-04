
# What is Transcoding
With transcoding, we use a more efficient codec to shrink the size of the recorded video file.  

# My Command

	ffmpeg -i input.ts -c:v libx264 -preset fast -crf 25 -c:a libfdk_aac -vbr 3  -ac 2 output.mp4

## Video Options
We will conver the video to H264.  This is currently the best codec available and is well supported with Hardware Accellerated decoding so all of the playback device will be able to play it.

We will use x264 to encode it.  

We will use the fast preset in order to reduce the CPU load of transcoding video.  We will use a CRF value of 25.  I found that 25 is a good mid-quality level that is rather space efficient.  

## Audio Options
We will use the Advance Audio Codec (AAC) for audio.  We will reduce the number of channels to stereo (-ac 2).  We will also use a variable bit-rate of 3 (80 to 120 kbps).

