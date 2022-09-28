from django import forms
from trans.models import ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = ticket
        fields = ['category','nickname','nickname2','chip_count', 'transfered_chip_count']

class StatusForm(forms.ModelForm):
    class Meta:
        model = ticket
        fields = ['approve','decline' ]

