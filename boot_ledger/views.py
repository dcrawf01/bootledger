# Create your views here.

from django.http import HttpResponse
from boot_ledger.models import Item
from django.views.generic import ListView


def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")