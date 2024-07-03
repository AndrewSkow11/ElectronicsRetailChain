from rest_framework import viewsets
from chain.models import LinkOfChain, Product
from chain.permissions import IsActiveEmployee
from chain.serializers import LinkOfChainSerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


class LinkOfChainViewSet(viewsets.ModelViewSet):
    queryset = LinkOfChain.objects.all()
    serializer_class = LinkOfChainSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contact', 'contact__country', ]
    permission_classes = [IsActiveEmployee]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]
