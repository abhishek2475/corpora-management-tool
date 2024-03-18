# Necessary imports
from rest_framework import generics
from .models import ParallelText, DeletionRequest
from .serializers import ParallelTextSerializer
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomSignupForm, ParallelTextForm, FilterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

# Define the index view
def index(request):
    return render(request, "index.html")

# Define the home view
@login_required(login_url="login")
def home(request):
    # Get all parallel texts
    parallel_texts = ParallelText.objects.all()
   
    # Get the choice from the session; gives None if doesn't exist
    choice = request.session.get('choice')

    if request.method == "POST":
        # Create a form instance and populate it with data from the request
        form = FilterForm(request.POST)
        if form.is_valid():
            # Get the source and target languages from the form
            source = form.cleaned_data.get("source")
            target = form.cleaned_data.get("target")
            
            # Check the language pair and render the appropriate template
            if set([source, target]) == set(["en", "hi"]):
                return render(request,"basetv.html", {"parallel_texts": parallel_texts, "choice": 1})
            elif set([source, target]) == set(["en", "mn"]):
                return render(request,"basetv.html", {"parallel_texts": parallel_texts, "choice": 2})
            elif set([source, target]) == set(["hi", "mn"]):
                return render(request,"basetv.html", {"parallel_texts": parallel_texts, "choice": 3})
            else:
                messages.info(request, "Invalid language pair. Please select a valid language pair.")
    else:
        form = FilterForm()

    if choice:
        # Remove the choice from the session
        del request.session['choice']
        if choice != 0:
            return render(request, "basetv.html", {"parallel_texts": parallel_texts, "choice": choice})

    return render(request, "base.html", {"parallel_texts": parallel_texts, "form": form, "choice": 0})

# Define the add ParallelText view
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

# Define the delete ParallelText view
@login_required(login_url="login")
def delete(request, id, choice):
    # Get the parallel text object with the given id
    parallel_texts = ParallelText.objects.get(id=id)
    
    # Check if the user is a Data Manager
    if request.user.groups.filter(name="Data Manager").exists():
        # Delete the parallel text object
        parallel_texts.delete()
        
        # Redirect based on the choice
        if choice == 4:
            return redirect('deletion')
        return redirect('home')
    else:
        # Create a deletion request
        deletion_request = DeletionRequest(parallel_text=parallel_texts, requested_by=request.user.username)
        deletion_request.save()
        
        # Set the choice in the session
        request.session['choice'] = choice
        
        return redirect('home')

# Define the deletion request view
def deletion(request):
    # Get all deletion requests
    deletion_requests = DeletionRequest.objects.all()
    # Render the deletion.html template with deletion requests
    return render(request, "deletion.html", {"deletion_requests": deletion_requests})

# Define the update ParallelText view
@login_required(login_url="login")
def update(request, id, choice):
    # Get the parallel text object with the given id
    parallel_texts = get_object_or_404(ParallelText, id=id)
    
    # Create a form instance and populate it with data from the request
    form = ParallelTextForm(request.POST or None, instance=parallel_texts)
    
    if form.is_valid():
        # Save the form
        form.save()
        
        # Set the choice in the session
        request.session['choice'] = choice
        
        return redirect("home")
    
    return render(request, 'update.html', {'form': form, 'choice': choice})

# Define the upload data view
@login_required(login_url="login")
def upload(request):
    return render(request, 'upload.html')

# Define the ParallelTextListCreate view
class ParallelTextListCreate(generics.ListCreateAPIView):
    # Get all parallel texts
    queryset = ParallelText.objects.all()
    
    # Use the ParallelTextSerializer for serialization
    serializer_class = ParallelTextSerializer

# Define the register user view
def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            form = CustomSignupForm(request.POST)
            if form.is_valid():
                # Get the role from the form
                role = form.cleaned_data.get("role")
                
                # Save the user form
                user = form.save()
                
                # Get the group based on the role
                group = Group.objects.get(name=role)
                
                # Add the user to the group
                user.groups.add(group)
                
                # Login the user
                login(request, user)
                
                return redirect("home")
        else:
            form = CustomSignupForm()

        return render(request, "signup.html", {"form": form})

# Define the user signin view
def signin(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                # Get the username and password from the form
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                
                # Authenticate the user
                user = authenticate(request, username=username, password=password)
                if user:
                    # Login the user
                    login(request, user)
                    return redirect("home")
                else:
                    messages.info(request, "Username or password is incorrect")
        else:
            form = AuthenticationForm()

        return render(request, "login.html", {"form": form})

# Define the user signout view
def signout(request):
    # Logout the user
    logout(request)
    # Redirect to the index page
    return redirect("index")