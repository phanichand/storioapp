from rest_framework import serializers
from .models import Collection, Meaning,StoryPage,Story,Promotions,Meaning,Question,Choice 

class CollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Collection
		fields =['id','collection_name','collection_cover_image','collection_back_color']

class StoryPageSerializer(serializers.ModelSerializer):
	class Meta:
		model = StoryPage
		fields ='__all__'        

class StorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Story
		fields ='__all__'          
		depth=1


class StoryPageSerializer(serializers.ModelSerializer):
	class Meta:
		model = StoryPage
		fields ='__all__' 
		depth=1  

class PromotionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Promotions
		fields ='__all__' 
		depth=1    

class MeaningSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meaning
		fields ='__all__' 
		depth=1  

class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = ['choice','is_correct']
		depth=1

class QuestionSerializer(serializers.ModelSerializer):
	choices=ChoiceSerializer(many=True,read_only=True)
	class Meta:
		model=Question
		fields = ['id','question','choices']
		depth=1
