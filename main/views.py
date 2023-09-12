from django.shortcuts import render
from .models import Item

# Create your views here.
def show_main(request):
    items = Item.objects.all()  # Mengambil semua objek Item dari basis data
    context = {
        'items': items,
    }

    return render(request, "main.html", context)