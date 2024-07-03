# from rest_framework import serializers
# from chain.models import LinkOfChain, Product, Contact
#
#
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('name', 'model',)
#
#
# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contact
#         fields = '__all__'
#
#
# class LinkOfChainSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LinkOfChain
#         fields = '__all__'
#         read_only_fields = ('debt',)
#
#     hierarchy_level = serializers.SerializerMethodField()
#     contact = ContactSerializer()
#     # product = ProductSerializer()
#
#     def get_hierarchy_level(self, obj):
#         return obj.get_hierarchy_level()
#

from rest_framework import serializers
from .models import LinkOfChain, Product, Contact
from django.core.exceptions import ValidationError


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'model', 'market_date', 'link_of_chain')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class LinkOfChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkOfChain
        fields = '__all__'
        read_only_fields = ('debt',)

    hierarchy_level = serializers.SerializerMethodField()
    contact = ContactSerializer()

    def get_hierarchy_level(self, obj):
        if obj.get_hierarchy_level() > 3:
            raise serializers.ValidationError("Иерархия звеньев не "
                                              "может превышать 3")
        print(obj.get_hierarchy_level())
        return obj.get_hierarchy_level()

    def create(self, validated_data):
        contact_data = validated_data.pop('contact')
        contact = Contact.objects.create(**contact_data)
        link_of_chain = LinkOfChain.objects.create(contact=contact, **validated_data)
        return link_of_chain

    def update(self, instance, validated_data):
        contact_data = validated_data.pop('contact')
        contact = instance.contact

        instance.name = validated_data.get('name', instance.name)
        instance.supplier = validated_data.get('supplier', instance.supplier)
        # Update other fields as needed

        for attr, value in contact_data.items():
            setattr(contact, attr, value)
        contact.save()

        instance.save()
        return instance
