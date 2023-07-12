from rest_framework import serializers
from .models import Category, Book, Product
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=6 )
    username = serializers.CharField(max_length=50, min_length =6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('id','first_name', 'last_name','email', 'username','password')

        def validate(self, args):
            email = args.get('email', None)
            username = args.get('username', None)
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({'emial': ('email already exist')})
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError({'username': ('username already exist')})
            return super().validate(args)


        def create(self, validated_data):
            return User.objects.create_user(**validated_data)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category

class BookSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'imageurl',
            'created_by',
            'status',
            'date_created' 
        )
        model = Book

class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        fields = (
            'id',
            'product_tag',
            'category',
            'price',
            'stock',
            'imageurl',
            'created_by',
            'status',
            'date_created'
        )
        model = Product
 
class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True,queryset=Book.objects.all())
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'books',
            'products'
        )
 