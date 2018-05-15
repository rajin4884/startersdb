from plan.models import PlanAlbum, PlanPhoto
from django.forms.models import inlineformset_factory

PhotoInlineFormSet = inlineformset_factory(PlanAlbum, PlanPhoto,
    fields = ['image', 'title', 'description'],
    extra = 2)
