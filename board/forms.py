from django.forms import ModelForm

from .models import *

######################## 일반 게시판 ##############################
class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })        
    class Meta:
        model = FreePosting # 수정 : Post >> FreePosting 변경
        fields = ['title', 'content','hits']
        
######################## 공학 게시판 ##############################
class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })        
    class Meta:
        model = EngPosting 
        fields = ['title', 'content']
        
######################## 자연과학 게시판 ##############################
class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })        
    class Meta:
        model = SciPosting 
        fields = ['title', 'content']
######################## 의학/간호 게시판 ##############################
class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })        
    class Meta:
        model = MedPosting  #@
        fields = ['title', 'content']
######################## 예체능 게시판 ##############################
class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })        
    class Meta:
        model = ArtPosting  #@
        fields = ['title', 'content']
######################## 인문/사회 게시판 ##############################
class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })        
    class Meta:
        model = SocPosting  #@
        fields = ['title', 'content']