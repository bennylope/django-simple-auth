from django.shortcuts import render


def simple_password(request):
    """
    Checks a password
    """
    return render(request, "simple_auth/password_form.html", {})
