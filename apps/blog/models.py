from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(
        verbose_name='カテゴリ',
        max_length=50,
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        verbose_name='タグ',
        max_length=50,
    )

    def __str__(self):
        return self.name


class Blog(models.Model):
    '''ブログコンテンツ'''
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200,
        blank=False,
        null=False,
        )

    body = models.TextField(
        verbose_name='本文',
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    tag = models.ManyToManyField(
        to=Tag,
        verbose_name='タグ',
        blank=True,
    )

    created_at = models.DateTimeField(
        verbose_name='作成日時',
        default=timezone.now,
    )

    updated_at = models.DateTimeField(
        verbose_name='更新日時',
        default=timezone.now,
    )

    def __str__(self):
        return self.title
