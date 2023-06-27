from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from website.models import Menuitem, Sport


# Create your views here.

def index(request):
    context = {
        'menuitems': Menuitem.objects.filter(is_active=True, is_menu=True)
    }
    return render(request, 'index.html', context)


def sport(request):
    context = {
        'sports': Sport.objects.all(),
        'menuitems': Menuitem.objects.filter(is_active=True, is_menu=True)
    }
    return render(request, 'sport.html', context)


def about(request):
    context = {
        'menuitems': Menuitem.objects.filter(is_active=True, is_menu=True)
    }
    return render(request, 'about.html', context)

# class HomeView(TemplateView):
#     template_name = 'index.html'
# def global_ctx():
#     return {
#         # any other values ...
#         "menuitems": Menuitem.objects.filter(is_active=True, is_menu=True)
#     }
