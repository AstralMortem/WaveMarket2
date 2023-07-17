from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import AudioFragments, Item,Category, Order, Tag


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'slug']

class AudioSerializer(ModelSerializer):
    class Meta:
        model = AudioFragments
        fields = ['audio_file']



class ItemSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True, many=False)
    tag = TagSerializer(read_only=True, many=True)
    audio = AudioSerializer(many=True, read_only=True)
    class Meta:
        model = Item
        fields = "__all__"

class SmallItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ["name", "price", "discount_price",  "slug", "image", "description"]
        read_only_fields = ['image']

        


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"