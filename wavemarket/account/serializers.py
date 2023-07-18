from rest_framework.serializers import ModelSerializer
from .models import Address, User

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class UserSerializer(ModelSerializer):
    address = AddressSerializer(many=False)
    
    class Meta:
        model = User
        fields = ['id','email', 'username' ,'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',
                  'phone', 'discount', 'address', 'photo']
        
class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'photo']