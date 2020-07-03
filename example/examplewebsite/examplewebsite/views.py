from django.shortcuts import render

from keep_sabbath import redirect_if_sabbath


@redirect_if_sabbath
def home_page_view(request):
    context = {}
    return render(request, "home.html", context)






