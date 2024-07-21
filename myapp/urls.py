from django.urls import path
from .views import signup_view, login_view,forgot_password_view, dashboard_view, profile_view, change_password_done
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('forgot_password/', forgot_password_view, name='forgot_password'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html', success_url='/change_password_done/'), name='change_password'),
    path('change_password_done/', change_password_done, name='change_password_done'),
]
