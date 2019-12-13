from django.contrib import admin
from django.urls import path, include
from milestone import views
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('profile/', views.profile, name='profile'),
]
