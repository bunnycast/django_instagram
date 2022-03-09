from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm


login = LoginView.as_view(template_name="accounts/login_form.html")


def logout(request):
    messages.success(request, "Logout Success. Good Bye!")
    return logout_then_login(request)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "Welcome to Sign Up! :D")
            # signed_user.send_welcome_email()    # celery로 비동기 처
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })

