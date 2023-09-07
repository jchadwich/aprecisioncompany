from django.contrib.auth import get_user_model
from django.views.generic import CreateView, ListView, UpdateView

User = get_user_model()


class UserListView(ListView):
    model = User
    template_name = "users/user_list.html"
    context_object_name = "users"


class UserCreateView(CreateView):
    model = User
    template_name = "users/user_form.html"
    fields = ()


class UserUpdateView(UpdateView):
    model = User
    template_name = "users/user_form.html"
    fields = ()
