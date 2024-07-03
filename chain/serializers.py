from rest_framework import serializers
from chain.models import LinkOfChain


class LinkOfChainSerializer(serializers.ModelSerializer):
    hierarchy_level = serializers.SerializerMethodField()


    class Meta:
        model = LinkOfChain
        fields = '__all__'
        read_only_fields = ('debt',)

    def get_hierarchy_level(self, obj):
        return obj.get_hierarchy_level()
