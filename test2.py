import requests
import json

url = "https://api.api2convert.com/v2/jobs"

payload = """{
  "input": [{
     "type": "remote",
   "source": "https://storage.yandexcloud.net/musicbacket/audioToSave751208.mp3"
  }],
   "conversion": [{
   "category": "audio",
   "target": "opus",
   "options": {
       "language_tts": "ru-RU"
   }
  }]
  }"""
headers = {"x-oc-api-key": "5012110b4afe538504d91639568ecfaa", "Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
