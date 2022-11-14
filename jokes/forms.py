from django.forms import ModelForm, Textarea

from .models import Joke

class JokeForm(ModelForm):
    # This is a model form, but I don't want it in models.py
    class Meta:
        model = Joke
        fields = ['question', 'answer', 'category']
        widgets = {
            'question': Textarea(
                attrs={'cols': 80, 'rows': 3, 'autofocus': True}
            ),
            'answer': Textarea(
                attrs={'cols': 80, 'rows': 2, 'placeholder': 'Make it funny!'}
            )
        }
        help_texts = {
            'question': 'No dirty jokes please.'
        }