from django.shortcuts import render

BASE_TEMPLATE_URL = 'message/'

def home(request):
  print("In Home View")

  return render(request, BASE_TEMPLATE_URL + 'home.html', {})

def room(request, room_name):
   return render(request, BASE_TEMPLATE_URL + "room.html", {"room_name": room_name})

def profile(request):
  print("In Profile View")
  return render(request, BASE_TEMPLATE_URL + 'profile.html', {})