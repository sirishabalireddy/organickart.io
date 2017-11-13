from django.shortcuts import render
from django.contrib.auth import authenticate, login
from food_carts.models import Product
from orders.models import Order, OrderItem

from .form import login_M

# Create your views here.

def Login(request):
    if request.method == 'POST':
        form = login_M(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username= cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)

                    orders = Order.objects.all()
                    orderitems = OrderItem.objects.all()

                    return render(request, 'manager/panel.html', {'orders': orders, 'orderitems': orderitems})

                else:
                    error = 'Account Disabled'
                    return render(request, 'manager/Error.html', {'error': error})

            else:
                form = login_M()
                return render(request, 'manager/login.html', {'form': form})

    else:
        form = login_M()
        return render(request, 'manager/login.html', {'form':form})