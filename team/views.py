from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, DetailView, TemplateView
from mysite.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
# from team.models import PlanPost,PlanPhoto
from django.views.generic.edit import CreateView


def topic(request):
    return render(request, 'team/topic.html', {})

def member(request):
    return render(request, 'team/member.html', {})

def settings(request):
    return render(request, 'team/settings.html', {})

def plan(request):
    return render(request, 'team/plan.html', {})

# class PlanLv(ListView) :
#     model =PlanPost
#     template_name = 'team/plan.html'
#     paginate_by = 2
#
# class PlanDV(DetailView) :
#     model =PlanPost
#     # template_name = "team/plan_detail.html"
#
# class PlanPhotoDV(DetailView):
#     model=PlanPhoto
    # template_name="team/planphoto_detail.html"



#
# class PlanPostCreateView(LoginRequiredMixin, CreateView):
#     model = PlanPost
#     fields = ['title', 'slug', 'description', 'content']
#     initial = {'slug': 'auto-filling-do-not-input'}
#     success_url = reverse_lazy('team:plan')
#
#     def form_valid(self, form):
#         form.instance.owner = self.request.user
#         return super(PlanPostCreateView, self).form_valid(form)

# class PlanPostDV(DetailView) :
#     model = PlanPost

def sitemap(request):
    return render(request, 'team/sitemap.html', {})

def design(request):
    return render(request, 'team/design.html', {})

def progress(request):
    return render(request, 'team/progress.html', {})
