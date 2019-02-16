from rest_framework import serializers


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
