from django.urls import path
from . import views

urlpatterns=[
    path('',views.ContractDataList.as_view()),
]