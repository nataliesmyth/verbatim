from django import forms
from .models import Comment, Image


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # By default, Django will generate a form dynamically from all fields of the model but we can explicitly define the fields we want the forms to have, which we do below
        fields = ('name', 'email', 'body')

# This will generate a form with title and image fields, which will then be rendered in the templates
class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')