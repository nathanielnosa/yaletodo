from django.urls import path
from . import views

urlpatterns = [
    path('todo/',views.TodoView.as_view()),
    path('todo/<str:id>/',views.TodoDetailsView.as_view()),
    path('complete/<str:id>/',views.CompleteView.as_view()),
]

