from django import forms
from .models import *


class TeamForm(forms.ModelForm):
    crest = forms.ImageField(required=False)
    class Meta:
        model = Team
        fields = ('name', 'short_name', 'crest', )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input-sm form-control',
                'placeholder': 'Enter the complete name...'
            }),
            'short_name': forms.TextInput(attrs={
                'class': 'input-sm form-control',
                'placeholder': 'This name will be used in creating the name event...'
            }),
        }


class CompetitionForm(forms.ModelForm):
    logo = forms.ImageField(required=False)
    class Meta:
        model = Competition
        exclude = ('user', )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input-sm form-control',
                'placeholder': 'Enter the complete name...'
            }),
            'short_name': forms.TextInput(attrs={
                'class': 'input-sm form-control',
                'placeholder': 'This name will be used in creating the name event...'
            }),
            'teams': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'size': '10',
            }),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('user', )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input-sm form-control',
                'placeholder': 'Enter the complete name...'
            }),
        }


class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ('event', 'description', 'quota', )
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'input-sm form-control',
                'placeholder': 'Enter the bet description here...'
            }),
        }
