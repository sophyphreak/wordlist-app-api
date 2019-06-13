from django.urls import path

from .views import WordList, WordDetail

urlpatterns = [
    path('<int:pk>/', WordDetail.as_view()),
    path('', WordList.as_view()),
]