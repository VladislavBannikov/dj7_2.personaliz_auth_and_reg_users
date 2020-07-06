from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views

from .forms import UserCreationForm2
from .models import User


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    if request.method == "POST":
        form = UserCreationForm2(request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get("username")
            # same_name_users = User.objects.filter(username=username)
            # if same_name_users.count() > 0:
            #     form.error_messages.update({"duplicate": "Пользователь с таким именем уже существует"})
            # else:
            # save user to database
            user = form.save()
            context = {"message": f"Пользователь {user} создан. "}
        else:
            context = {"form": form}

    elif request.method == "GET":
        form = UserCreationForm2()
        context = {"form": form}
    else:
        context = {"message": "Запрос не поддерживается"}

    return render(
        request,
        'signup.html',
        context=context

    )
