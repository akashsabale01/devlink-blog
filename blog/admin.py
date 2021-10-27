from django.contrib import admin
from .models import Post

admin.site.site_header = "DevLink Admin"
admin.site.site_title = "DevLink Admin Area"

admin.site.register(Post)
