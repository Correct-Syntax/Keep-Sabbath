from django.shortcuts import render
from django.conf import settings 


def keep_sabbath_page_view(request):
    try:
        return render(request, settings.SABBATH_REDIRECT_TEMPLATE, {})
    except:
        raise ValueError(
            'You have not set the SABBATH_REDIRECT_TEMPLATE in your settings.py'
            )

