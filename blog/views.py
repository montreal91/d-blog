# -*- coding: utf-8 -*- 

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.views import generic

from models import Post

moment = timezone.now()

class BlogView(generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'post_list'

	def get_queryset(self):
		return Post.objects.order_by('-date')[:10]

	def get_context_data(self, **kwargs):
		context = super(BlogView, self).get_context_data(**kwargs)
		context['moment'] = moment
		return context

class PostView(generic.DetailView):
	model = Post
	template_name = 'blog/post.html' 

#	def get_context_data(self, **kwargs):
#		context = super(BlogView, self).get_context_data(**kwargs)
#		context['moment'] = moment
#		return context