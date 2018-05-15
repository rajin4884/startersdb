from django.contrib import admin
from plan.models import PlanAlbum, PlanPhoto

# Register your models here.
class PhotoInline(admin.StackedInline):
    model = PlanPhoto
    extra = 2

class PlanAlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('name', 'description')

class PlanPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')

admin.site.register(PlanAlbum, PlanAlbumAdmin)
admin.site.register(PlanPhoto, PlanPhotoAdmin)
