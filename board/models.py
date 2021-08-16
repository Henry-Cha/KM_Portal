from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.CharField(max_length=20)
    date = models.DateTimeField()
    hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()

class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.CharField(max_length=20)
    date = models.DateTimeField()

    def __str__(self):
        return self.content
    