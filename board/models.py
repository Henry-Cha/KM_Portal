from django.db import models
from django.contrib.auth.models import User
from log_app.models import CustomUser

######################## 일반 게시판 ##############################
class FreePosting(models.Model): # 수정 : Post >> FreePosting 변경
    title = models.CharField(max_length=200)
    content = models.TextField()
    #writer = models.CharField(max_length=20)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    hits = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(verbose_name='댓글수', null=True)
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
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    def __str__(self):
        return self.content
######################## 공학 게시판 ##############################
class EngPosting(models.Model): 
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    hits = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(verbose_name='댓글수', null=True)
    def __str__(self):
        return self.title
    @property
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()

class EngAnswer(models.Model): 
    post = models.ForeignKey(EngPosting, on_delete=models.CASCADE,related_name='eng_set')
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    def __str__(self):
        return self.content
######################## 자연과학 게시판 ##############################
class SciPosting(models.Model): 
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    hits = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(verbose_name='댓글수', null=True)
    def __str__(self):
        return self.title
    @property
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()

class SciAnswer(models.Model): 
    post = models.ForeignKey(SciPosting, on_delete=models.CASCADE,related_name='sci_set')
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    def __str__(self):
        return self.content
######################## 의학/간호 게시판 ##############################
class MedPosting(models.Model):  #@
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    hits = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(verbose_name='댓글수', null=True)
    def __str__(self):
        return self.title
    @property
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()

class MedAnswer(models.Model):    #@
    post = models.ForeignKey(MedPosting, on_delete=models.CASCADE,related_name='med_set')  #@
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    def __str__(self):
        return self.content
######################## 예체능 게시판 ##############################
class ArtPosting(models.Model):  #@
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    hits = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(verbose_name='댓글수', null=True)
    def __str__(self):
        return self.title
    @property
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()

class ArtAnswer(models.Model):    #@
    post = models.ForeignKey(ArtPosting, on_delete=models.CASCADE,related_name='art_set')  #@2
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    def __str__(self):
        return self.content
######################## 인문/사회 게시판 ##############################
class SocPosting(models.Model):  #@
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    hits = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(verbose_name='댓글수', null=True)
    def __str__(self):
        return self.title
    @property
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()

class SocAnswer(models.Model):    #@
    post = models.ForeignKey(SocPosting, on_delete=models.CASCADE,related_name='soc_set')  #@2
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField()
    def __str__(self):
        return self.content