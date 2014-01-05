# -*- coding: utf-8 -*- 

"""
Django models for bookshelf project blog application
"""

from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	date = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.title + ' (%s)' % self.date

class Comment(models.Model):
	post = models.ForeignKey(Post)
	author = models.CharField(max_length=50)
	text = models.TextField()
	date = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.post.__unicode__() + ' ' + self.author + ' ' + self.text[:99]