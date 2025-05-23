
from rest_framework import viewsets
from .models import Article, Category, Tag, Reporter, Media, Comment, Location, AdBanner, Channel, Video
from .serializers import (
    ArticleSerializer, CategorySerializer, TagSerializer,
    ReporterSerializer, MediaSerializer, CommentSerializer,
    LocationSerializer, AdBannerSerializer, ChannelSerializer, VideoSerializer
)

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ReporterViewSet(viewsets.ModelViewSet):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class AdBannerViewSet(viewsets.ModelViewSet):
    queryset = AdBanner.objects.all()
    serializer_class = AdBannerSerializer

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer    
