import re
from django import forms
from django.core.exceptions import ValidationError
from .models import *

class SalonForm(forms.ModelForm):
    class Meta:
        model=Avtosalon
        fields=['title','context','email','phone','address']
        widgets={
            'title':forms.TextInput(attrs={"class": "form-control"}),
            'context':forms.Textarea(attrs={"class":"form-control",'rows':5}),
            'email':forms.TextInput(attrs={"class": "form-control"}),
            'phone':forms.NumberInput(attrs={"class":"form-control"}),
            'address':forms.TextInput(attrs={"class": "form-control"})
        }
    def clean_title(self):
        title=self.cleaned_data['title']

        if re.match(r'\d',title):
            raise ValidationError("Title raqam bo'lsin")
        return title

    def clean_email(self):
        email=self.cleaned_data['email']
        if not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
            raise ValidationError("Email noto'g'ri formatda.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        pattern = re.compile(r'^\+?\d{9,15}$')
        if not pattern.match(str(phone)):
            raise ValidationError("Telefon raqami noto'g'ri formatda.")
        return phone



class BrandForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields=['title','context']
        widgets={
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'context': forms.Textarea(attrs={"class": "form-control", 'rows': 5})
        }
    def clean_title(self):
        title=self.cleaned_data['title']

        if re.match(r'\d',title):
            raise ValidationError("Title raqam bo'lsin")
        return title



class CarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields='__all__'
        widgets={
            'salon_id':forms.Select(attrs={"class": "form-control"}),
            'brand_id':forms.Select(attrs={"class": "form-control"}),
            'model':forms.TextInput(attrs={"class": "form-control"}),
            'price':forms.NumberInput(attrs={"class":"form-control"}),
            'year':forms.DateTimeInput(attrs={
                "class": "form-control",
                "type": "datetime-local"
            }),
            'color':forms.TextInput(attrs={"class": "form-control"})
        }