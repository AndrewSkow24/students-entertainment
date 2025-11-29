from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.models import User
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:login")


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user
