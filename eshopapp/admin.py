from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from eshopapp.models import Category, Brand, Product

# Register your models here.
class SlugAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title',) 

class NewsAdmin(SummernoteModelAdmin, SlugAdmin):
	summer_note_fields = ('text', 'text_min')


admin.site.register(Category, NewsAdmin)
admin.site.register(Brand, NewsAdmin)
admin.site.register(Product, NewsAdmin)