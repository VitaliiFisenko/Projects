import pyttsx3
import speech_recognition  as sr
import pyowm as pyw
import time
import datetime
engine = pyttsx3.init()
print('Слушаю вас')
time.sleep(1)


r = sr.Recognizer()

print('...')
def say(str):
	print(str)
	engine.say(str)
	engine.runAndWait()
	engine.stop()
	print('...')
#мик
while True:
	query = ''
	r = sr.Recognizer()
	with sr.Microphone(device_index=1) as source:
		audio = r.listen(source)
	try:
		query = r.recognize_google(audio, language="ru-RU").lower()
	except:
		print('Fail to recognize your voice')
	if query == 'привет':
		say('Здравствуйте')
	elif query == 'пока':
		say('Ну пока')
		break
	elif query=='список':
		say('вот список доступных комманд')
		print("\t погода")
		print("\t время")
		print("\t привет")
		print('\t пока')
		say('на этом пока все..')
	elif query == 'время':
		say(str(datetime.datetime.now().hour)+' часов '+str(datetime.datetime.now().minute)+" минут")
	elif query == 'погода':
		say('назовите город')
		r = sr.Recognizer()
		with sr.Microphone(device_index=1) as source:
				audio = r.listen(source)
		try:
			 place = r.recognize_google(audio, language="ru-RU").lower()
		except:
			print('Fail to recognize your voice')
		owm = pyw.OWM('6d00d1d4e704068d70191bad2673e0cc', language='ru')
		observation = owm.weather_at_place(place)
		w = observation.get_weather()
		temp = w.get_temperature('celsius')['temp']
		say('В городе ' + place + ' сейчас ' + w.get_detailed_status())
		say("Температура сейчас в районе "+ str(temp)+" градуса по цельсию")
	else:
		say('для получения списка комманд скажите "список"')
