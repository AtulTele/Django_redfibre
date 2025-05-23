
from django.contrib import admin
from django.template.response import TemplateResponse
from .models import TextToSpeech
from .models import (
    Article, Category, Tag, Reporter, Media, Comment,
    Location, AdBanner, Channel, Video
)

# ─── Inline setups ─────────────────────────────
class MediaInline(admin.TabularInline):
    model = Media
    extra = 1

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class TextToSpeechInline(admin.StackedInline):
    model = TextToSpeech
    extra = 0
    max_num = 1


# ─── Article admin ─────────────────────────────
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "reporter", "channel", "is_published", "created_at")
    list_filter = ("category", "reporter", "channel", "is_published")
    search_fields = ("title", "summary", "content")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [MediaInline, CommentInline, TextToSpeechInline,]
    autocomplete_fields = ["reporter", "category", "tags", "location", "channel"]


# ─── Admins for related models ────────────────
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)

class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)

class ReporterAdmin(admin.ModelAdmin):
    search_fields = ("name",)

class LocationAdmin(admin.ModelAdmin):
    search_fields = ("name",)

class ChannelAdmin(admin.ModelAdmin):
    search_fields = ("name",)

class VideoAdmin(admin.ModelAdmin):
    list_display = ("article", "caption")
    search_fields = ("caption", "article__title")


# ─── Custom AdminSite with dashboard ──────────
class CustomAdminSite(admin.AdminSite):
    site_header = "Satara ToDay Admin"
    site_title = "Satara Dashboard"
    index_title = "Dashboard"

    def index(self, request, extra_context=None):
        categories = Category.objects.all()
        labels = [cat.name for cat in categories]
        data = [Article.objects.filter(category=cat).count() for cat in categories]

        extra_context = extra_context or {}
        extra_context['labels'] = labels
        extra_context['data'] = data

        return super().index(request, extra_context=extra_context)

# ─── Instantiate and Register ─────────────────
custom_admin_site = CustomAdminSite(name='customadmin')

custom_admin_site.register(Article, ArticleAdmin)
custom_admin_site.register(Category, CategoryAdmin)
custom_admin_site.register(Tag, TagAdmin)
custom_admin_site.register(Reporter, ReporterAdmin)
custom_admin_site.register(Location, LocationAdmin)
custom_admin_site.register(Channel, ChannelAdmin)
custom_admin_site.register(Media)
custom_admin_site.register(Comment)
custom_admin_site.register(AdBanner)
custom_admin_site.register(TextToSpeech)
custom_admin_site.register(Video, VideoAdmin)


