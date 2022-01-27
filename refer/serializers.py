from django.http import request
from refer.models import *
from rest_framework import serializers

class AllSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    recommended_by = serializers.StringRelatedField()
    class Meta:
        model=Profile
        # fields='__all__'
        fields='__all__'

# class AddSerializer(serializers.ModelSerializer):
#     u = serializers.CharField(User, source='username')
#     class Meta:
#         model = Profile
#         fields = ['u','recommended_by']
#         # fields = ['user']


class AddSerializer(serializers.ModelSerializer):
    

    class AnotherSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            # 'model_a_field' is a FK which will be assigned after creation of 'ModelA' model entry
            # First entry of ModelB will have (default) fieldB3 value as True, rest as False
            # 'field4' will be derived from its counterpart from the 'Product' model attribute
            # exclude = ['user','code','link','link2','bio', 'updated', 'created']
            exclude = ['user','code', 'updated', 'created','link', 'link2', 'bio']

    model_b = AnotherSerializer()  

    class Meta:
        model = User
        fields = '__all__'
        # fields = ['username',  'model_b']

    def create(self, validated_data):
        model_b_data = validated_data.pop('model_b')
        model_a_instance = Profile.objects.create(**validated_data)
        User.objects.create(username=model_a_instance.user,
                              **model_b_data)
        return model_a_instance



# class AddSerializer(serializers.ModelSerializer):
# #     class AnotheSerializer(serializers.ModelSerializer):
#         class Meta:
#             model=User
#             # fields='__all__'
#             # fields=  ['username','password']
#             fields = ['username','password']#     model_b = AnotheSerializer()#     class Meta:
#         model = Profile
#         # fields='__all__'
#         fields = ['recommended_by','model_b']#     def create(self, validated_data):
#         model_b_data = validated_data.pop('model_b')
#         model_a_instance = User.objects.update_or_create(**model_b_data)
#         Profile.objects.create(user=model_a_instance,**model_b_data)
#         return model_a_instance