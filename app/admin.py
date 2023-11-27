from django.contrib import admin

from app.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','description','image']
    
admin.site.register(Post,PostAdmin)