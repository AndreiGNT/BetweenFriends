from django import forms
from .models import Comment


class CommentUpdateForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class' : 'form-control w-100', 'id' : 'commentContent', 'cols': 50, 'rows': 25}),
        # help_text=help_texts['any_character'],
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']