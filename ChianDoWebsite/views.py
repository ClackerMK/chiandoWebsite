from django.db.models import QuerySet
from django.db.models.aggregates import Count
from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from ChianDoWebsite.models import Blog, Event, Gallery

# Create your views here.

class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "latest_blog_post"

    def get_queryset(self):
        if self.request.GET.get('num') is not None:
            num = int(self.request.GET.get('num'))
        else:
            num = 9

        blogs =  Blog.objects.filter(visible=True).order_by('-pinned', '-pub_date')[:num]

        return blogs


class BlogView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs);

        return context


class GalleryView(generic.ListView):
    template_name = "galerien.html"

    model = Gallery

    def get_context_data(self, **kwargs):
        context = super(GalleryView,self).get_context_data(**kwargs)

        return context


class EventView(generic.ListView):
    template_name = "events.html"

    def get_queryset(self):

        events = Event.objects.filter(start_date__gte=timezone.now()).order_by('-start_date')

        return events


class ArchiveView(generic.ListView):
    template_name = "archive.html"

    model = Blog

    def get_context_data(self, **kwargs):
        context = super(ArchiveView, self).get_context_data(**kwargs)

        return context
