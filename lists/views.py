from django.shortcuts import render, redirect
from django.shortcuts import render_to_response

from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    item_list = List.objects.get(id=list_id)
    items = Item.objects.filter(list=item_list)
    return render(request, 'lists.html', {'list': item_list})


def add_item(request, list_id):
    item_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=item_list)
    return redirect('/lists/{}'.format(item_list.id))


def new_list(request):
    item_list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=item_list)
    return redirect('/lists/{}'.format(item_list.id))