My DVR
======

# Introduction

## Motivation
Now that I finally have a cable provider (RCN) that lets me freely copy recorded shows, i would like to get rid of my TiVo.  I will use HDHomeRun Prime as a tuner to record all of my shows onto my NAS server.

## Goal
Create my own DVR based on Python

# Current Progress

## Complete

* DONE Detect HDHomeRun device using libhdhomerun library

## In Progress

* Record video stream using H264 video codec and Opus Audio codecs
* Schedule a fix time/duration daily recording
    * E! News for my wife would be good since its on at the same time every day

## Future
* Use SchedulesDirect API to Determine when shows are on
* Create a "Name" based recording shedule
* Remove Commercials from recordings (Copy MythTV' CommFlag program)

# Processes

## Command Center
This will be the main process that is launched first.  This process will host a Unix Socket (based on the asyncore class) and will spawn all of the other processes.  Additionally, the Command Center will mantain the centra database used by the other subprocesses

## WebUI Server
The User will interact with this process.  Various DVR commands will be issued

## Recorder
This process will be spawned by the Command Center when a stream needs to be recorded.  THere may be multiple recorder processes running simultaniously.  

## Transcoder
This process will transcode MPEG2 video files to H264 once recording is complete.  For now, only 1 trancoder process will run at a given time.  

## Device Manager
This process will periodically look for tuners as well as report back the status of each tuner.

## Listing Manager
This process will fetch the latest listing information from the internet and schedule recordings accordingly

## Commercial Flagger
This process will scan video files and look for commericals.  This info will be used to delete commericals from the video during transcoding.  

# Recoding
Basic Command

	hdhomerun_config <device_id> save <tuner number> - | avconv -i - -c:v libx264 -preset fast -crf 25 -c:a libopus -ac 2 -b:a 128k  -ac 2 output.mkv

 
