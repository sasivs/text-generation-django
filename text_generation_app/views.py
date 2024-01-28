from django.shortcuts import render
from transformers import pipeline, AutoTokenizer
from .forms import TextGenerationForm  # Import the form from the forms.py file of your app
import torch
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def generate_text(request):
    if request.method == 'POST':
        form = TextGenerationForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            max_length = form.cleaned_data['max_length']
            model = "Mukesh555/Llama-2-7b-indian_lawyer_chat-finetune"
            if not request.session.get('tokenizer'):
                tokenizer = AutoTokenizer.from_pretrained(model)
                request.session['tokenizer'] = tokenizer
            else:
                tokenizer = request.session.get('tokenizer')
            if not request.session.get('generator'):
                generator = pipeline("text-generation", model=model, torch_dtype=torch.float16, device_map="auto")
                request.session['generator'] = generator
            else:
                generator = request.session.get('generator')
            res = generator(f'[INST] {input_text} [/INST]', max_length=max_length, num_return_sequences=1, do_sample=True, top_k=10,eos_token_id=tokenizer.eos_token_id,)

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
