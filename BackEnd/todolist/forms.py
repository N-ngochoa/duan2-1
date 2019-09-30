from django import forms
from .models import to_do_list, item

class to_do_form(forms.Form):
    name_todo = forms.CharField(label='Tên to do list', max_length=30)
    is_public = forms.BooleanField(label="public cho mọi người xem")

    def add(self):
        name = self.cleaned_data['name_todo']
        is_public = self.cleaned_data['is_public']
        to_do_list.objects.create(name=name, is_public=is_public)

    def update(self):
        name = self.cleaned_data['name_todo']
        is_public = self.cleaned_data['is_public']
        to_do_list.objects.filter(name=name)


class item_form(forms.Form, ):
    name_item = forms.CharField(label='Tên to do list', max_length=30)
    ispublic = forms.BooleanField(label="public cho mọi người xem")

    def add(self):
        name = self.cleaned_data['name']
        is_public = self.cleaned_data['ispublic']
        item.objects.create(name=name)
