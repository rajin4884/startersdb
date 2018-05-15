from design.models import DesignAlbum, DesignPhoto
from django.forms.models import inlineformset_factory

PhotoInlineFormSet = inlineformset_factory(DesignAlbum, DesignPhoto,
    fields = ['image', 'title', 'description'],
    extra = 2)
