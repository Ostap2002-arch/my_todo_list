from django import forms

from .models import Color, Works


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

class FormCreateTask(forms.Form):
    title = forms.CharField(max_length=256,
                            label='Название задачи',
                            widget=forms.TimeInput(attrs={'class':'form-control'})
                            )
    description = forms.CharField(max_length=256,
                            label='Описание',
                            widget=forms.Textarea(attrs={'class':'form-control'})
                                  )

    # priority = forms.ModelChoiceField(queryset= Works.PRIORITY,
    #                                label='Приоритет',
    #                                widget=forms.RadioSelect()
    #                                   )
    date_task = forms.DateTimeField(label='Дата события', widget=forms.DateInput(format='%Y-%m-%d'),
                                    input_formats=('%Y-%m-%d',),
                                    required=False,
                                    )
    to_warn = forms.DateTimeField(label='Отправить уведомление за', widget=forms.TimeInput())
    files = forms.FileField(label='Дополнительный материал',
                            widget=forms.FileInput(attrs={'class' : 'form-control', 'type':'file'}))




# attrs={'class': 'form-check-input color1'}