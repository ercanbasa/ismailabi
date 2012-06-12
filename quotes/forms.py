from django import forms
from quotes.models import Quote

class SubmitQuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        exclude = ('is_active', )