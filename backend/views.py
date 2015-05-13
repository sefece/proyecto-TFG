from django.shortcuts import render

from .models import User, Administrator, Applicant, Bidder, Revisor, Offer, Application, Tag, Item
from .serializers import UserSerializer, AdministratorSerializer, ApplicantSerializer, BidderSerializer, RevisorSerializer, OfferSerializer, ApplicationSerializer, TagSerializer, ItemSerializer
from rest_framework import viewsets
 
class UserViewSet(viewsets.ModelViewSet):
 
    serializer_class = UserSerializer
    queryset = User.objects.all()
 
class AdministratorViewSet(viewsets.ModelViewSet):
 
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()

class ApplicantViewSet(viewsets.ModelViewSet):
 
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()

class BidderViewSet(viewsets.ModelViewSet):
 
    serializer_class = BidderSerializer
    queryset = Bidder.objects.all()

class RevisorViewSet(viewsets.ModelViewSet):
 
    serializer_class = RevisorSerializer
    queryset = Revisor.objects.all()

class OfferViewSet(viewsets.ModelViewSet):
 
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()

class ApplicationViewSet(viewsets.ModelViewSet):
 
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

class TagViewSet(viewsets.ModelViewSet):
 
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

class ItemViewSet(viewsets.ModelViewSet):
 
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
