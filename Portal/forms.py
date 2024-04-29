from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class NewsCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['post_ID','author_ID_FK','category_ID_FK','post_title','post_content','post_rank']

    def clean(self):
        cleaned_data=super().clean()
        post_title=cleaned_data.get("post_title")
        if post_title is not None and len(post_title)<2:
            raise ValidationError({"post_title":"Заголовок не может быть меньше 2 символов"})
            return cleaned_data

        post_content = cleaned_data.get("post_content")
        if post_content is not None and len(post_content) < 2:
            raise ValidationError({"post_content": "Содержание не может быть меньше 2 символов"})
            return cleaned_data


        return cleaned_data


