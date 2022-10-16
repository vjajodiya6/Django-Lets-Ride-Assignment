from rest_framework import serializers
from letsRideServer.models import Requests, Riders


class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ('RequestId',
                  'RequesterEmailid',
                  'From',
                  'To',
                  'RequesterDate',
                  'FlexibleDate',
                  'TotalAssets',
                  'Assettype',
                  'Assetsensitivity',
                  'DeliveryContact',
                  'Status')


class RidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riders
        fields = ('RiderId',
                  'RiderEmailid',
                  'RiderContact',
                  'From',
                  'To',
                  'RiderDate',
                  'FlexibleDate',
                  'Medium',
                  'TotalAssets')
