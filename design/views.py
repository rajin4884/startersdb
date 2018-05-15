from django.views.generic import ListView, DetailView
from design.models import DesignAlbum, DesignPhoto

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

class DesignAlbumLV(ListView):
    model = DesignAlbum

class DesignAlbumDV(DetailView):
    model = DesignAlbum

class DesignPhotoDV(DetailView):
    model = DesignPhoto

#--- Add/Change/Update/Delete for Photo
class DesignPhotoCreateView(LoginRequiredMixin, CreateView):
    model = DesignPhoto
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('design:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(DesignPhotoCreateView, self).form_valid(form)

class DesignPhotoChangeLV(LoginRequiredMixin, ListView):
    template_name = 'design/photo_change_list.html'

    def get_queryset(self):
        return DesignPhoto.objects.filter(owner=self.request.user)

class DesignPhotoUpdateView(LoginRequiredMixin, UpdateView) :
    model = DesignPhoto
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('design:index')

class DesignPhotoDeleteView(LoginRequiredMixin, DeleteView) :
    model = DesignPhoto
    success_url = reverse_lazy('design:index')

#--- Add/Change/Update/Delete for Album
#--- Change/Delete for Album
class DesignAlbumChangeLV(LoginRequiredMixin, ListView):
    template_name = 'design/album_change_list.html'

    def get_queryset(self):
        return DesignAlbum.objects.filter(owner=self.request.user)

class DesignAlbumDeleteView(LoginRequiredMixin, DeleteView) :
    model = DesignAlbum
    success_url = reverse_lazy('design:index')


#--- InlineFormSet View
#--- Add/Update for Album
from django.shortcuts import redirect
from design.forms import PhotoInlineFormSet

class DesignAlbumPhotoCV(LoginRequiredMixin, CreateView):
    model = DesignAlbum
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(DesignAlbumPhotoCV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect('design:album_detail', pk=self.object.id)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class DesignAlbumPhotoUV(LoginRequiredMixin, UpdateView):
    model = DesignAlbum
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(DesignAlbumPhotoUV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
