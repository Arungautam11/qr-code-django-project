from django import forms


class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        max_length=50,
        label='QR Code Name :',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter QR code name'
        })
        )
    url = forms.URLField(
        max_length=200, 
        label='QR Code URL :',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the URL'
        })
        )