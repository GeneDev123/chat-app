# chat-app
A Chat application where two user can converse with one another in realtime.

Devlog:
August 08, 2023
- Used django as the main framework for the application.
- Created Rooms where the channels can communicate and interact with one another.

How to run locally: 
- pipenv shell
- cd main
- Open Docker and in a cli terminal enter the command: docker run --rm -p 6379:6379 redis:7
- create another terminal then enter "python manage.py runserver"

How to use with Ngrok:
- Open Docker
- run "docker run --rm -p 6379:6379 redis:7"
- Python manage.py runserver
- Add the Ngrok url in the allowed_host in settings.py
- convert ws to wss