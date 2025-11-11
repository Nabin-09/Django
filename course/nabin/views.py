from django.shortcuts import render

def all_items(request):
    return render(request , 'nabin/all_nabin.html')

def all_order(request):
    return render(request , 'nabin/all_orders.html')