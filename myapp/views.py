from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# Create your views here.


def get_book(request):
    books = Book.objects.all()
    return render(request, 'get_book.html', {'books':books})

def create_book(request):
    books = Book.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        photo = request.FILES.get('photo')
        video = request.FILES.get('video')
        Book.objects.create(
            title=title,
            quantity=quantity,
            price=price,
            photo=photo,
            video=video
        )
        return redirect('books')
    return render(request, 'create_book.html', {'books':books})


def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.quantity = request.POST.get('quantity')
        book.price = request.POST.get('price')
        if request.FILES.get('photo'):
            book.photo = request.FILES.get('photo')
        if request.FILES.get('video'):
            book.video = request.FILES.get('video')
        book.save()
        return redirect('books')
    return render(request, 'update_book.html', {'book': book})

    
    
    
def delete_book(request,id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books')

