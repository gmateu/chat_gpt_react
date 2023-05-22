#!/bin/bash
source venv/bin/activate
uvicorn --host 0.0.0.0 main:app --reload
