from django import forms

from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control shadow-none'}),
            'text': forms.Textarea(attrs={'class': 'form-control shadow-none'}),
        }
        labels = {'text': 'Add your thoughts here'}

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
        # if 'Django' not in title:
        #     raise forms.ValidationError('We only accept notes about Django')
        # return title
