from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'userid', 'productid', 'status')
