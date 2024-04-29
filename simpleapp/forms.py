from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','description','category','price','quantity']

    def clean(self):
        cleaned_data=super().clean()
        description=cleaned_data.get("description")
        if description is not None and len(description)<20:
            raise ValidationError({"description":"Описание не может быть меньше 20 символов"})
            return cleaned_data

        name=cleaned_data.get("name")
        if name==description:
            raise ValidationError({"name":"Название не должно быть равно описанию"})

        return cleaned_data
