import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',200)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

while True:
	text = input()
	if text == 'quit()':
		break
	else:
		engine.say(text)
		engine.runAndWait()