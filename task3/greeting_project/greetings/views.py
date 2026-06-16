from django.shortcuts import render

from .forms import NameForm
from .models import Greeting


def index(request):
    """
    Обрабатывает форму ввода имени: сохраняет имя в базе данных
    и отображает персонализированное приветствие на главной странице.
    """
    greeting_name = None

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Greeting.objects.create(name=name)
            greeting_name = name
            # Очищаем форму после успешной отправки
            form = NameForm()
    else:
        form = NameForm()

    context = {
        'form': form,
        'greeting_name': greeting_name,
    }
    return render(request, 'greetings/index.html', context)
