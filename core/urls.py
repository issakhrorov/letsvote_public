from django.urls import path
from . import views

urlpatterns = [
    path('', views.getActivePromotions, name='activePromotions'),
    path('element', views.getElements, name='element'),
    path('category/<str:pk>', views.getCategoryPromotions, name='categoryPromotions'),
    path('category', views.getCategory, name='category'),
    path('card/<str:pk>', views.getCards, name='card'),
    path('info/<str:pk>', views.getInfo, name='info'),
    path('vote/', views.getVote, name="vote" ),
    path('rvote/', views.getRightVote, name="rightVote")
    # path('rightvote/', views.rightvote, name="rightvote" ),
]
