from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo_id = models.AutoField
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=50)
    main = models.BooleanField(blank=True, default=False)
    project_name = models.CharField(max_length=50)
    images = models.ImageField(upload_to="Studio/images")

    def __str__(self):
        template = '{0.project_name}, {0.title}'
        return template.format(self)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
