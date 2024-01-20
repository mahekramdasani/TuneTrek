import nltk
nltk.download('punkt')
import pandas as pd
from django.db.models import Q  # Import Q for complex queries
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from nltk.stem.porter import PorterStemmer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rest_framework.decorators import api_view
from .models import Song
from .serializers import SongSerializer
# from api.models import UserLike
# from api.serializers import UserLikeSerializer

stemmer = PorterStemmer()

def tokenization(txt):
    tokens = nltk.word_tokenize(txt)
    stemming = [stemmer.stem(w) for w in tokens]
    return " ".join(stemming)

def recommend_songs_based_on_lyrics(song_title, song_artist):
    df = pd.DataFrame(Song.objects.all().values())
    df['lyrics'] = df['lyrics'].str.lower().replace(r'^\w\s', ' ').replace(r'\n', ' ', regex=True)
    df['lyrics'] = df['lyrics'].apply(lambda x: tokenization(x))

    tfidvector = TfidfVectorizer(analyzer='word', stop_words='english')
    matrix = tfidvector.fit_transform(df['lyrics'])
    similarity = cosine_similarity(matrix)

    idx = df[(df['title'] == song_title) & (df['artist'] == song_artist)].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])

    songs = []
    for m_id in distances[1:6]:  # Change this to 6 to get 5 songs
        songs.append(df.iloc[m_id[0]])

    return songs

@api_view(['GET'])
def RecommendSongsView(request, song_id):
    try:
        song = Song.objects.get(song_id=song_id)
    except Song.DoesNotExist:
        return Response({"error": "Song not found"}, status=status.HTTP_404_NOT_FOUND)

    recommended_songs_data = recommend_songs_based_on_lyrics(song.title, song.artist)

    # Retrieve Song objects based on recommended song data
    recommended_songs = [Song.objects.get(title=song['title'], artist=song['artist']) for song in recommended_songs_data]

    serializer = SongSerializer(recommended_songs, many=True)
    return Response(serializer.data)


class SongListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


def home(request):
    
    return render(request, "index.html")

def about(request):
    return HttpResponse("<h1>Welcome to about page</h1>")
# class LikedSongsView(APIView):
#     def get(self, request):
#         user = request.user
#         liked_songs = UserLike.objects.filter(user=user)
#         serializer = UserLikeSerializer(liked_songs, many=True)
#         return Response(serializer.data)



# class RecommendSongsView(APIView):
#     def get(self, request):
#         # user = request.user
#         # liked_songs = UserLike.objects.filter(user=user)
#         # # Creating a list of dictionaries containing 'title' and 'artist' for each liked song
#         # liked_songs_data = [{'title': song.song.title, 'artist': song.song.artist} for song in liked_songs]
        
#         recommended_songs_data = recommend_songs_based_on_lyrics(liked_songs_data)

#         # Retrieve Song objects based on recommended song data
#         recommended_songs = [Song.objects.get(title=song['title'], artist=song['artist']) for song in recommended_songs_data]

#         serializer = SongSerializer(recommended_songs, many=True)
#         return Response(serializer.data)


# class LikedSongsView(APIView):
#     def get(self, request):
#         if request.user.is_authenticated:
#             liked_songs = UserLike.objects.filter(user=request.user).select_related('song')
#             serializer = UserLikeSerializer(liked_songs, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

#     def post(self, request, song_id):
#         if request.user.is_authenticated:
#             song = get_object_or_404(Song, id=song_id)
            
#             # Create a UserLike instance to record the like
#             user_like, created = UserLike.objects.get_or_create(user=request.user, song=song)
            
#             return Response({"message": "Song liked successfully"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

#     def delete(self, request, song_id):
#         if request.user.is_authenticated:
#             song = get_object_or_404(Song, id=song_id)
            
#             # Delete the UserLike instance to remove the like
#             user_like = UserLike.objects.filter(user=request.user, song=song).first()
#             if user_like:
#                 user_like.delete()

#             return Response({"message": "Song unliked successfully"}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
