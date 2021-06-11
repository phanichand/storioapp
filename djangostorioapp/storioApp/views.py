from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CollectionSerializer,StoryPageSerializer,StorySerializer,PromotionsSerializer,MeaningSerializer,QuestionSerializer

from .models import Collection, Question,StoryPage,Story,Promotions,Meaning
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Collection List':'/collection-list/',
		'Collection Detail View':'/collection-detail/<str:pk>/',
		'Collection Create':'/collection-create/',
		'Collection Update':'/collection-update/<str:pk>/',
		'Collection Delete':'/collection-delete/<str:pk>/',

        'Story List':'/story-list/',
        'Story List By Collection':'/story-detail/<str:collection>/',
		'Story Detail View':'/story-detail-id/<str:pk>/',
		'Story Create':'/story-create/',
		'Story Update':'/story-update/<str:pk>/',
		'Story Delete':'/story-delete/<str:pk>/',

        
		'StoryPage List By StoryId':'/storypage-detail/<str:story>/',
		'StoryPage Create':'/storypage-create/',
		'StoryPage Update':'/storypage-update/<str:pk>/',
		'StoryPage Delete':'/storypage-delete/<str:pk>/',

		'Promtotions':'/promotions/'
		}

	return Response(api_urls)

@api_view(['GET'])
def collectionList(request):
	collections = Collection.objects.all().order_by('-id')
	serializer = CollectionSerializer(collections, many=True, context={"request":request})
	return Response(serializer.data)

@api_view(['GET'])
def collectionDetail(request, pk):
	collections = Collection.objects.get(id=pk)
	serializer = CollectionSerializer(collections, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def collectionCreate(request):
	serializer = CollectionSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def collectionUpdate(request, pk):
	collection = Collection.objects.get(id=pk)
	serializer = CollectionSerializer(instance=collection, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def collectionDelete(request, pk):
	collection = Collection.objects.get(id=pk)
	collection.delete()

	return Response('Item succsesfully delete!')


# Stories
@api_view(['GET'])
def storyList(request):
	storys = Story.objects.all().order_by('-id')
	serializer = StorySerializer(storys, many=True, context={"request":request})
	return Response(serializer.data)

@api_view(['GET'])
def storyDetail(request, pk):
	story = Story.objects.get(id=pk)
	serializer = StorySerializer(story, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def storyCreate(request):
	serializer = StorySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def storyUpdate(request, pk):
	story = Story.objects.get(id=pk)
	serializer = StorySerializer(instance=story, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def storyDelete(request, pk):
	story = Story.objects.get(id=pk)
	story.delete()

	return Response('Item succsesfully delete!')


@api_view(['GET'])
def storyListByCollection(request, collection):
	story = Story.objects.filter(collection_id=collection)
	serializer = StorySerializer(story, many=True, context={"request":request})
	return Response(serializer.data)


@api_view(['GET'])
def storypageListByStory(request, story):
	story = StoryPage.objects.filter(story_id=story).order_by('story_page_no')
	serializer = StoryPageSerializer(story, many=True, context={"request":request})
	return Response(serializer.data)


@api_view(['POST'])
def storypageCreate(request):
	serializer = StoryPageSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def storypageUpdate(request, pk):
	storyPage = StoryPage.objects.get(id=pk)
	serializer = StoryPageSerializer(instance=storyPage, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def storypageDelete(request, pk):
	storyPage = StoryPage.objects.get(id=pk)
	storyPage.delete()

	return Response('Item succsesfully delete!')

@api_view(['GET'])
def PromotionList(request):
	promotions = Promotions.objects.all().order_by('-id')
	serializer = PromotionsSerializer(promotions, many=True, context={"request":request})
	return Response(serializer.data)

@api_view(['GET'])
def get_meaning(request,word):
	meanings = Meaning.objects.get(word=word)
	serializer = MeaningSerializer(meanings,context={"request":request})
	return Response(serializer.data)

@api_view(['GET'])
def get_quiz(request,story):
	quiz = Question.objects.filter(story=story)
	serializer = QuestionSerializer(quiz,many=True,context={"request":request})
	return Response(serializer.data)
