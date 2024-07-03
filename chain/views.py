from rest_framework import viewsets
from chain.models import LinkOfChain
from chain.permissions import IsActiveEmployee
from chain.serializers import LinkOfChainSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class LinkOfChainViewSet(viewsets.ModelViewSet):
    # добавить только поставщиков
    queryset = LinkOfChain.objects.all()
    serializer_class = LinkOfChainSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contact', 'contact__country', ]
    permission_classes = [IsActiveEmployee]

