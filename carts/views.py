from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from product.models import Product
from orders.models import Order
from accounts.forms import RegisterForm
from billing.models import BillingProfile

# Create your views here.
# def cart_creater(user=None):
#     cart_obj = Cart.objects.create(user=None)
#     print("Create New Cart")
#     return cart_obj

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # products = cart_obj.products.all()
    # total = 0
    # for x in products:
    #     total += x.price
    # cart_obj.total = total
    # cart_obj.save()
    return render(request, 'cart.html',{"cart":cart_obj})

def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return redirect("cart:cart_home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items'] = cart_obj.products.count()
    
    return redirect("cart:cart_home")

def checkout_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    order_obj = None
    if new_obj or Cart.objects.count() == 0:
        return redirect("cart:cart_home")
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    
    user = request.user
    billing_profile = None
    if user.is_authenticated:
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(
            user=user, email=user.email
        )
    context = {
        "object":order_obj,
        "billing_profile":billing_profile,
    }
    return render(request, 'checkout.html', context)