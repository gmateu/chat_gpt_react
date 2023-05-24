#main imports
from fastapi import FastAPI,File,UploadFile,HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

#custom Function imports
from functions.openai_requests import convert_audio_to_text
from functions.openai_requests import get_chat_response
from functions.database import store_messages,reset_messages
from functions.text_to_speech import convert_text_to_speech



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

@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "reseted messages"}

#post bot response
#notee: not playing in browser when using post request
@app.post("/post-audio")
async def post_audio(file: UploadFile = File(...)):
    #audio_input = open("guillem_voice.mp3", "rb")

    #save file from front end
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")


    #decode audio
    message_decoded = convert_audio_to_text(audio_input)

    #Guard: ensure message is decoded
    if not message_decoded:
        return HTTPException(status_code=400,detail="Failed to decode audio")
    
    #Get chatGpte response
    chat_response = get_chat_response(message_decoded)

    if not chat_response:
        return HTTPException(status_code=400,detail="Failed to get chat response")
    
    #convert chat response to audio
    audio_output = convert_text_to_speech(chat_response)
    print("audio_output:",audio_output)

    if not audio_output:
        return HTTPException(status_code=400,detail="Failed to convert text to speech")
    
    #create a generator that yields chunks of data
    def iterfile():
        yield audio_output
    

    #store messages
    store_messages(message_decoded, chat_response)

    print("chat response:",chat_response)

    #return audio file
    return StreamingResponse(iterfile(),media_type="application/octet-stream")


