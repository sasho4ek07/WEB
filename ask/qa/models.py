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
		return '/question/%d/' % self.id

	class  Meta:
		db_table = 'question'
		ordering = ['-id']

class  Answer(models.Model):
	question = models.ForeignKey(Question, null= True, on_delete=models.SET_NULL, related_name='question_set')
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	author = models.ForeignKey(User)
	#likes = models.ManyToManyField(Like)
	#rating = models.OneToOneField(QRating)
	def  __unicode__(self):
		return self.text
	def  get_url(self):
		return reverse('questions', kwargs={'id': self.id})

	class  Meta:
		db_table = 'answer'
	ordering = ['-added_at']






# Create your models here.my
