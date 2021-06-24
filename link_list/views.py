from django.shortcuts import render
from django.views.generic import ListView
from .models import Link

class LinksListView(ListView):
    template_name = 'link_list/index.html'
    queryset = Link.objects.all()
    context_object_name = 'links'