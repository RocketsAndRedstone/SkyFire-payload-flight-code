#!/bin/python
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from datetime import datetime
import time
def startRecording():
    encoder = H264Encoder(bitrate=10000000)
    output = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + ".h264"
    picam2.start_recording(encoder,output)
    time.sleep(300)
    picam2.stop_recording()


picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
for i in range (24):
    startRecording()
