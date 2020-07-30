from django.contrib import admin
from .models import Post
# Register your models here.





class PostAdmin(admin.ModelAdmin):

    list_display = ['title','publishing_date'] #Admin panelini detaylandırır
    list_display_links = ['title','publishing_date'] #Linkler ekler
    list_filter = ['publishing_date']
    search_fields = ['title', 'content']

    class Meta:
        model = Post


#Admin paneline ekleme
admin.site.register(Post, PostAdmin)