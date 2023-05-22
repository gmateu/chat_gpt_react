#main imports
from fastapi import FastAPI,File,UploadFile,HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

#custom Function imports


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