from django.shortcuts import render


def journey(request):
    return render(request, "weightloss/journey.html")