from django.urls import path

from .views import ListView, DetailView, UpdateView, DeleteView, CreateView
urlpatterns = [
    
    path("<str:board>/", ListView.as_view(),name='board'),

        path("<str:board>/<int:pk>", DetailView.as_view(), name='details'),
        path("<str:board>/update/<int:pk>", UpdateView.as_view(),name='update'),
        path("<str:board>/delete/<int:pk>", DeleteView.as_view(), name='delete'),
        path("create/", CreateView.as_view(), name="create"),

    # path("culture/", ListView.as_view(), name='culture'),

    #     path("culture/<int:pk>", DetailView.as_view(), name='animation_details'),
    #     path("culture/update/<int:pk>", UpdateView.as_view(),name='animation_update'),
    #     path("culture/delete/<int:pk>", DeleteView.as_view(), name='animation_delete'),

    # path("videogames/", ListView.as_view(),name='videogames'),

    #     path("videogames/<int:pk>", DetailView.as_view(), name='animation_details'),
    #     path("videogames/update/<int:pk>", UpdateView.as_view(),name='animation_update'),
    #     path("videogames/delete/<int:pk>", DeleteView.as_view(), name='animation_delete'),

    # path("musicphotography/", ListView.as_view(),name='musicphotography'),

    #     path("musicphotography/<int:pk>", DetailView.as_view(), name='animation_details'),
    #     path("musicphotography/update/<int:pk>", UpdateView.as_view(),name='animation_update'),
    #     path("musicphotography/delete/<int:pk>", DeleteView.as_view(), name='animation_delete'),
]