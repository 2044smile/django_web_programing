from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/result/', views.ResultView.as_view(), name="result"),
    path('<int:pk>/vote', views.vote, name="vote"),
    #RESTAPI
    path('api/', views.ApiQuestionList.as_view(), name="api_list")
]