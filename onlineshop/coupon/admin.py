from django.contrib import admin
from .models import Coupon


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'use_form', 'use_to', 'amount', 'active']
    list_filter = ['active', 'use_form', 'use_to']
    search_fields = ['code']


admin.site.register(Coupon, CouponAdmin)