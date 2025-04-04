from django.contrib import admin
from django import forms
from .models import  Country, State, District, Area, SelectList, Company, Branch, Account, Category
from .forms import SelectListForm, CategoryForm


# Register your models here.

    
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'status')
    search_fields = ('name',)
    list_filter = ('status',)
    
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'order', 'status')
    search_fields = ('name', 'country__name')
    list_filter = ('status', 'country')
    
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'order', 'status')
    search_fields = ('name', 'state__name')
    list_filter = ('status', 'state')

class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'order', 'status')
    search_fields = ('name', 'district__name')
    list_filter = ('status', 'district')
    
class SelectListAdmin(admin.ModelAdmin):
    form = SelectListForm
    list_display = ('name', 'value', 'type', 'status', 'display_order')
    
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'active', 'country', 'state', 'district')
    search_fields = ('name', 'email')
    list_filter = ('active', 'country', 'state', 'district')
    
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'location', 'email', 'phone', 'mobile', 'company', 'active')
    search_fields = ('name', 'code', 'email')
    list_filter = ('active', 'company')
    
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_number', 'opening_balance', 'bank_name', 'company', 'branch','active')
    search_fields = ('name', 'account_number', 'bank_name')
    list_filter = ('active', 'company', 'branch')
    
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ('name', 'slug', 'page_layout', 'status')
    search_fields = ('name', 'slug')
    list_filter = ('status',)
    

admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(SelectList, SelectListAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Category, CategoryAdmin)
