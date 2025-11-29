from django.urls import path
from . import views
from .apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path("", views.StudentListView.as_view(), name="list_student"),
    path("detail/<int:pk>/", views.StudentDetailView.as_view(), name="detail_student"),
    path("create/", views.StudentCreateView.as_view(), name="create_student"),
    path("update/<int:pk>/", views.StudentUpdateView.as_view(), name="update_student"),
    path("delete/<int:pk>/", views.StudentDeleteView.as_view(), name="student_delete"),
]
