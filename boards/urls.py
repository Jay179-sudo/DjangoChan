from django.urls import path

from .views import BoardListView, BoardDetailView, BoardUpdateView, BoardDeleteView, BoardCreateView
urlpatterns = [
    
    path("create/", BoardCreateView.as_view(), name='create'),
    path("<str:board>/", BoardListView.as_view(),name='board'),
    path("<str:board>/<int:pk>", BoardDetailView.as_view(), name='details'),
    path("<str:board>/update/<int:pk>", BoardUpdateView.as_view(),name='update'),
    path("<str:board>/delete/<int:pk>", BoardDeleteView.as_view(), name='delete'),
]