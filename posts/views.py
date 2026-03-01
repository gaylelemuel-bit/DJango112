from django.shortcuts import render
from django.views.generic import ListView, CreateView,DetailView,DeleteView,UpdateView
from posts.models import Post, Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)

# Create your views here.
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    published_status = Status.objects.get(name="published")
    queryset = Post.objects.filter(status=published_status)
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return(context)


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title","subtitle","body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(LoginRequiredMixin,DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "post"
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return(context)

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    context_object_name = "post"
    success_url = reverse_lazy("list")

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False 
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title","subtitle","body", "status"]
    context_object_name = "post"

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False 
    
class ArchivedPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/archived.html'  
    context_object_name = 'posts'       

    def get_queryset(self):
        return Post.objects.filter(status__name='archived')    
    
class DraftPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/draft.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status__name='draft')  
    

