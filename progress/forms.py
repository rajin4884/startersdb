from progress.models import ProgressAlbum, ProgressPhoto
from django.forms.models import inlineformset_factory

PhotoInlineFormSet = inlineformset_factory(ProgressAlbum, ProgressPhoto,
    fields = ['image', 'title', 'description'],
    extra = 2)
