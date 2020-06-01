from django.conf import settings
from django.db import models
from django.utils import timezone


class Streamer(models.Model):
    id = models.AutoField(primary_key=True)
    streamerName = models.TextField()

    def __str__(self):
        self.streamerName



