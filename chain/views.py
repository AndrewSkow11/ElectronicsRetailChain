from rest_framework import viewsets
from chain.models import LinkOfChain
from chain.serializers import LinkOfChainSerializer
from django_filters.rest_framework import DjangoFilterBackend


class LinkOfChainViewSet(viewsets.ModelViewSet):
    # добавить только поставщиков
    queryset = LinkOfChain.objects.all()
    serializer_class = LinkOfChainSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contact', 'contact__country', ]
