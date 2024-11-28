from django.urls import path
from . import views
app_name = 'user'

urlpatterns = [
    path("", views.user, name="user"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('register/', views.register, name='register'),
    path('top-up/<int:user_id>/', views.top_up, name='top_up'),  # The top-up page
    path('profile/', views.user_view, name='profile'),  # The user profile page
]