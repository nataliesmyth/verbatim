from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # By default, Django will generate a form dynamically from all fields of the model but we can explicitly define the fields we want the forms to have, which we do below
        fields = ('name', 'email', 'body')