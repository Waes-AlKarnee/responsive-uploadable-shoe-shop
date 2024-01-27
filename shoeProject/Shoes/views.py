from django.shortcuts import redirect, render
from .models import shoe


# Create your views here.

def shoes(request):
    if request.method == "POST":
        userData = request.POST
    
        shoeName = userData.get('name')
        shoePrice = userData.get('price')
        shoeImage = request.FILES.get('Img')
        shoe.objects.create(
            name=shoeName, price=shoePrice, Img=shoeImage
        )

        return redirect('/')
    
    allshoes = shoe.objects.all()
    return render(request, 'home.html', {'shoelist':allshoes})