from django import forms
class Student(forms.Form):
    name=forms.CharField(help_text='only 10 characters')
    password=forms.CharField(widget=forms.PasswordInput())
    email=forms.EmailField()
    contact=forms.IntegerField()
    checkbox=forms.CharField()
