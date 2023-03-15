from django import forms
from .models import Item


class ItemForm(form.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']
