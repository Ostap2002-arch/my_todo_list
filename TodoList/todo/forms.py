from django import forms

from .models import Color


class FormCreateCategories(forms.Form):
    title = forms.CharField(max_length=256,
                            label='Новая категория',
                            widget=forms.TextInput(attrs={'class':'col-6 form-control mx-2'}))
    color = forms.ModelChoiceField(queryset=Color.objects.all(),
                                   label='Цвет',
                                   widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    push = forms.BooleanField(
        label='Уведомления по умолчанию',
        widget=forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
        required=False
    )



# attrs={'class': 'form-check-input color1'}