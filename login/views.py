from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def add_user(request):
    #validacion de parametros
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/register')

    else:
        #encriptar password
        password = User.objects.encriptar(request.POST['password'])
        decode_hash_pw = password.decode('utf-8')

        #crear usuario
        user = User.objects.create(
            name=request.POST['name'],
            user_name=request.POST['user_name'],
            # email=request.POST['email'],
            password=decode_hash_pw,
            # birthday = request.POST['birthday'],
        )
        request.session['user_id'] = user.id
        #retornar mensaje de creacion correcta
        # msg="User successfully created"
        # messages.success(request, msg)
    return redirect('/travels')


def login(request):
    if 'user_id' in request.session:
        return redirect('/travels')

    user = User.objects.filter(user_name=request.POST['user_name'].lower())
    errors = User.objects.login_validator(request.POST['password'], user)

    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/')
    else:
        request.session['user_id'] = user[0].id
        request.session['user_name'] = user[0].name
        return redirect('/travels')


def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return redirect('/travels')

def log_out(request):
    request.session.flush()
    return redirect('/')
