from django.shortcuts import render
from .forms import PasswordGeneratorForm
from .models import GeneratedPassword
import random
import string

def password_generator(request):
    if request.method == 'POST':
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            use_lowercase = form.cleaned_data['use_lowercase']
            use_uppercase = form.cleaned_data['use_uppercase']
            use_digits = form.cleaned_data['use_digits']
            use_special_chars = form.cleaned_data['use_special_chars']
            characters = ''

            if use_lowercase:
                characters += string.ascii_lowercase
            if use_uppercase:
                characters += string.ascii_uppercase
            if use_digits:
                characters += string.digits
            if use_special_chars:
                characters += string.punctuation

            generated_password = ''.join(random.choice(characters) for _ in range(length))
            GeneratedPassword.objects.create(generated_password=generated_password)

            # Get the most recent generated password
            recent_password = GeneratedPassword.objects.latest('timestamp')

    else:
        form = PasswordGeneratorForm()
        recent_password = None

    return render(request, 'password_generator/password_generator.html', {'form': form, 'recent_password': recent_password})
