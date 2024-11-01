from django.contrib import admin

from petstagram.common.models import Like, Comment
from petstagram.pets.models import Pet


# Register your models here.
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
