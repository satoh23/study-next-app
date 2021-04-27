from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField('内容', blank=True, null=True, default='よろしくお願いします')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title


class Task(models.Model):

    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title
