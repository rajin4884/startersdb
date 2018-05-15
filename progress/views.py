from django.views.generic import ListView, DetailView
from progress.models import ProgressAlbum, ProgressPhoto

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

class ProgressAlbumLV(ListView):
    model = ProgressAlbum

class ProgressAlbumDV(DetailView):
    model = ProgressAlbum

class ProgressPhotoDV(DetailView):
    model = ProgressPhoto

#--- Add/Change/Update/Delete for Photo
class ProgressPhotoCreateView(LoginRequiredMixin, CreateView):
    model = ProgressPhoto
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('progress:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ProgressPhotoCreateView, self).form_valid(form)

class ProgressPhotoChangeLV(LoginRequiredMixin, ListView):
    template_name = 'progress/photo_change_list.html'

    def get_queryset(self):
        return ProgressPhoto.objects.filter(owner=self.request.user)

class ProgressPhotoUpdateView(LoginRequiredMixin, UpdateView) :
    model = ProgressPhoto
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('progress:index')

class ProgressPhotoDeleteView(LoginRequiredMixin, DeleteView) :
    model = ProgressPhoto
    success_url = reverse_lazy('progress:index')

#--- Add/Change/Update/Delete for Album
#--- Change/Delete for Album
class ProgressAlbumChangeLV(LoginRequiredMixin, ListView):
    template_name = 'progress/album_change_list.html'

    def get_queryset(self):
        return ProgressAlbum.objects.filter(owner=self.request.user)

class ProgressAlbumDeleteView(LoginRequiredMixin, DeleteView) :
    model = ProgressAlbum
    success_url = reverse_lazy('progress:index')


#--- InlineFormSet View
#--- Add/Update for Album
from django.shortcuts import redirect
from progress.forms import PhotoInlineFormSet

class ProgressAlbumPhotoCV(LoginRequiredMixin, CreateView):
    model = ProgressAlbum
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(ProgressAlbumPhotoCV, self).get_context_data(**kwargs)
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
            return redirect('progress:album_detail', pk=self.object.id)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class ProgressAlbumPhotoUV(LoginRequiredMixin, UpdateView):
    model = ProgressAlbum
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(ProgressAlbumPhotoUV, self).get_context_data(**kwargs)
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
