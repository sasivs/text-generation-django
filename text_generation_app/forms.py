from django import forms

class TextGenerationForm(forms.Form):
    input_text = forms.CharField(label='Input Text', widget=forms.Textarea)
    max_length = forms.IntegerField(label='Max Length', min_value=1, max_value=100)
