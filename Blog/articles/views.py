from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import post
from .forms import PostForm, EditForm, DeleteForm

#def home(request):
  #  return render(request, 'home.html',{})

class HomeView(ListView):
    model = post
    template_name='home.html'
    #ordering = ['-id']
    ordering = ['-art_date']


class ArticleDetailView(DetailView):
    model = post
    template_name = 'articles_details.html'

class AddPostView(CreateView):
    model = post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = post
    form_class = DeleteForm
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

