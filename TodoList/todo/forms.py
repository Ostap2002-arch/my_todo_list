from django import forms

from .models import Color, Works, Priority


class FormCreateCategories(forms.Form):
    title = forms.CharField(max_length=256,
                            label='Новая категория',
                            widget=forms.TextInput(attrs={'class': 'col-6 form-control mx-2'}))
    color = forms.ModelChoiceField(queryset=Color.objects.all(),
                                   label='Цвет',
                                   widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    push = forms.BooleanField(
        label='Уведомления по умолчанию',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        required=False
    )


class FormCreateTask(forms.Form):
    title = forms.CharField(max_length=256,
                            label='Название задачи',
                            widget=forms.TimeInput(attrs={'class': 'form-control'})
                            )
    description = forms.CharField(max_length=256,
                                  label='Описание',
                                  widget=forms.Textarea(attrs={'class': 'form-control'})
                                  )

    priority = forms.ModelChoiceField(queryset= Priority.objects.all(),
                                      label='Приоритет',
                                      widget=forms.RadioSelect(),
                                      )
    date_task = forms.DateTimeField(label='Дата события', widget=forms.DateTimeInput(format='%H:%M %m/%d/%Y',
                                                                                     attrs={'id': 'input_task1',
                                                                                            'aria-describedby': 'basic-addon1', },
                                                                                     ),
                                    )
    to_warn = forms.DateTimeField(label='Отправить уведомление', widget=forms.DateTimeInput(format='%H:%M %m/%d/%Y',
                                                                                            attrs={'id': 'input_task2',
                                                                                                   'aria-describedby': 'basic-addon2'}))

    files = forms.FileField(label='Дополнительный материал',
                            widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}))

# attrs={'class': 'form-check-input color1'}
