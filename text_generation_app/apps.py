from django.apps import AppConfig
from transformers import pipeline, AutoTokenizer
from .forms import TextGenerationForm  # Import the form from the forms.py file of your app
import torch

class TextGenerationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'text_generation_app'
    # model = "Mukesh555/Llama-2-7b-indian_lawyer_chat-finetune"
    # tokenizer = AutoTokenizer.from_pretrained(model)
    # generator = pipeline("text-generation", model=model, torch_dtype=torch.float16, device_map="auto", offload_folder="offload")
