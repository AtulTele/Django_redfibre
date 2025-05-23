
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ArticleViewSet, CategoryViewSet, TagViewSet,
    ReporterViewSet, MediaViewSet, CommentViewSet,
    LocationViewSet, AdBannerViewSet, ChannelViewSet,VideoViewSet
)

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'reporters', ReporterViewSet)
router.register(r'media', MediaViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'ad-banners', AdBannerViewSet)
router.register(r'channels', ChannelViewSet)
router.register(r'videos', VideoViewSet)  # ✅ Consistent with others



urlpatterns = [
    path('api/', include(router.urls)),
]
