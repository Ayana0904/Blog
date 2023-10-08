from django import forms
from product import models


class CategoryCreate(forms.Form):
    title = forms.CharField(max_length=300)


class ProductsCreate(forms.Form):
    img = forms.ImageField(required=False)
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    rate = forms.FloatField()
    category = forms.ModelChoiceField(queryset=models.Category.objects.all())
    prize = forms.FloatField()
    phone_number = forms.FloatField()


class CommentCreateForm(forms.Form):
    text = forms.CharField(max_length=320)
    name = forms.CharField(max_length=30)
