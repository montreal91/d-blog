# -*- coding: utf-8 -*- 

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.views import generic

from models import Post

# Create your views here.

def index(request):
	post_list = Post.objects.order_by('-date')[:10]
	months = {1: 'January', 
		2: 'February', 
		3: 'March', 
		4: 'April', 
		5: 'May', 
		6: 'June', 
		7: 'July', 
		8: 'August', 
		9: 'September', 
		10: 'October', 
		11: 'November', 
		12: 'December'}
	moment = timezone.now()
	today = str(moment.day) + ' ' + months[moment.month] + ' ' + str(moment.year)
	context = {'post_list':post_list, 'today': today}
	return render(request, 'blog/index.html', context)

def post(request, post_id):
	pass

class BlogView(generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'post_list'

	def get_queryset(self):
		return Post.objects.order_by('-date')[:10]

class PostView(generic.DetailView):
	model = Post
	template_name = 'blog/post.html' 