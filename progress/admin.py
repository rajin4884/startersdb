from django.contrib import admin
from progress.models import ProgressAlbum, ProgressPhoto

# Register your models here.
class PhotoInline(admin.StackedInline):
    model = ProgressPhoto
    extra = 2

class ProgressAlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('name', 'description')

class ProgressPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')

admin.site.register(ProgressAlbum, ProgressAlbumAdmin)
admin.site.register(ProgressPhoto, ProgressPhotoAdmin)
