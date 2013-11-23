My DVR
======

# Introduction

## Motivation
Now that I finally have a cable provider (RCN) that lets me freely copy recorded shows, i would like to get rid of my TiVo.  I will use HDHomeRun Prime as a tuner to record all of my shows onto my NAS server.

## Goal
Create my own DVR based on Python

# Feature Roll Out

## Version 1
The first version will be a basic recording app that records at a given time M-F.
* Recorder
    * Streams the TV stream to a file
    * Recordings will be saved in the .mpeg folder.  
    * When a recording is in progress, it will be saved as a randome string.  The MPEG extension will not be added until the recording is completed.
* Transcoder
    * Looks for files in the /.mpeg/ folder.  When an mpeg is found, convert it to an mp4 file
* Control Center
    * Starts the Recorder Process when needed
* Device Manager
    * Discovers Tuners on the current network and sends them back to the Control Center
* CLI Interface
    * Allow user to tweak the command center

# Processes

## Command Center
This will be the main process that is launched first.  This process will host a Unix Socket (based on the asyncore class) and will spawn all of the other processes.  Additionally, the Command Center will mantain the centra database used by the other subprocesses

## WebUI Server
A HTTP web server will act as a simple User interface for scheduling and managing recordings.  It will send and recieve commands to the Command Center.  This webserver will use the FastCGI protocol.  

## Recorder
This process will be spawned by the Command Center when a stream needs to be recorded.  THere may be multiple recorder processes running simultaniously.  

## Transcoder
This process will transcode MPEG2 video files to H264 once recording is complete.  For now, only 1 trancoder process will run at a given time.  

## Device Manager
This process will periodically look for tuners as well as report back the status of each tuner.

## Schedule Manager
This process will fetch the latest listing information from the internet and schedule recordings accordingly.  It will compare the recoding rules (stored in the Command Center database) with the current listings.  When a match is found, a basic recording event will be pushed back to the Command Center.  This event will be recorded by he Recorder Process.  

## Commercial Flagger
This process will scan video files and look for commericals.  This info will be used to delete commericals from the video during transcoding.  

# Databases

## Rules
A list of human readable rules used to automatically schedule new events.  

* title
    * RegEx matching the title
* description
    * RegEx matching the description
* new
    * True if only new shows should be schedules
* channel
    * A list of channels you are allowed to record on

## Schedule
Contains a list of recording events. Each event will have the following key/values

* uid
    * A unique id given to each event 
* name
    * The Name of the recording
* time
    * Start Time of the recording (in Unix time... seconds since 1/1/1970 in UTC)
* length
    * Length of recording (in seconds)

