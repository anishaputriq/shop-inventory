from django.shortcuts import render

# Create your views here.
def show_main(request):
    items = [
        {
            'name': 'Beef Noodle :)',
            'amount': 8,
            'description': 'Mie rasa daging',
        },
        {
            'name': 'Chicken Rice >_<',
            'amount': 12,
            'description': 'Nasi dengan ayam',
        },
        {
            'name': 'Chitatoo ;)',
            'amount': 26,
            'description': 'Crispy potato chips',
        },
    ]

    context = {
        'items': items,
    }

    return render(request, "main.html", context)