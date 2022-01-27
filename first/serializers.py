from first.models import Plo, Tally
from rest_framework import serializers


class DemoSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()
    class Meta:
        model=Plo
        # fields='__all__'
        fields='__all__'

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plo
        fields = ['company','file']


class tallySerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()
    class Meta:
        model= Tally
        # fields='__all__'
        fields='__all__'

class AlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tally
        fields = ['company','file']