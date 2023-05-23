import openai
from decouple import config


#retrive environment variables 
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

#openai whisper
#convert audio to text
def convert_audio_to_text(audio_file):
    try:
        transcript=openai.Audio.transcribe("whisper-1",audio_file)
        message_test=transcript["text"]
        return message_test
    except Exception as e:
        print(e)
        return None
