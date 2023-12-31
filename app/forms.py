from django import forms


class bookingForms(forms.Form):
    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    seats = forms.CharField(label='Seats',widget=forms.TextInput(attrs={'class':'form-control'}))
    fare = forms.CharField(label="Price",widget=forms.TextInput(attrs={'class':'form-control','disabled': 'disabled'}))