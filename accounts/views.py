from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

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


# Connexion de l'utilisateur
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')

    return render(request, 'accounts/login.html', {'error': 'Utilisateur ou mot de passe incorrect'})


# Déconnexion de l'utilisateur
def logout_user(request):
    logout(request)
    return redirect('index')
