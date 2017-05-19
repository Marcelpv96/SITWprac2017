from django import forms
from .models import Team,Bet

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


class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ('event', 'description', 'quota', )
        widgets = {
            'description' : forms.TextInput(attrs={
                'class': 'input-sm form-control',
                'placeholder': 'Enter the bet description here...'
            }),
        }

    def save(self, commit=True, request=None, *args, **kwargs):
        instance = super(TeamForm, self).save(commit=False)
        instance.user = request.user
        if commit:
            instance.save()
        return instance