# musicrecommend/urls.py
from django.urls import path
from .views import SongListView, home, about,RecommendSongsView

urlpatterns = [
    path('songs/', SongListView.as_view(), name='song-list'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    # path('liked-songs/', LikedSongsView.as_view(), name='liked-songs'),
    # path('liked-songs/<int:song_id>', LikedSongsView.as_view(), name='liked-songs'),
    path('recommend-songs/<int:song_id>/', RecommendSongsView, name='recommend-songs'),
]


