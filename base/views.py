from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from .models import CustomUser, OTP, Task
from .forms import SignUpForm, OTPForm, LoginForm, TaskForm
import random
from django.contrib.auth.decorators import login_required

def send_otp(user):
    otp = random.randint(100000, 999999)
    OTP.objects.create(user=user, otp=otp)
    send_mail(
        'HI YOUR OTP IS...',
        f'Your OTP code is {otp}',
        'abhinethra.app.dev@gmail.com',
        [user.email],
        fail_silently=False,
    )
   

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Initially, set the user to inactive
            user.save()
            send_otp(user)
            request.session['user_id'] = user.id
            return redirect('verify_otp')  # Redirect to OTP verification page
    else:
        form = SignUpForm()
    return render(request, 'auth/sign_up.html', {'form': form})

def verify_otp(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            otp_code = form.cleaned_data['otp']
            user_id = request.session.get('user_id')
            user = CustomUser.objects.get(id=user_id)
            otp_record = OTP.objects.get(user=user)
            if otp_record.otp == otp_code and otp_record.is_valid():
                user.is_active = True  # Activate the user
                user.save()
                login(request, user)  # Log the user in
                return redirect('home')  # Redirect to the home page
            else:
                form.add_error('otp', 'Invalid OTP')
    else:
        form = OTPForm()
    return render(request, 'auth/verify_otp.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user, is_done=False)  # Filter tasks for the logged-in user
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    return render(request, 'home.html', {'tasks': tasks, 'form': form})

@login_required
def mark_task_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_done = True
    task.save()
    return redirect('home')

@login_required
def mark_task_undone(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_done = False
    task.save()
    return redirect('home')

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    return redirect('home')
