#!/usr/bin/python
  
import speech_recognition as sr
import sys
import watson_developer_cloud
import json
import urllib


rok=''
sys.stdout.write('SET VARIABLE Watson "%s"\n'% rok)
sys.stdout.flush()

r = sr.Recognizer()

impo =  sys.argv[1]
audio = "%s.flac" % impo

with sr.AudioFile(audio) as source:
    audio = r.record(source)
    sys.stdout.write("EXEC " + "\"" + "NOOP" + "\" \"" + "audio imported" + "\" " + "\n")
    sys.stdout.flush()

try:
    text = r.recognize_google(audio)
    sys.stdout.write("EXEC " + "\"" + "NOOP" + "\" \"" "%s \n"% text)
    sys.stdout.flush()
    assistant = watson_developer_cloud.AssistantV1(username='0b3f8d4a-563d-4e82-beda-2c011ffcbbe2',password='qbJXLtwDrp2t',version='2018-09-20')
    response = assistant.message(workspace_id='c56ea37e-0ade-432f-8c7f-7b48d065d57a',input={'text': text}).get_result()      
    outp = str(response['output']['text'][0])
    k = urllib.quote_plus(outp)
    j =  outp.replace(","," ")
    sys.stdout.write("EXEC " + "\"" + "NOOP" + "\" \"" "%s \n"% k)
    sys.stdout.flush()
    sys.stdout.write('SET VARIABLE Watson "%s"\n'% j)
    sys.stdout.flush()
    
except Exception as e:
    print (e)