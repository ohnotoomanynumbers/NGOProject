from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import CustomUser
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registeration_form, updateUser_form
from django.shortcuts import get_object_or_404
import sys
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
"""
user1=CustomUser.objects.get(id=1)
#print >>sys.stderr, user1.id
print("################")
print("pk:")
print(user1.pk)
print(user1.email)
print(user1.role)
print("################")
"""
def test(request):
	#return HttpResponse("<h1>product about</h1>")
	return render(request, "UserApp/test.html", {"title":"test"})

def home(request):
	#return HttpResponse("<h1>product about</h1>")
	return render(request, "UserApp/home.html", {"title":"home"})
"""
def register(request):
	if request.method == "POST":
		form = registeration_form(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get("username")
			messages.success(request, f"Account {username} is created!")
			return redirect("UserApp-test")
	else:
		form = registeration_form()
	return render(request, "UserApp/register.html", {"form": form})
"""
class UserListView(LoginRequiredMixin, ListView):
	model = CustomUser
	template_name = "UserApp/customuser_list.html"
	context_object_name = "users"
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			if not request.user.role=="admin":
				return HttpResponseForbidden()
		else:
			return HttpResponseForbidden()
		return super().dispatch(request, *args, **kwargs)
	#ordering = ["product_id"]

class UserCreateView(LoginRequiredMixin, CreateView):
	login_url = '/login/'
    #redirect_field_name = 'home'
	model = CustomUser
	template_name = "UserApp/register.html"
	form_class = registeration_form
	#success_url="users/"
	def get_success_url(self):
		return reverse('users-list')
	#def form_valid(self, form): # set seller to the user
	#	form.instance.seller = self.request.user
	#	return super().form_valid(form)
	"""
	def form_valid(self, form):
		user = form.save(commit=True)
		password = form.cleaned_data['password']
		user.set_password(password)
		user.save()
		return HttpResponseRedirect(self.get_success_url())
	"""
class UserUpdateView(LoginRequiredMixin, UpdateView):
	model = CustomUser
	form_class = updateUser_form
	template_name = 'UserApp/customuser_update.html'
	context_object_name = 'user'
	def get_success_url(self):
		return reverse('users-list')

	def form_valid(self, form):
		user = form.save(commit=True)
		#password = form.cleaned_data['password']
		#user.set_password(password)
		user.save()
		return HttpResponseRedirect(self.get_success_url())
	
	def dispatch(self, request, *args, **kwargs):
		# here you can make your custom validation for any particular user
		if not request.user.role=="admin":
			raise PermissionDenied()
		return super().dispatch(request, *args, **kwargs)
    
class UserDeleteView(LoginRequiredMixin, DeleteView):
	model = CustomUser
	template_name = "UserApp/customuser_delete.html"
	#context_object_name = 'user'
	def get_success_url(self):
		return reverse('users-list')
	"""
	def form_valid(self, form): # set seller to the user
		form.instance.seller = self.request.user
		return super().form_valid(form)
	def test_func(self):
		product=self.get_object()
		if self.request.user == product.seller:
			return True
		return False
	"""