from django.contrib import admin
from .models import *


admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Coupon)
admin.site.register(AudioFragments)
admin.site.register(Tag)