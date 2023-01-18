from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
from .models import Board


class BoardListView(LoginRequiredMixin, ListView):
    model = Board
    template_name = "board_list.html"


class BoardDetailView(LoginRequiredMixin, DetailView):
    model = Board
    template_name = "board_detail.html"


class BoardDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Board
    template_name = "board_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user


class BoardUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Board
    template_name = "board_update.html"
    fields = (
        "title",
        "body",
        "tag",
    )

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user


class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    template_name = "board_new.html"
    fields = (
    "title",
    "body",
    "tag",
    )

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
