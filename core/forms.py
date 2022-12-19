from django import forms 
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone', 'subject', 'message']
      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)

        for field in self.fields:
            new_class ={
                'class': 'form-control col-6',
                'placeholder': f'Recipe your {self.fields[str(field)].label}'
            }
            self.fields[str(field)].widget.attrs.update(
                new_class
            )
