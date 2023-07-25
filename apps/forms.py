from django.contrib.auth.hashers import make_password
from django.forms import ModelForm
from django.template.base import COMMENT_TAG_END

from apps.models import User, Category, Blog, Comment, Send_email


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'linkedin', 'instagram', 'images', 'about', 'phone', 'full_name', 'email', 'password']

    def clean_password(self):
        return make_password(self.cleaned_data['password'])


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'images', 'location', 'area', 'room', 'floor', 'price', 'property_Type',
                  'property_description', 'status', 'beds', 'baths', 'garages', 'author']


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ('created_at',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('fill_name', 'email', 'text')


class EmailForm(ModelForm):
    class Meta:
        model = Send_email
        fields = ('name', 'email', 'subject', 'text')
