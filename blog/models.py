from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField 

# Create your models here.


STATUS_CHOICES = (
    ('d','DRAFT'),
    ('p', 'PUBLISHED'),
)

CATEGORY_CHOICES = (
    ('f', 'frontend'),
    ('b', 'backend'),
    
)

class Post(models.Model):
    
    title= models.CharField(max_length=50)
    content= models.TextField()
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image= models.URLField(max_length=5000, blank=True)
    status= models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    published_date= models.DateTimeField(auto_now_add=True)
    last_updated= models.DateTimeField(auto_now=True)
    slug= AutoSlugField(populate_from="title")
    
    def __str__(self):
        return self.title
    
    def slugify_function(content):
        return content.replace(' ', '-').lower()
    
    
    # şimdilik kullanmadım. Modele fieldler ekliyor. 
    
    # @property
    # def comments(self):
    #     return self.comment_set.all()

    # @property
    # def get_comment_count(self):
    #     return self.comment_set.count()

    # @property
    # def get_view_count(self):
    #     return self.postview_set.count()

    # @property
    # def get_like_count(self):
    #     return self.like.count()
    
    
class Comment(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    time_stamp = models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    
    def __str__(self):
        return self.user.username

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_views")
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return self.user.username
    
