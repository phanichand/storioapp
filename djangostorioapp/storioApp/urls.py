from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('collection-list/', views.collectionList, name="collection-list"),
	path('collection-detail/<str:pk>/', views.collectionDetail, name="collection-detail"),
	path('collection-create/', views.collectionCreate, name="collection-create"),

	path('collection-update/<str:pk>/', views.collectionUpdate, name="collection-update"),
	path('collection-delete/<str:pk>/', views.collectionDelete, name="collection-delete"),

    path('story-list/', views.storyList, name="story-list"),
    path('story-detail-id/<str:pk>/', views.storyDetail, name="story-id-storyDetail"),
	path('story-detail/<str:collection>/', views.storyListByCollection, name="story-detail"),
	path('story-create/', views.storyCreate, name="story-create"),

	path('story-update/<str:pk>/', views.storyUpdate, name="story-update"),
	path('story-delete/<str:pk>/', views.storyDelete, name="story-delete"),



    path('storypage-detail/<str:story>/', views.storypageListByStory, name="storypage-detail"),
	path('storypage-create/', views.storypageCreate, name="storypage-create"),

	path('storypage-update/<str:pk>/', views.storypageUpdate, name="storypage-update"),
	path('storypage-delete/<str:pk>/', views.storypageDelete, name="storypage-delete"),
	path('promotions/', views.PromotionList, name="promotions"),
	path('get-meaning/<str:word>/',views.get_meaning,name="meanings"),
	path('quiz/<int:story>/',views.get_quiz,name="quiz"),

]
