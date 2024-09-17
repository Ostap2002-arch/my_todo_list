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


# Create multiple filefield

from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput(attrs={'class': 'form-control'}))
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

class FileFieldForm(forms.Form):
    file_field = MultipleFileField()


# End create multiplr filefield


class FormCreateTask(forms.Form):
    title = forms.CharField(max_length=256,
                            label='Название задачи',
                            widget=forms.TimeInput(attrs={'class': 'form-control'}),
                            )
    description = forms.CharField(max_length=256,
                                  label='Описание',
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'rows' : 'auto'}),
                                  required=False
                                  )

    priority = forms.ModelChoiceField(queryset= Priority.objects.all(),
                                      label='Приоритет',
                                      widget=forms.RadioSelect(attrs={'class':'form-check-input'}),
                                      )
    date_task = forms.DateTimeField(label='Дата события', input_formats=['%H:%M %m/%d/%Y',],  widget=forms.DateTimeInput(
                                                                                     attrs={'id': 'input_task1',
                                                                                            'aria-describedby': 'basic-addon1', },
                                                                                     ),
                                    )
    to_warn = forms.DateTimeField(label='Отправить уведомление', input_formats=['%H:%M %m/%d/%Y',],
                                  widget=forms.DateTimeInput(
                                  attrs={'id': 'input_task2',
                                        'aria-describedby': 'basic-addon2'}),
                                  required=False)

    files  = MultipleFileField(label='Дополнительно',
                               required=False)
