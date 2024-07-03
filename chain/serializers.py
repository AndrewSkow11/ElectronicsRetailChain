from rest_framework import serializers
from chain.models import LinkOfChain

class LinkOfChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkOfChain
        exclude = ['debt', ]