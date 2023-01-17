from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView , DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
from .models import Board

class ListView(LoginRequiredMixin, ListView):
    model = Board
    template_name="board_list.html"

class DetailView(LoginRequiredMixin, DetailView):
    model = Board
    template_name="board_detail.html"

class DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    model = Board
    template_name="board_delete.html"
    success_url=reverse_lazy("home")

    
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class UpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Board
    template_name = "board_update.html"
    fields = (
        "title",
        "body",
        "tag",
    )
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user


class CreateView(LoginRequiredMixin, CreateView):
    model = Board
    template_name = "board_create.html"
    fields = (
        "title",
        "body",
        "tag",
    )
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
