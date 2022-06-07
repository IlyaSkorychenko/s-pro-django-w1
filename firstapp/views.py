from datetime import date

from django.http import HttpResponse, HttpResponseNotFound

from firstapp.enums import DateUnit


def hellodjango(request):
    return HttpResponse('Hello Django!')


def hello_name(request, name: str):
    return HttpResponse(f'Hello {name}!')


def get_date(request):
    current_date = date.today()

    return HttpResponse(current_date.strftime('%d.%m.%y'))


def get_date_info(request, unit: str):
    current_date = date.today()

    match unit:
        case DateUnit.year.value:
            date_info = current_date.year
        case DateUnit.month.value:
            date_info = f'{current_date.month:02d}'
        case DateUnit.day.value:
            date_info = f'{current_date.day:02d}'
        case _:
            return HttpResponseNotFound(
                f'Unexpected date unit: {unit}. Expected: {[e.value for e in DateUnit]}'
            )

    return HttpResponse(date_info)
