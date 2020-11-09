from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Genre(models.Model):

    title = models.CharField("Название", max_length=200)
    slug = models.SlugField("Путь", unique=True)
    description = models.TextField("Описание")

    def __str__(self):
        return self.title 


class Post(models.Model):

    text = models.TextField("Комментарий к треку")
    pub_date = models.DateTimeField("Дата публикации",
                                    auto_now_add=True, db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Автор")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, blank=True,
                              null=True, related_name="posts",
                              verbose_name="Жанр")
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    content = models.FileField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-pub_date"]


class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments",
                             verbose_name="Пост")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Автор комментария") 
    text = models.TextField("Текст комментария")
    created = models.DateTimeField("Время публикации", auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-created"]


class Follow(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="follower")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="following")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_follow')
        ]
