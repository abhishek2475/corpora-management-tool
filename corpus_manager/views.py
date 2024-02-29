from rest_framework import generics
from .models import ParallelText
from .serializers import ParallelTextSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomSignupForm, ParallelTextForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def home(request):
    parallel_texts = ParallelText.objects.all()
    return render(request, "base.html", {"parallel_texts": parallel_texts})

@login_required(login_url="login")
def add(request):
    if request.method == "POST":
        form = ParallelTextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ParallelTextForm()
    return render(request, "add.html", {"form": form})

@login_required(login_url="login")
def delete(request,id):
    parallel_texts = ParallelText.objects.get(id=id)
    parallel_texts.delete()
    return redirect('home')

@login_required(login_url="login")
def update(request, id):
    parallel_texts = get_object_or_404(ParallelText, id=id)
    form = ParallelTextForm(request.POST or None, instance=parallel_texts)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, 'update.html', {'form': form})

@login_required(login_url="login")
def upload(request):
    return render(request, 'upload.html')

class ParallelTextListCreate(generics.ListCreateAPIView):
    queryset = ParallelText.objects.all()
    serializer_class = ParallelTextSerializer

def parallel_texts(request):
    parallel_texts = ParallelText.objects.all()
    return render(request, 'display.html', {'parallel_texts': parallel_texts})

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            form = CustomSignupForm(request.POST)
            if form.is_valid():
                role = form.cleaned_data.get("role")
                user = form.save()
                group = Group.objects.get(name=role)
                user.groups.add(group)
                login(request, user)
                return redirect("home")
        else:
            form = CustomSignupForm()

        return render(request, "signup.html", {"form": form})

def signin(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        print("logging...", request.POST)
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect("home")
                else:
                    messages.info(request, "Username or password is incorrect")
        else:
            form = AuthenticationForm()

        return render(request, "login.html", {"form": form})

def signout(request):
    logout(request)
    return redirect("login")