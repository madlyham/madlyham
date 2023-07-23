from django import *

def my_view():
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
