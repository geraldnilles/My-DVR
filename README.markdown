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

# Recoding
Basic Command

	hdhomerun_config <device_id> save <tuner number> - | avconv -i - -c:v libx264 -preset fast -crf 25 -c:a libopus -ac 2 -b:a 128k  -ac 2 output.mkv

 
