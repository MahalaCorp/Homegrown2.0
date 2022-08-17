from django.contrib import admin

from .models import Blog, Talent, TalentImage

# Register your models here.
admin.site.site_header = "Homegrown Talent Admin"
admin.site.title = "Homegrown Talent Admin Area"
admin.site.index_title = "Welcome to Homegrown Talent Admin"


class ImageInline(admin.TabularInline):
    model = TalentImage
    extra = 3


class TalentAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'coverImage', 'height', 'waist',
              'bust', 'shoe', 'dress', 'eye', 'hair')
    list_display = ('name', 'create_at', 'updated_at')
    inlines = [ImageInline]


admin.site.register(Blog)
admin.site.register(Talent, TalentAdmin)
