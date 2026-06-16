from django import forms


class NameForm(forms.Form):
    """Форма ввода имени пользователя с обязательным заполнением."""

    name = forms.CharField(
        max_length=100,
        required=True,
        error_messages={
            'required': 'Пожалуйста, введите имя.',
        },
        widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
    )

    def clean_name(self):
        """Дополнительная проверка: имя не должно состоять из пробелов."""
        name = self.cleaned_data['name'].strip()
        if not name:
            raise forms.ValidationError('Имя не может быть пустым.')
        return name
