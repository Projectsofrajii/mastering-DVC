from rest_framework import serializers
from .models import *
from .models import *
from rest_framework import serializers
from django.conf import settings


class MeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmMeterMaster
        fields = ['meter_id', 'meter_serial_number', ]


class RTOCSerializer(serializers.ModelSerializer):
    class Meta:
        model = RsmTableObisCode
        fields = '__all__'


class RsmColumnObisCodeSeri(serializers.ModelSerializer):
    class Meta:
        model = RsmColumnObisCode
        fields = '__all__'


class InstantSeri(serializers.ModelSerializer):
    InstantProfile = serializers.CharField(source='_00_00_01_00_00_FF')

    class Meta:
        model = b01005E5B00Ff
        fields = ['InstantProfile', ]


class BlockloadSeri(serializers.ModelSerializer):
    BlockloadProfile = serializers.CharField(source='_00_00_01_00_00_FF')

    class Meta:
        model = c0100630100Ff
        fields = ['meter_id', 'BlockloadProfile', ]


class DailyloadSeri(serializers.ModelSerializer):
    DailyloadProfile = serializers.CharField(source='_00_00_01_00_00_FF')

    class Meta:
        model = d0100630200Ff
        fields = ['meter_id', 'DailyloadProfile', ]

class RsmMeterMasterSeri(serializers.ModelSerializer):#3

    class Meta:
        model = RsmMeterMaster
        fields = ['meter_id','meter_serial_number']

class InstantSeri(serializers.ModelSerializer):#3
    class Meta:
        model = InstantModel
        fields = ['meter_id','updated_timestamp',]
