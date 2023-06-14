from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

from django.contrib.auth.models import User


#______________________________________________________________________________________________________________

class NewsPortal(models.Model):
    objects = None
    sort_date_of_publication = models.DateTimeField(auto_now_add=True)
    article_title = models.CharField(max_length=50, unique=True)   # названия статьи не должны повторяться
    article_author = models.CharField(max_length=50)
    article_description = models.TextField()   # Текст статьи

    news_category = models.ForeignKey(to='NewsCategory', on_delete=models.CASCADE, related_name='news')   # все
    # новости в категории будут доступны через поле news

    def __str__(self):   # отображение описания товара на страничке в интернете
        return f'{self.article_title.title()}: {self.article_description[:500]}: {self.article_author.title()}'

    def get_absolute_url(self):
        return reverse('new_detail', args=[str(self.id)])    # для создания новости и статьи отдельно, с универсальным
        # путем во simpleapp\urls.py
        #return reverse('post/new_detail', args=[str(self.id)])

    def preview(self):
        return self.article_description[0:124] + '...'


class NewsCategory(models.Model):
    # названия категорий тоже не должны повторяться
    objects = None
    article_title = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(User, blank=True, related_name='categories')

    def __str__(self):
        return self.article_title.title()

    # Create your models here.

class NewsPortalCategory(models.Model):
    news_category = models.ForeignKey(NewsPortal, on_delete=models.CASCADE)
    news_portal = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)

class Appointment(models.Model):
    date = models.DateField(
        default=datetime.utcnow,
    )
    client_name = models.CharField(
        max_length=200
    )
    message = models.TextField()

    def __str__(self):
        return f'{self.client_name}: {self.message}'