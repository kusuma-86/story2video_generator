#!/bin/bash
echo "Starting FastAPI backend on http://localhost:8000"
uvicorn backend.main:app --reload
