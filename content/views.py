
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Post

# Create your views here.

def home(request):
    return render(request, 'home.html')


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'content/post_list.html'
    context_object_name = 'posts'
    def get_queryset(self):
        # Only show posts created by the logged-in user
        return Post.objects.filter(author=self.request.user)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'content', 'category', 'tags', 'status']
    template_name = 'content/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # set author automatically
        return super().form_valid(form)

class PostView(DetailView):
    model = Post
    template_name = 'content/post_view.html'
    context_object_name = 'post'

class PostEditView(UpdateView):
    model = Post
    fields = ['title', 'slug', 'content', 'category', 'tags', 'status']
    template_name = 'content/post_edit.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        # Only allow editing of user's own posts
        return Post.objects.filter(author=self.request.user)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'content/post_delete.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        # Only allow editing of user's own posts
        return Post.objects.filter(author=self.request.user)

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('post_list')
