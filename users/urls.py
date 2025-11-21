from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # Import Django's built-in auth views

app_name = 'users'

urlpatterns = [
        path('signup/', views.signup, name='signup'),
        # Use our custom user_login view
        path('login/', views.user_login, name='login'),
        # Use our custom user_logout view
        path('logout/', views.user_logout, name='logout'),
        
        # Optional: Django's built-in password reset views (for future)
        # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
        # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
        # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
        # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    ]