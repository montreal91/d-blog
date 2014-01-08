# -*- coding: utf-8 -*- 
import json

from django.utils import timezone
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from models import Post

class AjaxResponseMixin(object):
	"""
	Mixin to add AJAX support to a form.
	"""

	def render_to_json_response(self, context, **response_kwargs):
		data = json.dumps(context)
		response_kwargs['content-type'] = 'application/json'
		return HttpResponse(data, **response_kwargs)

	def form_invalid(self, form):
		response = super(AjaxResponseMixin, self).form_invalid(form)
		if self.request.is_ajax():
			return self.render_to_json_response(form.errors, status=400)
		else:
			return response

	def form_valid(self, form):
		response = super(AjaxResponseMixin, self).form_valid(form)
		if self.request.is_ajax():
			data = {
				'pk': self.object.pk,
			}
			return self.render_to_json_response(data)
		else:
			return response


class BlogView(AjaxResponseMixin, CreateView):
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

class CreatePostView(CreateView):
	model = Post
	fields = ['title', 'text']

class UpdatePostView(UpdateView):
	model = Post
	fields = ['title', 'text']

class DeletePostView(DeleteView):
	model = Post
	success_url = reverse_lazy('index')