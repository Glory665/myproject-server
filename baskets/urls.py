from django.urls import path

from baskets.views import basket_add

app_name = 'baskets'

urlpatterns = [
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
]