from django.urls import path
from . import views

urlpatterns=[
    path('',views.ContractData.as_view()),
    path('<str:user>',views.ContractDataDetail.as_view())
]