#main imports
from fastapi import FastAPI,File,UploadFile,HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

#custom Function imports
from functions.openai_requests import convert_audio_to_text


#initiate App
app = FastAPI()


#CORS - Origins
origins =[
    "http://192.168.1.10:5173",
    "http://192.168.1.10:5174",
]

#CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health")
async def check_health():
    return {"message": "healthy"}

#post bot response
#notee: not playing in browser when using post request
@app.post("/post-audio")
async def post_audio(file:UploadFile=File(...)):
    print("hello world",file)
    message_decoded = convert_audio_to_text(file)
    print("message:",message_decoded)
    return message_decoded


#get audio
@app.get("/post-audio-get")
async def get_audio():
    audio_input = open("guillem_voice.mp3", "rb")

    #decode audio
    message_decoded = convert_audio_to_text(audio_input)
    print(message_decoded)
    return message_decoded


