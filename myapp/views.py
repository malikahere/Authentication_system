from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from Signup_Login_authentication import settings
from .forms import UserRegisterForm , PasswordResetRequestForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        userinput = request.POST.get('username_or_email', '')
        password = request.POST.get('password', '')

        users_by_email = User.objects.filter(email=userinput)

        # If no users found with the email, check by username
        if not users_by_email.exists():
            users_by_username = User.objects.filter(username=userinput)
            users_by_email = users_by_username  # Use username filter results for further checks

        # Check each user found with the email or username
        for user in users_by_email:
            if user.check_password(password):
                # If password matches, log in the user
                login(request, user)
                return redirect('dashboard')
               
        else:
            messages.error(request, 'Invalid credentials, please check username/email or password.')

    return render(request, "login.html")

def forgot_password_view(request):
    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            users = User.objects.filter(email=email).order_by('-last_login')
            
            if users.exists():
                user = users.first()
                subject = 'Password Reset Request'
                domain = get_current_site(request).domain
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                protocol = 'https' if request.is_secure() else 'http'
                reset_link = f"{protocol}://{domain}/reset/{uid}/{token}/"
                context = {
                    'user': user,
                    'reset_link': reset_link,
                    'domain': domain,
                }
                html_message = render_to_string('password_reset_email.html', context)
                plain_message = strip_tags(html_message)
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = email

                send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
                
                messages.success(request, 'A password reset link has been sent to your email address.')
                return redirect('forgot_password')
            else:
                messages.error(request, 'No account found with that email address.')

    else:
        form = PasswordResetRequestForm()

    return render(request, 'forgot_password.html', {'form': form})

@login_required
def dashboard_view(request):
    user = request.user
    context = {
        'username': user.username,}
    return render(request, 'dashboard.html', context)

@login_required
def profile_view(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
        'date_joined': user.date_joined,
        'last_login': user.last_login,
    }
    return render(request, 'profile.html', context)

@login_required
def change_password_done(request):
    return render(request, 'change_password_done.html')


