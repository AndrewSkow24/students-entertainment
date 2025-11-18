from django.db import models

NULLABLE = {"blank": True, "null": True}


class Student(models.Model):
    # имя, фамилия, аватар
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    avatar = models.ImageField(upload_to="students/", verbose_name="аватар", **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ("last_name",)
