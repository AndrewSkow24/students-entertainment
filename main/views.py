from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .models import Student, Subject
from .forms import StudentForm, SubjectForm
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .sevices import get_cached_subjects_for_student


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    permission_required = "main.add_student"
    success_url = reverse_lazy("main:list_student")


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data["subjects"] = get_cached_subjects_for_student(self.object.pk)

        return context_data


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    permission_required = "main.change_student"
    success_url = reverse_lazy("main:list_student")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(
            Student, Subject, form=SubjectForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = SubjectFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = SubjectFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if formset.is_valid():
            # ссылка на родительскую запись
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class StudentListView(LoginRequiredMixin, ListView):
    model = Student


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("main:list_student")
    permission_required = "main.delete_student"
