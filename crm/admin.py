from django.contrib import admin
from .models import Company, Contact, Deal, Activity, Task


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0


class DealInline(admin.TabularInline):
    model = Deal
    extra = 0


class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 0

class TaskInline(admin.TabularInline):
    model = Task
    extra = 0

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'segment', 'city', 'created_at', 'view_contacts', 'view_deals')
    search_fields = ('name', 'cnpj', 'email')
    list_filter = ('segment', 'city', 'state')
    inlines = [ContactInline, DealInline, ActivityInline, TaskInline]

    def view_contacts(self, obj):
        return f"{obj.contact_set.count()} contatos"
    view_contacts.short_description = "Contatos"

    def view_deals(self, obj):
        return f"{obj.deal_set.count()} oportunidades"
    view_deals.short_description = "Oportunidades"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('company',)


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'value', 'stage', 'status', 'expected_close_date', 'created_at')
    search_fields = ('title',)
    list_filter = ('stage', 'status', 'company')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'company', 'contact', 'deal', 'activity_date', 'created_at')
    search_fields = ('description',)
    list_filter = ('activity_type', 'company')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'contact', 'deal', 'due_date', 'status', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'company')