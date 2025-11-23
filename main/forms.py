from django.forms import ModelForm
from .models import Student, Subject
from django import forms


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # widget - менеджер поля, который отвечает за отображение
            field.widget.attrs["class"] = "form-control"


class StudentForm(StyleFormMixin, ModelForm):
    class Meta:
        fields = "__all__"
        model = Student

    def clean_email(self):
        cleaned_data = self.cleaned_data["email"]
        if "mail.ru" not in cleaned_data:
            raise forms.ValidationError("Почта не относится к домену mail.ru")
        return cleaned_data


class SubjectForm(StudentForm, ModelForm):
    class Meta:
        fields = "__all__"
        model = Subject
