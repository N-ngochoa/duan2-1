from django.contrib import admin
from .models import nguoi_dung,to_do_list,item,to_do_share

admin.site.register(to_do_list)
admin.site.register(nguoi_dung)
admin.site.register(item)
admin.site.register(to_do_share)