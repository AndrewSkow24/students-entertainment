from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from .models import Student, Subject
from .forms import StudentForm, SubjectForm
from django.forms import inlineformset_factory


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy("main:list_student")


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
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


class StudentListView(ListView):
    model = Student
