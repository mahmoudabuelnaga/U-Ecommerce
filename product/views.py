from django.shortcuts import render, get_object_or_404
from .models import Product, Color
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.utils.translation import ugettext
from django.utils import translation
from django.http import HttpResponseRedirect
from django.conf import settings
from carts.models import Cart


# Create your views here.
class ProductListView(ListView):
    # queryset = Product.objects.all()
    
    template_name=  'products/list.html'
    context_object_name= 'products'
    def get_queryset(self, *args, **kwargs):
        request = self.request
        
        return Product.objects.all()



    # def get_context_data(self,*args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     return context

def product_list_view(request):
    # print(request.session.get("first_name" , "UnKnown"))
    # print(request.session.get("last_name" , "UnKnown"))
    queryset = Product.objects.all()
    context = {
        'products':queryset,
    }
    return render(request, 'products/list.html', context)

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name=  'products/detail.html'
    # context_object_name = 'product'
    def get_context_data(self,*args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

def product_detail_view(request, pk=None, *args, **kwargs):
    queryset = Product.objects.get_by_id(pk)
    if queryset is None:
        raise Http404("product doesn't exist")
    # queryset = get_object_or_404(Product, pk=pk)
    # try:
    #     queryset = Product.objects.get(pk=pk)
    # except Product.DoesNotExcept:
    #     raise Http404("errors")
    context = {
        'product':queryset,
    }
    return render(request, 'products/detail.html', context)

def color_product(request):
    color = Color.objects.all()
    return render(request, "color.html", {"color":color,})


def change_language(request):
    current_language = translation.get_language()
    if current_language == 'ar':
        lang_code = 'en'
    else:
        lang_code = 'ar'
    
    response = HttpResponseRedirect(request.GET.get('retuen_url'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    translation.activate(lang_code)
    return response