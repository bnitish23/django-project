from django import forms
from testapp.models import login

class loginForm(forms.ModelForm):
        
    class Meta:
            model = login
            fields = '__all__'
    