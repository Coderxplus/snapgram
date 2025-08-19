from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, ProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])  # Encrypt password
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("login")
        
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        
    context = {
            "userform":user_form,
            "profileform":profile_form
        }

        
        
    return render(request, template_name="registration.html", context=context)


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            remember = request.POST.get("remember_me")
            if remember == "on":
                request.session.set_expiry(1209600)  # 2 weeks
            else:
                request.session.set_expiry(0)  

            return redirect('/')
        else:
            print("Form is invalid")

    return render(request, "registration/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("/login")

@login_required
def edit_profile(request, user):
    
    logged_user = get_object_or_404(User, username=user)

    if request.user == logged_user:
        profile = Profile.objects.get(user__username=user)
        if request.method == "POST":
            profile_pic = request.FILES.get("pic")
            username = request.POST.get("username")
            full_name = request.POST.get("name")
            bio = request.POST.get("bio")
            if profile_pic:
                profile.profile_pic = profile_pic
            
            profile.user.username = username
            profile.full_name = full_name
            profile.bio = bio
            profile.save()

            return redirect("/")
            
    context = {
        "edit_user":user,
    }


    return render(request, "edit_profile.html", context)






# Create your views here.
