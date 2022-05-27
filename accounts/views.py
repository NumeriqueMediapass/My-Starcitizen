from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout

User = get_user_model()


# Inscription de l'utilisateur
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)

        login(request, user)
        return redirect('index')

    return render(request, 'accounts/register.html')


def logout_user(request):
    logout(request)
    return redirect('index')
