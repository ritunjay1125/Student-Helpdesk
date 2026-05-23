
# Student Helpdesk Chatbot

A simple cloud-oriented Student Helpdesk Chatbot project developed using Flask and Docker.

## Features
- Student query handling
- Chatbot interaction
- REST API based communication
- Docker container support
- Simple frontend interface

## Technologies Used
- Python Flask
- HTML/CSS/JavaScript
- Docker
- GitHub

## Run Locally

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run project
```bash
python app.py
```

Open:
http://127.0.0.1:5000

## Docker Setup

Build Docker image:
```bash
docker build -t student-helpdesk-chatbot .
```

Run container:
```bash
docker run -p 5000:5000 student-helpdesk-chatbot
```

## Project Workflow
User -> Web Interface -> Flask Backend -> Chatbot Response
