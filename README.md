# SkyFire-payload-flight-code
The code running on the payload of the high powered model rocket, SkyFire
This payload is a RaspberryPi 4b with a raspberry pi cammera to record onboard footage. A PiSugar battery pack was used to provide power during the flight

To configure this code for your own use do the folowing:
1: open up the terminal
2: install python and pip
3: using pip, install pycamera2, datetime, and time.
4: add the python file and batch scrypt to the desktop enviroment
5: open the batch scrypt and change the file path to that of the python scrypt
6: in the terminal, go to crontab by typing sudo crontab -e
7: add "@reboot python batch file path", with this the camera will start recording when the pi receves power and starts up

The python scrypt given here, you will get 24, 5 minute recordings for a total of 2 hours of footage. This system is set up so that in the case of an unexpected power loss, there will be some recoverable footage.
To change number of recordings, change the number in the for loop, to change the amount of time each recording lasts, go to the "startRecording" function and change the number in the time.sleep(#) line, the number in parenthasees is the time in seconds each recording lasts.

The inflight footage recovered using this code:
https://github.com/user-attachments/assets/46f81e59-5469-430d-a539-59a854977442
