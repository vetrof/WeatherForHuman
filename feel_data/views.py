from django.contrib import messages
from django.shortcuts import render, redirect

from feel_data.save_feel_data import save_feel
from django.contrib.auth.decorators import login_required


@login_required
def save_feel_data(request):

    feel_num = request.GET.get('feel_num')
    feel_info = request.GET.get('feel_info')

    if feel_num:
        save_feel(request, feel_num, feel_info)
        messages.success(request, 'Спасибо, данные записаны!')

    else:
        messages.success(request, 'Данные не записаны. Нужно выбрать самочувствие.')

    return redirect(request.META.get('HTTP_REFERER'))
