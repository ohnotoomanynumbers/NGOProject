from . import views
from .views import UserListView, UserUpdateView, UserCreateView, UserDeleteView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#app_name="productapp"

urlpatterns = [
    path('', UserListView.as_view(), name="users-list"),
    path('register/', UserCreateView.as_view(), name="register"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="users-detele"),
	#path("users/<int:pk>/", ProductDetailView.as_view(), name="users-detail"),
	path("<int:pk>/update/", UserUpdateView.as_view(), name="users-update"),
	#path(r'^update/$', UserUpdateView.as_view(), name="users-update"),
	#path("update/", UserUpdateView.as_view(), name="users-update"),
	
	#path("users/create/", ProductCreateView.as_view(), name="users-create"),
    path("test/", views.test, name="users-test"),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)