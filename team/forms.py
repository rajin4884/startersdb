from planphoto.models import PlanPost,PlanPhoto
from django.forms.models import inlineformset_factory

PlanPhotoInlineFormSet = inlineformset_factory(PlanPost, PlanPhoto,
    fields = ['image', 'title', 'description'],
    extra = 2)
