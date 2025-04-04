from django.shortcuts import render


def user_login(request):
    return render(request, 'userauth/user-login.html')

def user_register(request):
    return render(request, 'userauth/user-register.html')
