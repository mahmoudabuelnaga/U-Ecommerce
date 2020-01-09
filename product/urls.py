from django.urls import path
from .views import ProductListView, ProductDetailView, product_list_view, product_detail_view

app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view()),
    path('fbv/', product_list_view),

    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('fbv/<int:pk>/', product_detail_view),
]
