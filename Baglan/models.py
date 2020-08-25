from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = [
    ['Erkek', "Erkek"],
    ['Aýal', "Aýal"],
]

REL_CHOICES = [
    ['Hiç', "Hiç"],
    ['Ýeke', "Ýeke"],
    ['Gatnaşyklarda', "Gatnaşyklarda"],
    ['Meşgul', "Meşgul"],
    ['Çylşyrymly', "Çylşyrymly"],
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Ulanyjy ady")
    avatar = models.FileField(verbose_name="Awatar", null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name="Öz barada")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name="Şäher")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Doglan guni")
    gender = models.CharField(max_length=10, verbose_name="Jynsy", choices=GENDER_CHOICES, default="male")
    relationship = models.CharField(max_length=20, verbose_name="Gatnaşyklar ýagdaýy", choices=REL_CHOICES, default="none")

    def __str__(self):
        return self.user.username

class Post(models.Model):
    datetime = models.DateTimeField(verbose_name="Sene", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Awtor", related_name="posts")
    text = models.CharField(max_length=1000, verbose_name="Tekst", null=True, blank=True)
    image = models.FileField(verbose_name="Surat", null=True, blank=True)

    def __str__(self):
        return self.author.username
    class Meta:
        ordering = ["-datetime"]

class Comment(models.Model):
    datetime = models.DateTimeField(verbose_name="Sene", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Awtor", related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Post", related_name="comments")
    text = models.CharField(max_length=1000, verbose_name="Tekst", null=True, blank=True)
    def __str__(self):
        return self.author.username
    class Meta:
        ordering = ["datetime"]