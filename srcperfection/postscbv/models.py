from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings


# Create your models here.

def content_file_name(instance, filename):
    return '/'.join([instance.user.username, filename])

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=220)
	content = models.TextField()
	image = models.ImageField(upload_to=content_file_name,
					height_field='height_field',
					width_field='width_field',
					null=True,
					blank=True)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	draft = models.BooleanField(default=False)
	email = models.EmailField(max_length=220, default='please_change@gmail.com')

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('postscbv:post_detail', kwargs={'pk':self.pk})

	class Meta:
		ordering = ['-id']
		
		

