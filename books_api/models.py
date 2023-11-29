from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 180)
    author = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

    def __str__(self):
        return self.task