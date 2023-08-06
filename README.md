# chat-app
A Chat application where two user can converse with one another in realtime.

Requirements:
- Docker Desktop
- Ngrok
- Pipfile
- Pipfile.lock

How to run locally: 
- Docker Desktop
- Open Docker and in a cli terminal enter the command "docker run --rm -p 6379:6379 redis:7"
- Open another terminal then
- Enter "pipenv shell"
- Enter "cd main"
- Enter "python manage.py runserver"

How to deploy with Ngrok:
- Require Docker Desktop and Ngrok
- run "docker run --rm -p 6379:6379 redis:7"
- convert all 'ws' to 'wss' in 'message/routing.py' nad 'template/message/room.html'
- The Ngrok Url must end with ".ngrok-free.app", otherwise update the ALLOWED_HOST in settings.py
- Python manage.py runserver

Limitations of Ngrok:
- Some ISP blocking the application
- IOS cuurently not workinng

----------------------
Devlog:

August 08, 2023
- Used django as the main framework for the application.
- Created Rooms where the channels can communicate and interact with one another.
- functional for both Local and Ngrok
