from django.shortcuts import render
from transformers import pipeline
from .forms import TextGenerationForm  # Import the form from the forms.py file of your app


def generate_text(request):
    if request.method == 'POST':
        form = TextGenerationForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            max_length = form.cleaned_data['max_length']

            generator = pipeline("text-generation", model='distilgpt2')
            res = generator(input_text, max_length=max_length, num_return_sequences=1)

            context = {
                'form': form,
                'output_text': res[0]['generated_text'],
            }
            return render(request, 'text_generation_app/generate_text.html', context)
    else:
        form = TextGenerationForm()

    context = {
        'form': form,
        'output_text': None,
    }
    return render(request, 'text_generation_app/generate_text.html', context)
