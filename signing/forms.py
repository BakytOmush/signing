from django import forms
from .models import SignedDocument

class DocumentForm(forms.ModelForm):
    class Meta:
        model = SignedDocument
        fields = ['document']