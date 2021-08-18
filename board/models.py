from django.db import models
from django.contrib.auth.models import User

class FreePosting(models.Model): # 수정 : Post >> FreePosting 변경
    title = models.CharField(max_length=200)
    content = models.TextField()
    #writer = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()

class FreeAnswer(models.Model): # 수정 : Post >> FreeAnswer 변경
    post = models.ForeignKey(FreePosting, on_delete=models.CASCADE,related_name='free_set') #  수정 : relate_name == class 별칭 추가 ForeignKey Post >> FreePosting 변경
    content = models.TextField()
    #writer = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.content
    