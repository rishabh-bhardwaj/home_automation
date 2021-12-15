import speech_recognition as sr
import serial
from time import sleep
import RPi.GPIO as GPIO
r=sr.Recognizer()
bulb1=7
bulb2=5
bulb1sts=0
bulb2sts=0
def listen():
	with sr.Microphone(device_index = 2) as source:
		r.adjust_for_ambient_noise(source)
		print("Say Something ::")
		audio=r.listen(source)
		print("WE HEARD YOU:")
		ch1=voice(audio)
	return ch1;
def voice(audio1):
	try:
		text1=r.recognize_google(audio1)
		print("You Said:"+text1);
		return text1
	except sr.RequestError as e:
		print("CANNOT UNDERSTAND")
		led()
		return 0
	except sr.UnknownValueError:
		print("Google cannot understand you")
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.output(7,0)
GPIO.output(5,0)
def funcon(bulb):
	GPIO.output(bulb,1);
	sleep(1)
	return
def funcoff(bulb):
	GPIO.output(bulb,0)
	sleep(1)
	return	
def led():
	while True:
		ch1=listen()
		if(ch1=="LED 1 on"):
			funcon(bulb1)
			print("LIGHT 1 IS ON")
		if(ch1=="led to on"):
                        funcon(bulb2)
                        print("LIGHT 2 IS ON")

		elif(ch1=="led one of" or ch1=="led 1 of" or ch1=="led one off" or ch1=="LED one of "):	
			funcoff(bulb1)
			print("LIGHT 1 IS OFF")
		elif(ch1=="led to off" or ch1=="led to of" or ch1=="led two of"):  
                        funcoff(bulb2)
                        print("LIGHT 2 IS OFF")
		elif(ch1=="SYSTEM OFF" or ch1=="system of"):
			GPIO.output(7,0)
			GPIO.output(5,0)
			return 0

led()











