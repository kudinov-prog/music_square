from django import forms
from .models import Genre, Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['genre', 'text', 'image', 'content']
        labels = {
            'genre': 'Группа',
            'text': 'Текст',
            'image': 'Картинка',
            'content': 'Аудиотрек'
            }
        help_texts = {
            'genre': 'Если знаете тематику, то выберите группу!',
            'text': 'Постарайтесь выкладывать годный контент!',
            'image': 'Выберите картинку!',
            'content': 'Выберите годную музыку!'
            }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Текст'}
        help_texts = {'text': 'Введите комментарий!'}
