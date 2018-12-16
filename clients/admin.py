from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Client


class ClientModel(admin.ModelAdmin):
    list_display = (
        'ordering',
        'business',
        'contact_person',
        'status',
        'project_type',
        'total_amount',
    )
    list_filter = (
        'joined',
        'status',
        'project_type',
        'technology_stack',
    )
    list_display_links = ('business', )
    list_editable = (
        'ordering',
        'status',
    )
    search_fields = ('business', 'contact_person', 'status', 'project_type',
                     'technology_stack', 'total_amount')
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={
                'rows': 4,
                'cols': 100
            })
        }
    }

    fieldsets = (
        ('CLIENT INFO', {
            'fields': ('business', 'contact_person', 'phone', 'email')
        }),
        ('PROJECT DETAILS', {
            'fields': ('status', 'project_type', 'technology_stack',
                       'description')
        }),
        ('DEVELOPMENT DETAILS', {
            'fields': ('pivotal_tracker', 'repositories', 'dev_team',
                       'project_docs')
        }),
        ('PAYMENTS', {
            'fields': ('total_amount', 'amount_paid', 'amount_due')
        }),
        ('CASH UTILISATION', {
            'fields': ('expenditure', 'profit')
        }),
        ('TIMELINES', {
            'fields':
            ('expected_start_date', 'expected_duration', 'expected_end_date',
             'actual_start_date', 'actual_end_date', 'actual_duration')
        }),
        ('DEPLOYMENT', {
            'fields': ('product_urls', )
        }),
        ('OUR FEEDBACK', {
            'fields': ('project_complexity', 'rate_client', 'comments')
        }),
        ('CLIENT FEEDBACK', {
            'fields': ('rating', 'feedback')
        }),
    )


admin.site.register(Client, ClientModel)
