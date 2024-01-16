from django import forms
from .models import Article



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "content")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500 placeholder-gray-400",
                    "placeholder": "Title",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500 placeholder-gray-400",
                    "placeholder": "Content",
                }
            )
        }
