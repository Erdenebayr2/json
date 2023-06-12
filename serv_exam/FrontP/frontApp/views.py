from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout
import json

def login_json():
    u_login = {}
    with open('log_u.json', 'w') as file:
        json_data = json.dump(u_login, file)
    return json_data

def authenticate_user(username, password):
    with open('log_u.json', 'r') as file:
        json_data = json.load(file)
        for user_id,user_data in json_data.items():
            if user_data['name'] == username and user_data['password'] == password:
                return True
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        age = request.POST['age']
        email = request.POST['email']
        new_user = {
            'name': username,
            'password': password,
            'age': age,
            'email': email
        }
        logged_in_user = {
            'message': 'success',
        }
        with open('log_u.json', 'r') as file:
            json_data = json.load(file)\
            
        u_login = json_data
        json_data = json.dumps(new_user, indent=4)
        user_id = 'u_id{}'.format(len(u_login) + 1)
        u_login[user_id] = new_user

        with open('log_u.json', 'w', encoding='utf-8') as file:
            json.dump(u_login, file,indent=4)
        print(json_data)

        return redirect('log_in')

    return render(request, 'index.html')

def log_in(request):
    if request.session.get('uname'):
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if authenticate_user(username, password):
                request.session['uname'] = username
                return redirect('home')
            else:
                return HttpResponse('Invalid username or password')
        return render(request, 'login.html')
def home(request):
    if request.session.get('uname'):
        return redirect('home')
    else:
        return redirect('log_in')
def log_out(request):
    del request.session.get['uname']
    logout(request)
    return redirect('log_in')

def handler40(request, exception):
    return render(request, '404.html', status=404)
