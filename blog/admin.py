from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('title', 'content')

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set author during the first save.
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
