from django import forms

class TextGenerationForm(forms.Form):
    input_text = forms.CharField(label='Input Text', widget=forms.Textarea(attrs={'class':'text', 'id':'input-text','placeholder':'Input Text', "oninput":'this.style.height = "";this.style.height = this.scrollHeight + "px"'}))
    max_length = forms.IntegerField(label='Max Length', min_value=1, max_value=5000)
