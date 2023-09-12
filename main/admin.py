from django.contrib import admin
from main.models import Item
# Register your models here.

item_data_list = {
    'name': 'Beef Noodle',
    'amount' : 8,
    'description': 'Mie rasa daging',
    },
{
    'name': 'Chicken Rice',
    'amount': 12,
    'description': 'Nasi dengan ayam',
},
{
    'name': 'Chitatoo',
    'amount': 26,
    'description': 'Crispy potato chips',
},

# Buat dan simpan semua objek Item
for item_data in item_data_list:
    item = Item(**item_data)
    item.save()
