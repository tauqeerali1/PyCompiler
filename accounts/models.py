from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Posts(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


class Exam(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)
    