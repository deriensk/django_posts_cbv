from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=220)
	content = models.TextField()
	draft = models.BooleanField(default=False)
	email = models.EmailField(max_length=220, default='please_change@gmail.com')

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('postscbv:post_detail', kwargs={'pk':self.pk})
		

