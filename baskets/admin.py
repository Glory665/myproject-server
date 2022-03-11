from django.contrib import admin

from baskets.models import Basket


class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = readonly_fields = ('product', 'quantity', 'created_timestamp')
    extra = 0
