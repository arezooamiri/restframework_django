from rest_framework import serialaizers 
from shop.models import Category
from shop.models import Customer
from shop.models import Order
from shop.models import ChekoutDetail


class CategorySerializer(serializers.Serializer):
    name=serialaizers.CharField(max_length=150)
    created=serialaizers.DateTimeField()
    color=serialaizers.CharField(max_length=150)
    price=serialaizers.FloatField()


    def create(self,validated_data):
        return Category.objects.create(**validated_data)
    def upadte(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.created=validated_data.get('created',instance.created)
        instance.color=validated_data.get('color',instance.color)
        instance.price=validated_data.get('price',instance.price)
        instance.save()
        return instance

class CustomerSerializer(serialaizers.Serializer):
    name=serialaizers.CharField(max_length=100)
    email=serialaizers.CharField(max_length=100)
    phone_number=serialaizers.CharField(max_length=10)

    def create(self,validated_data):
        return Customer.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name) 
        instance.email=validated_data.get('email',instance.email)
        instance.phone_number=validated_data.get('phone_number',instance.phone_number)
        instance.save()
        return instance 
class OrderSerializer(serialaizers.Serialize):
    Customer=serialaizers.ForeignKey()
    date_ordered=serialaizers.DateTimeField()
    complete=serialaizers.BooleanField(default=False)
    transaction_id = serialaizers.CharField(max_length=100) 


    def create(self,validated_data):
        return Order.objects.create(**validated_data)
    def upadte(self,instance,validated_data):
        instance.Customer=validated_data.get('Customer',instance.customer)
        instance.date_ordered=validated_data.get('date_ordered',instance.date_ordered)
        instance.complete=validated_data.get('complete',instance.complete)
        instance.transaction_id=validated_data.get('transcation_data',instance.transaction_id)
        instance.save()
        return instance 


class ChekoutDetailSerializer(serialaizers.Serialize):
    Customer=serialaizers.ForeignKey()
    Order=serialaizers.ForeignKey()
    phone_number = serialaizers.CharField(max_length=10)
    total_amount = serialaizers.CharField(max_length=10)
    address = serialaizers.CharField(max_length=300)
    city = serialaizers.CharField(max_length=100)
    state = serialaizers.CharField(max_length=100)
    zipcode = serialaizers.CharField(max_length=100)
    date_added = serialaizers.DateTimeField()
    
 

    def create(self,validated_data):
        return ChekoutDetail.objects.Create(validated_data)
    def upadte(self,instance,validated_data):
        instance.Customer=validated_data.get('Customer',instance.Customer)
        instance.Order=validated_data.get('Order',instance.Order)
        instance.phone_number=validated_data.get('phone_number',instance.phone_number)
        instance.total_amount=validated_data.get('total_amount',instance.total_amount)
        instance.address=validated_data.get('adress',instance.address)
        instance.city=validated_data.get('city',instance.city)
        instance.state=validated_data.get('state',instance.state)
        instance.zipcode=validated_data.get('zipcode',instance.zipcode)
        instance.date_added=validated_data.get('date_added',instance.date_added)
        instance.save()
        return instance




