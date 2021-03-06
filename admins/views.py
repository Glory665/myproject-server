from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'GeekShop-Admin'}
    return render(request, 'admins/index.html', context)


class TitleMixin:
    title = None

    def get_context_data(self, object_list=None, *args, **kwargs):
        context = super(TitleMixin, self).get_context_data(object_list=None, **kwargs)
        context['title'] = self.title
        return context


class UserListView(TitleMixin, ListView):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'GeekShop - Админка'

    # def get_context_data(self, object_list=None, *args, **kwargs):
    #     context = super(UserListView, self).get_context_data()
    #     context['title'] = 'GeekShop - Admin'
    #     return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# Read controller
# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     users = User.objects.all()
#     context = {'title': 'GeekShop-Admin', 'users': users}
#     return render(request, 'admins/admin-users-read.html', context)


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    success_message = 'Пользователь успешно создан!'


# Create controller
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Пользователь успешно создан.')
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#     else:
#         form = UserAdminRegistrationForm()
#     context = {'title': 'GeekShop-Admin', 'form': form}
#     return render(request, 'admins/admin-users-create.html', context)


class UserAdminUpdateView(TitleMixin, UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    title = 'GeekShop - Админка'

# Update controller
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_update(request, pk):
#     selected_user = User.objects.get(id=pk)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(instance=selected_user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#     context = {'title': 'GeekShop-Admin', 'form': form, 'selected_user': selected_user}
#     return render(request, 'admins/admin-users-update-delete.html', context)


class UserAdminDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.safe_delete()
        return HttpResponseRedirect(self.success_url)

# Delete controller
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_delete(request, pk):
#     user = User.objects.get(id=pk)
#     user.safe_delete()
#     return HttpResponseRedirect(reverse('admin_staff:admin_users'))
