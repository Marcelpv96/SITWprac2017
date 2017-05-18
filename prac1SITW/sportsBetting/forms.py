from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'short_name', 'crest', )
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': 'input-sm form-control',
                'placeholder': 'Enter the complete name...'
            }),
            'short_name': forms.TextInput(attrs={
                'class': 'input-sm form-control',
                'placeholder': 'This name will be used in creating the name event...'
            }),
        }

    def save(self, commit=True, request=None, *args, **kwargs):
        instance = super(TeamForm, self).save(commit=False)
        instance.created_by = request.user
        if commit:
            instance.save()
        return instance