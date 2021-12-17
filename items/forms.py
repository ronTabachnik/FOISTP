from django import forms


class ReviewForm(forms.Form):
    grade = forms.DecimalField(
        max_value=5,
        min_value=0,
        decimal_places=1,
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        )
    )
    text = forms.CharField(
        label='Description',
        max_length=500,
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        )
    )
