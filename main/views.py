# users/views.py
import json
from .models import Measurement
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.contrib.auth.decorators import login_required



from .forms import RegistrationForm
from .forms import MeasurementForm
from .models import Workouts,UserProgress,WorkoutPlans




def workout_view(request):
    workouts = Workouts.objects.all().filter(workout_type='lose')
    return render(request, 'main/body_exercise.html', {'workouts': workouts})

def body_gain_home(request):
    workouts = Workouts.objects.all().filter(workout_type='gain')
    return render(request, 'main/body_gain_home.html', {'workouts': workouts})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')  # Redirect to a home page or another page after registration
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})

def measurement(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.user = request.user
            measurement.bmi = calculate_bmi(measurement.height, measurement.weight)
            measurement.save()
            return redirect('workout')
    else:
        form = MeasurementForm()
    
    return render(request, 'main/measurement.html', {'form': form})

def calculate_bmi(height, weight):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return bmi

def home(request):
    return render(request, "main/home.html")
# def measurement(request):
#     return render(request, "main/measurement.html")
def workout(request):
    workout_plans = WorkoutPlans.objects.all()
    return render(request, "main/workout.html", {'workout_plans':workout_plans})

def goal(request):
    return render(request, "main/goal.html")
def home(request):
    return render(request, "main/home.html")


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to home or any other page
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})
def logout_view(request):
    auth_logout(request)
    return redirect('login')
# def body_exercise(request):
#     return render(request, "main/body_exercise.html")


@csrf_exempt
def update_user_progress(request, id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_progress = UserProgress.objects.get(pk=id)
            user_progress.plan = data['plan']
            user_progress.no_days = data['no_days']
            user_progress.save()
            return JsonResponse({'success': True})
        except UserProgress.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'UserProgress not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@login_required
def dashboard(request):
    user_progress = UserProgress.objects.filter(user=request.user).first()

    if user_progress:
        # Calculate remaining days
        remaining_days = user_progress.unique_title_days.days - user_progress.no_days
        
        # Calculate progress (example logic)
        total_days = user_progress.unique_title_days.days
        progress = ((total_days - remaining_days) / total_days) * 100 if total_days > 0 else 0
    else:
        remaining_days = 0
        progress = 0

    context = {
        'user_progress': user_progress,
        'remaining_days': remaining_days,
        'progress': progress,
    }

    return render(request, 'main/dashboard.html', {'context':context})