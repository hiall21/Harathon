from django import forms

from .models import Post, Comment#, Photo

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

# class ImageExampleForm(forms.ModelForm):
#     class Meta:
#         model = Photo
#         fields = ('title', 'content' ,'image',)
