from django.db import models
from django.contrib.auth.models import User
from django.urls import path, re_path, reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.


class TimespamtedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse("article-detail", args=(str(self.id)))
        return reverse('blog:home')


class Post(TimespamtedModel):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField(default='addtext')
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='category')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        #return reverse("article-detail", args=(str(self.id)))
        return reverse("blog:home")


class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


def approved_comments(self):
    return self.comments.filter(approved_comment=True)
