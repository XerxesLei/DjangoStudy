from django.http import HttpResponse

from django.shortcuts import render

def hello(request):
    return HttpResponse("hello world!")


def runa (request):
    context = {}
    context['hello'] = "hello world!"
    context['runa']  = 'hello diango'
    view_list = ["hello1", 'hell', 'hello3']
    context['view_list'] = view_list
    return render(request, 'runa.html',context)

def test(request) :
    context = {}
    context['hello'] = 'hello'
    return render(request, 'test.html',context)