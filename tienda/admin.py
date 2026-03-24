from django.contrib import admin
from .models import Category, Product, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} 
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'created']
    list_filter = ['created', 'category']
    list_editable = ['price', 'stock']
    prepopulated_fields = {'slug': ('name',)}


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'paid', 'created']
    list_filter = ['paid', 'created']
    inlines = [OrderItemInline] 