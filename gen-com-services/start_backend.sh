#!/bin/bash
# source venv/bin/activate  # Activate virtual environment (if using one)
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
