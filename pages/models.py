from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()


    def __str__(self):
        return self.title


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE, default=1)
    user = models.CharField(max_length=100)
    comment = models.TextField()