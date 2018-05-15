from django.contrib import admin
from design.models import DesignAlbum, DesignPhoto

# Register your models here.
class PhotoInline(admin.StackedInline):
    model = DesignPhoto
    extra = 2

class DesignAlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('name', 'description')

class DesignPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')

admin.site.register(DesignAlbum, DesignAlbumAdmin)
admin.site.register(DesignPhoto, DesignPhotoAdmin)
