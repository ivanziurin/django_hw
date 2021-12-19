from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_sort = request.GET.get('sort', 'name')
    if phone_sort == 'min_price':
        phone_sort = 'price'
    elif phone_sort == 'max_price':
        phone_sort = '-price'
    else:
        phone_sort = 'name'
    phone_objects = Phone.objects.order_by(phone_sort)
    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    post = get_object_or_404(Phone, slug=slug)
    context = {'phone': post}
    return render(request, template, context)


def db_delete(request):
    Phone.objects.all().delete()
    return HttpResponse('База данных очищена')