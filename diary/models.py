# -*- coding: utf-8 -*- 

"""
Django models for bookshelf project diary application
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

class Reader(AbstractUser):
	"""
	A little bit extended standard user model. Extensions allow to count 
	wished and read books. These people are reading books.
	"""
	wished = models.IntegerField(default=0)
	read = models.IntegerField(default=0)

class Writer(models.Model):
	"""
	Data clas which describes writers (those people, who are writing books).
	"""
	name1 = models.CharField(max_length=30, verbose_name="First name")
	name2 = models.CharField(max_length=30, blank=True, \
		verbose_name="Second name")
	name3 = models.CharField(max_length=30, blank=True, \
		verbose_name="Third name")
	surname = models.CharField(max_length=30)

	born = models.DateField()
	died = models.DateField(blank=True)
	bio = models.TextField(blank=True)

	works = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name1[0] + '. ' + self.surname

class Work(models.Model):
	"""
	'Work' is more general term for a book. This data class describes all works that
	are 
	"""
	author = models.ForeignKey(Writer)
	reader = models.ForeignKey(Reader)
	annotation = models.TextField(blank=True)

	title = models.CharField(max_length=100)

	theme = models.CharField(max_length=20)
	genre = models.CharField(max_length=20, blank=True)
	form = models.CharField(max_length=20, blank=True)

	day_wished = models.DateField()
	day_read = models.DateField(blank=True)
	times_read = models.IntegerField(default=0,)

	active = models.BooleanField(default=True)

class Response(models.Model):
	work = models.ForeignKey(Work)
	responser = models.ForeignKey(Reader)

	title = models.CharField(max_length=100)
	response_text = models.TextField()

	date = models.DateField(auto_now_add=True)