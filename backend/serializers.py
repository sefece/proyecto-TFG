from rest_framework import serializers
from .models import User, Administrator, Applicant, Bidder, Revisor, Offer, Application, Tag, Item
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name', 'password',)
 
class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('id', 'user',)

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ('id', 'user',)

class BidderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bidder
        fields = ('id', 'user',)

class RevisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revisor
        fields = ('id', 'user',)

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'bidder', 'revisor',)

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'applicant', 'offer',)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag_name', 'tag_description',) 

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'tag', 'item_name', 'item_description', 'file',)