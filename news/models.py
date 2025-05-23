
# models.py
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subcategories', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        full_name = self.name
        if self.parent:
            full_name = f"{self.parent.name} > {self.name}"
        return full_name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Reporter(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to="reporters/", blank=True, null=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Channel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="channels/logos/", blank=True, null=True)

    def __str__(self):
        return self.name
    
    

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.TextField()
    content = RichTextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    channel = models.ForeignKey(Channel, on_delete=models.SET_NULL, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Media(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="media")
    image = models.ImageField(upload_to="articles/images/", blank=True, null=True)
    video = models.FileField(upload_to="articles/videos/", blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Media for {self.article.title}"

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.article.title}"

class AdBanner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="ads/")
    link = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class TextToSpeech(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name="tts")
    audio_file = models.FileField(upload_to="tts/", blank=True, null=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"TTS for {self.article.title}"

class Video(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="videos")
    image = models.ImageField(upload_to="articles/images/", blank=True, null=True)
    video = models.FileField(upload_to="articles/videos/", blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Video for {self.article.title}"



