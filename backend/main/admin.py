from django.contrib import admin

from .models import Blog

# Register your models here.
admin.site.site_header = "Homegrown Talent Admin"
admin.site.title = "Homegrown Talent Admin Area"
admin.site.index_title = "Welcome to Homegrown Talent Admin"

admin.site.register(Blog)
