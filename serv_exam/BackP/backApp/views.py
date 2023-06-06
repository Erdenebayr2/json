from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import json

class login_json:
    u_login = {}
    with open('log_u.json', 'w') as file:
        json_data = json.dump(u_login, file)
# Create your views here.
def index(request):
    u_login = login_json.u_login
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
        json_data = json.dumps(new_user, indent=4)
        user_id = 'u_id{}'.format(len(u_login) + 1)
        u_login[user_id] = new_user
        with open('log_u.json', 'w', encoding='utf-8') as file:
            json.dump(u_login, file,indent=4)
        print(json_data)
        return redirect('log_in')
    return render(request, 'index.html')

def log_in(request):
    if request.session.get('json_data'):
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            with open('log_u.json', 'r') as file:
                json_data = json.dumps(json.load(file))
            if json_data:
                user_data = json.loads(json_data)
                print(user_data, type(user_data))
                print(user_data.get('name'))
                if username == user_data['u_id1']['name'] and password == user_data['u_id1']['password']:
                    return redirect('home')
                else:
                    return HttpResponse('Invalid username or password')
        return render(request, 'login.html')
def home(request):
    return render(request, 'home.html')
def log_out(request):
    del request.session['json_data']
    logout(request)
    return redirect('log_in')
