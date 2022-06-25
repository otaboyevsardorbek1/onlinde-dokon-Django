from django.shortcuts import render

def home_page_view(request):
    return render(request, 'store/index.html')

def shopping_page_view(request):
    return render(request, "store/shop.html")
