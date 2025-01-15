from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    #indexes
    class Meta:
        ordering=['-publish']
        indexes=[
            models.Index(fields=['-publish'])
        ]

    #status and Status is an enum with readable values {variable_name='value','label'}
    class Status(models.TextChoices):
        DRAFT='DF','Draft'
        PUBLISHED='PB','Published'

    #fields
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    author=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts',
    )
    body=models.TextField()

    #date fields
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )

    def __str__(self):
        return self.title