from django.db.models.fields import BooleanField, CharField, TextField, EmailField
from django.forms import ModelForm
from .models import Student, Subject
from django import forms


class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            if (
                isinstance(field, CharField)
                or isinstance(field, EmailField)
                or isinstance(field, TextField)
            ):
                field.widget.attrs["class"] = "form-control"


class StudentForm(StyledFormMixin, ModelForm):
    class Meta:
        fields = "__all__"
        model = Student

    def clean_email(self):
        cleaned_data = self.cleaned_data["email"]

        if not cleaned_data:
            raise forms.ValidationError("Email обязателен для заполнения")

        if "mail.ru" not in cleaned_data:
            raise forms.ValidationError("Почта не относится к домену mail.ru")
        return cleaned_data


class SubjectForm(StyledFormMixin, ModelForm):
    class Meta:
        fields = "__all__"
        model = Subject
