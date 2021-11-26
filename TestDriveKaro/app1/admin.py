from django.contrib import admin
from app1.models import Contact, filter_top, filter_luxury,brand_top,brand_luxury
# Register your models here.
admin.site.register(Contact)
admin.site.register(filter_top)
admin.site.register(filter_luxury)
admin.site.register(brand_top)
admin.site.register(brand_luxury)
