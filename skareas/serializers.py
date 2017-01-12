import rest_framework.serializers as rfs
import skareas.models as skm

from django.contrib.auth.models import User

class UserSerializer(rfs.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class SkiAreaSerializer(rfs.ModelSerializer):
    class Meta:
        fields = ('uid','name')
        model = skm.SkiArea
