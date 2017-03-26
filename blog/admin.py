from django.contrib import admin
from .models import Post

# Register your models here.
# to be Post model available on administrating page
admin.site.register(Post)