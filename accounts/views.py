from django.contrib import messages
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            messages.success(request, "Welcome to Sign Up! :D")
            signed_user.send_welcome_email()    # celery로 비동기 처
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })
