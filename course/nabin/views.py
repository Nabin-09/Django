from django.shortcuts import render

def all_items(request):
    return render(request , 'nabin/all_nabin.html')