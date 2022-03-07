from django.shortcuts import render

from users.models import User

def index(request):
    context = {'title': 'GeekShop-Admin'}
    return render(request, 'admins/index.html', context)


# Read controller
def admin_users(request):
    users = User.objects.all()
    context = {'title': 'GeekShop-Admin', 'users': users}
    return render(request, 'admins/admin-users-read.html', context)
