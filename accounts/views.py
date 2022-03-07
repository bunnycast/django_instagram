from django.contrib import messages
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Welcome to Sign Up! :D")
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })
