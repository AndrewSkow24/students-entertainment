from django.forms import ModelForm
from .models import Student, Subject


class StudentForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = Student


class SubjectForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = Subject
