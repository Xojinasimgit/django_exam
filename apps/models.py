from django.contrib.auth.models import AbstractUser
from django.db.models import TextField, CharField, EmailField, ImageField, Model, IntegerField, ForeignKey, CASCADE, \
    DateTimeField, TextChoices


# Create your models here.

class User(AbstractUser):
    images = ImageField(upload_to='pic/', blank=True, null=True)
    full_name = CharField(max_length=255, blank=True, null=True)
    about = TextField(null=True, blank=True)
    phone = CharField(max_length=255, blank=True, null=True)
    email = EmailField()
    instagram = CharField(max_length=255, blank=True, null=True)
    linkedin = CharField(max_length=255, blank=True, null=True)


class Category(Model):
    name = CharField(max_length=255)
    images = ImageField(upload_to='img/', blank=True, null=True)
    location = CharField(max_length=255)
    area = CharField(max_length=20)
    room = IntegerField()
    floor = IntegerField()
    price = IntegerField()
    property_Type = CharField(max_length=200)
    property_description = TextField()
    status = CharField(max_length=200)
    beds = IntegerField()
    baths = IntegerField()
    garages = IntegerField()
    author = ForeignKey('apps.User', CASCADE, related_name='my_category')
    created_at = DateTimeField(auto_now_add=True)


class Blog(Model):
    class Status(TextChoices):
        TRAVEL = 'Travel', 'Travel'
        DISCOUNT = 'Discount', 'Discount'
        NEWS = 'News', 'News'

    image = ImageField(upload_to='jpg/', blank=True, null=True)
    title = CharField(max_length=200)
    category = CharField(max_length=50, choices=Status.choices, default=Status.TRAVEL)
    about = TextField()
    author = ForeignKey('apps.User', on_delete=CASCADE, related_name='add_blog')
    created_at = DateTimeField(auto_now_add=True)


class Comment(Model):
    fill_name = CharField(max_length=255)
    email = EmailField()
    text = TextField()
    to_blog = ForeignKey('apps.Blog', CASCADE, related_name='my_command')
    created_at = DateTimeField(auto_now_add=True)


class Send_email(Model):
    name = CharField(max_length=200)
    email = EmailField()
    subject = CharField(max_length=200)
    text = TextField()
    created_at = DateTimeField(auto_now_add=True)
