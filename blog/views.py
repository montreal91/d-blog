# -*- coding: utf-8 -*- 

from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from models import Post

class BlogView(CreateView):
	template_name = 'blog/index.html'
	model = Post
	success_url = '/blog/'
	fields = ['title', 'text']

	def get_post_list(self):
		return Post.objects.order_by('-date')[:10]

	def get_context_data(self, **kwargs):
		context = super(BlogView, self).get_context_data(**kwargs)
		context['moment'] = timezone.now()
		context['post_list'] = self.get_post_list()
		return context

class PostView(DetailView):
	model = Post
	template_name = 'blog/post.html' 