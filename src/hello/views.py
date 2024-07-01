from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'hello.html')


@login_required
def required(request):
    useremail = None
    if request.user.is_authenticated:
        useremail = request.user.email
    return HttpResponse("Hello, {}.".format(useremail))
