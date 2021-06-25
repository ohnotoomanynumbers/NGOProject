from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import CustomUser
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registeration_form


def test(request):
	#return HttpResponse("<h1>product about</h1>")
	return render(request, "UserApp/test.html", {"title":"test"})

def register(request):
	if request.method == "POST":
		form = registeration_form(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get("username")
			messages.success(request, f"Account {username} is created!")
			return redirect("UserApp-test")

	else:
		form = UserCreationForm()
	form=UserCreationForm()
	return render(request, "UserApp/register.html", {"form": form})


class UserListView(ListView):
	model = CustomUser
	template_name = "profile_list.html"
	context_object_name = "users"
	#ordering = ["product_id"]

class ProductCreateView(LoginRequiredMixin, CreateView):
	login_url = '/login/'
    #redirect_field_name = 'home'
	model = CustomUser
	template_name = "UserApp/user_create.html"
	fields = ["firstName", "lastName", "role", "email" ]