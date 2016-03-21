from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class  Question(models.Model):
	title = models.CharField(max_length=50) 
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User, related_name='likes_set')
	
	def  __unicode__(self):
		return self.title
	def  get_url(self):
		return '/question/%d/' % self.pk

	class  Meta:
		db_table = 'question'
		ordering = ['-added_at']

class  Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	question = models.OneToOneField(Question)
	#rating = models.OneToOneField(QRating)
	author = models.ForeignKey(User)
	#likes = models.ManyToManyField(Like)
	
	def  __unicode__(self):
		return self.title
	def  get_absolute_url(self):
		return '/answer/%d/' % self.pk

	class  Meta:
		db_table = 'answer'
	ordering = ['-added_at']






# Create your models here.my
