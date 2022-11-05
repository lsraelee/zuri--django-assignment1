from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ArtisteViewSet, SongViewSet, LyricViewSet

router = DefaultRouter()
router.register(r'artiste', ArtisteViewSet, basename='artiste' )
router.register(r'song', SongViewSet, basename='song')
router.register(r'lyric', LyricViewSet, basename='lyric')

urlpatterns = []

urlpatterns += router.urls