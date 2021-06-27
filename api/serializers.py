from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from contracts.models import SmartContract


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = SmartContract
        fields = ('pk','hash')