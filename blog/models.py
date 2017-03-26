from django.db import models
from django.utils import timezone


class Post(models.Model):
    # foreign key to user
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    # it is now by default
    created_date = models.DateTimeField(
        default=timezone.now)
    # it may be blank or null
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
