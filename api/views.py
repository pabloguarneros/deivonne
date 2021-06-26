from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAdminUser, BasePermission
from contracts.models import SmartContract
from . import serializers

# Create your views here.
class ContractData(generics.ListCreateAPIView):

    serializer_class = serializers.ContractSerializer

    def get_queryset(self):
        return SmartContract.objects.all()

class ContractDataDetail(generics.ListCreateAPIView):

    serializer_class = serializers.ContractSerializer

    def get_queryset(self):
        return SmartContract.objects.all()