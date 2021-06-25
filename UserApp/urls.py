from . import views
from .views import UserListView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#app_name="productapp"

urlpatterns = [
    path('', UserListView.as_view(), name="users-list"),
	#path("users/<int:pk>/", ProductDetailView.as_view(), name="users-detail"),
	#path("users/<int:pk>/edit/", ProductUpdateView.as_view(), name="users-update"),
	#path("users/<int:pk>/delete/", ProductDeleteView.as_view(), name="users-delete"),
	#path("users/create/", ProductCreateView.as_view(), name="users-create"),
    path("test/", views.test, name="users-test"),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)