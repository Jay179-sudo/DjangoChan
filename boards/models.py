# articles/models.py
from django.conf import settings
from django.db import models
from django.urls import reverse


class Board(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    TAG_CHOICES = [
        ("Animations", "Animations"),
        ("Culture", "Culture"),
        ("Video Games", "Video Games"),
        ("Music and Photography", "Music and Photography")
    ]
    tag = models.TextField(choices=TAG_CHOICES, default="Animations")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        returnval = self.tag.lower()
        if returnval == "music and photography":
            returnval = "musicphotography"
        elif returnval == "video games":
            returnval = "videogames"
        
        return reverse("board", kwargs={"board": returnval})
