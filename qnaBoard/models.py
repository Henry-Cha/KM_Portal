from django.db import models
from django.contrib.auth.models import User
from log_app.models import CustomUser

class Post(models.Model): 
    title = models.CharField(max_length=200)
    content = models.TextField()
    #writer = models.CharField(max_length=20)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    hits = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(verbose_name='댓글수', null=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    @property
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()

class Answer(models.Model): 
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='answer_set') #  수정 : relate_name == class 별칭 추가 ForeignKey Post
    content = models.TextField()
    #writer = models.CharField(max_length=20)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    select = models.BooleanField(default=False)
    def __str__(self):
        return self.content