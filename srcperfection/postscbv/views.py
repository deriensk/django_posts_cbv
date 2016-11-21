from django.shortcuts import render

from django.core.urlresolvers import reverse

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



from .models import Post
from .forms import PostModelForm

# Create your views here.

class PostCreate(CreateView):
	template_name = 'post_form.html'
	form_class = PostModelForm

	def form_valid(self, form):
		form.instance.added_by = self.request.user
		form.instance.last_edited_by = self.request.user

		return super(PostCreate, self).form_valid(form)

	def get_success_url(self):
		return reverse('postscbv:post_list')	


class PostList(ListView):
	model = Post

	
class PostDetail(DetailView):
	
	model = Post

	

class PostDelete(DeleteView):
	model = Post

	def get_success_url(self):
		return reverse('postscbv:post_list')


class PostUpdate(UpdateView):
	model = Post
	template_name = 'post_form.html'
	form_class = PostModelForm





