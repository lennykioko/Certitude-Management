from rest_framework import serializers

from . import models


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'ordering',
            'joined',
            'business',
            'name',
            'status',
            'description',
            'stack',
            'total_amount',
        )
        model = models.Client
