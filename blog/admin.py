from django.contrib import admin
from .models import Creator, Post

@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ['name','surname','country', 'add_date']
    search_fields = ['name','surname','country', 'add_date']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','country', 'add_date']
    search_fields = ['name','author','country', 'add_date']

# Register your models here.
