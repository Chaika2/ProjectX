from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def actual(request):
    return render(request, "main/actual.html")


def geo(request):
    return render(request, "main/geo.html")

def last(request):
    return render(request, "main/last.html")


def skills(request):
    return render(request, "main/skills.html")
