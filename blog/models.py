from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    CATEGORY_COUNTRIES = [
        ('argentina', 'Argentina'),
        ('belize', 'Belize'),
        ('bolivia', 'Bolivia'),
        ('brazil', 'Brazil'),
        ('canada', 'Canada'),
        ('chile', 'Chile'),
        ('costa_rica', 'Costa Rica'),
        ('ecuador', 'Ecuador'),
        ('guatemala', 'Guatemala'),
        ('mexico', 'Mexico'),
        ('honduras', 'Honduras'),
        ('nicaragua', 'Nicaragua'),
        ('paraguay', 'Paraguay'),
        ('peru', 'Peru'),
        ('venezuela', 'Venezuela'),     
        ('other', 'Other'),   
    ]

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    country = models.CharField(max_length=50, choices=CATEGORY_COUNTRIES, blank=False, null=False, default='other')
    content = models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    