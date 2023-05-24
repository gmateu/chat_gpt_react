import requests
import json
from decouple import config


ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")
print(ELEVEN_LABS_API_KEY)

def convert_text_to_speech(message):
    print("in convert_text_to_speech")
    #define voice
    body={
        "text": message,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0,
            "similarity_boost":0
        }
    }

    '''
    body={
        "text": message,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    '''

    #define voice
    voice_rachel="21m00Tcm4TlvDq8ikWAM"

    headers ={
        "xi-api-key": ELEVEN_LABS_API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    }
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}"
    print(endpoint,headers)

    #send request
    try:
        print("________________")
        print("try")
        response = requests.post(endpoint,json=body,headers=headers)
        print(response)
    except Exception as e:
        print("error requesting elevenlabs:",e)
        return e
    
    #handle response
    if response.status_code == 200:
        print("response 200: ",response.content)
        return response.content
    else:
        return