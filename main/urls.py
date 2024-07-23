# users/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name='home'),
    path("home/", views.home,name='home'),
    path("goal/", views.goal, name='goal'),
    path("measurement/", views.measurement, name='measurement'),
    path("workout/", views.workout, name='workout'),
    path("register/", views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('body_exercise/',views.workout_view, name='body_exercise'),
    path('body_gain_home/',views.body_gain_home, name='body_gain_home'),
     path('update-progress/<int:id>/', views.update_user_progress, name='update_user_progress'),
    path('dashboard/',views.dashboard, name='dashboard'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)