from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# to be Post model available on administrating page
admin.site.register(Post)
admin.site.register(Comment)
