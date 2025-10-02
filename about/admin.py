from django.contrib import admin
from .models import About, Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('message', 'name','read',)
    list_filter = ('name',)
    