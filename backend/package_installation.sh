#\!/bin/bash
source venv/bin/activate
pip3 install python-decouple==3.8 python-multipart==0.0.6 requests==2.28.2 fastapi=0.92.0 openai==0.27.0
pip3 install uvicorn[standard]