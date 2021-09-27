from django.shortcuts import render, redirect
from .models import *
from login.models import *
from django.contrib import messages
from datetime import date, datetime

# Create your views here.
def travels(request):
    if 'user_id' not in request.session:
        return redirect('/')
    today = datetime.now()

    context = {
        'active_user': User.objects.get(id=request.session['user_id']),
        'travel_list': Travel.objects.filter(user__id = request.session['user_id']).order_by('start_date'),
        'all_travels': Travel.objects.all().exclude(user__id = request.session['user_id']),
    }
    return render(request, 'travels.html', context)


def add_travel(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'add_travel.html')


def new_travel(request):
    if 'user_id' not in request.session:
        return redirect('/')
    active_user = User.objects.get(id=request.session['user_id'])
    errors = {}
    today = datetime.now()
    comp_date = request.POST['start_date']
    comp_date2 = request.POST['end_date']
    date_object = datetime.strptime(comp_date, "%Y-%m-%d")
    date_object2 = datetime.strptime(comp_date2, "%Y-%m-%d")

    if len(request.POST['destination']) == 0:
        errors['destination'] = "Must provide a destination to your travel"
    if len(request.POST['plan']) == 0:
        errors['plan'] = "Must type a travel plan"
    if len(request.POST['start_date']) == 0:
        errors['no_start_date'] = "Must provide a start date for your travel"
    if len(request.POST['end_date']) == 0:
        errors['no_end_date'] = "Must provide a end date for your travel"
    if today > date_object or today > date_object2:
        errors['bad_dates'] = "Start or end date travel cannot be in set in a past date"
    # if today > date_object2:
    #     errors['bad_start_date'] = "End date travel cannot be in set in a past date"
    if date_object > date_object2:
        errors['bad_dates2'] = "The start date travel cannot be after end date travel"

    if len(errors) > 0:
            for key, msg in errors.items():
                messages.error(request, msg)
            return redirect('/travels/add')
    else:
        Travel.objects.create(
            destination = request.POST['destination'],
            plan=request.POST['plan'],
            start_date = comp_date,
            end_date = comp_date2,
            user = active_user,
        )
        return redirect('/travels')


def view_travel(request, travel_id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'travel': Travel.objects.get(id = travel_id),
        # 'other_users': Travel.objects.filter(id=travel_id).joined.all(),
    }
    return render(request, 'destination.html', context)


def add_user(request, user_id):
    pass