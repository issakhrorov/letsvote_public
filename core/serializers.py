from rest_framework.serializers import ModelSerializer
from .models import Category, Promotion, Element, Vote, Voter

class CategorySerializer(ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'

class PromotionSerializer(ModelSerializer):
  class Meta:
    model = Promotion 
    fields = '__all__'

class ElementSerializer(ModelSerializer):
  class Meta: 
    model = Element
    fields = '__all__'

class VoterSerializer(ModelSerializer):
  model = Voter
  fields = '__all__'

class VoteSerializer(ModelSerializer):
  model = Vote
  fields = '__all__'