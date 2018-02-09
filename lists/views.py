from django.shortcuts import render, redirect
from django.shortcuts import render_to_response

from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists.html', {'items': items})


def new_list(request):
    item_list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=item_list)
    return redirect('/lists/only-list')