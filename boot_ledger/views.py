# Create your views here.

from django.http import HttpResponse
from boot_ledger.models import Item
from django.views.generic import ListView

class ListItemView(ListView):

	model = Item
	template_name = 'items_list.html'
