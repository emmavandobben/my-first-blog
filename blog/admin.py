from django.contrib import admin

from .models import Label
from .models import Post


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_date"]
    list_filter = ["title", "published_date"]
    search_fields = ["title", "published_date"]


admin.site.register(Post, PostAdmin)
admin.site.register(Label)
