from django.shortcuts import render , get_object_or_404
from .models import blog , comment
from django.views import generic

class index(generic.ListView):
  context_object_name = 'latest_blog_list'
  template_name = 'cogni/index.html'

  def get_queryset(self):
    return blog.objects.order_by('-id')[:3]

class DetailView(generic.DetailView):
  model = blog
  template_name = 'cogni/detail.view'
