from django.contrib import admin
from .models import (
    Category, Collection, Product, FlagshipLounge,
    ConsultationBooking, BespokeInquiry, JournalArticle, PressQuote
)

admin.site.site_header = "Aether Jewels • Celestial Atelier Control Suite"
admin.site.site_title = "Aether Jewels Admin"
admin.site.index_title = "Celestial High Jewellery Management"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'display_order', 'is_featured')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('display_order', 'is_featured')


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'subtitle', 'is_featured', 'is_active', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_featured', 'is_active')
    search_fields = ('name', 'subtitle', 'curator_note')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'sku', 'category', 'collection', 'formatted_price_inr', 'carat_weight', 'is_masterpiece', 'is_featured', 'in_stock')
    list_filter = ('category', 'collection', 'metal_type', 'is_masterpiece', 'is_featured', 'in_stock')
    search_fields = ('title', 'sku', 'subtitle', 'primary_gemstone', 'gemstone_origin')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_masterpiece', 'is_featured', 'in_stock')
    fieldsets = (
        ('General Identity', {
            'fields': ('title', 'slug', 'sku', 'subtitle', 'category', 'collection')
        }),
        ('Valuation & Stock', {
            'fields': ('price_inr', 'is_price_on_request', 'in_stock', 'stock_count')
        }),
        ('Gemstone & Gemological Specs', {
            'fields': ('primary_gemstone', 'gemstone_origin', 'carat_weight', 'clarity_cut', 'metal_type', 'metal_description', 'dimensions', 'certification')
        }),
        ('Celestial Narrative & Craftsmanship', {
            'fields': ('description', 'craftsmanship_story')
        }),
        ('Visual Assets', {
            'fields': ('image_primary', 'image_secondary', 'image_detail', 'image_editorial')
        }),
        ('Flagship Curation', {
            'fields': ('is_featured', 'is_masterpiece')
        }),
    )


@admin.register(FlagshipLounge)
class FlagshipLoungeAdmin(admin.ModelAdmin):
    list_display = ('lounge_name', 'city', 'phone', 'email', 'is_active', 'display_order')
    list_editable = ('is_active', 'display_order')


@admin.register(ConsultationBooking)
class ConsultationBookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'full_name', 'phone', 'city_lounge', 'preferred_date', 'preferred_time', 'jewellery_interest', 'status', 'created_at')
    list_filter = ('status', 'city_lounge', 'jewellery_interest')
    search_fields = ('booking_id', 'full_name', 'email', 'phone')
    list_editable = ('status',)


@admin.register(BespokeInquiry)
class BespokeInquiryAdmin(admin.ModelAdmin):
    list_display = ('inquiry_id', 'client_name', 'phone', 'piece_type', 'gemstone', 'metal', 'carat_weight', 'estimated_price_inr', 'created_at')
    list_filter = ('piece_type', 'gemstone', 'metal')
    search_fields = ('inquiry_id', 'client_name', 'email', 'phone')


@admin.register(JournalArticle)
class JournalArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'read_time', 'published_date', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'snippet', 'content')


@admin.register(PressQuote)
class PressQuoteAdmin(admin.ModelAdmin):
    list_display = ('publication', 'badge_text', 'year', 'display_order')
    list_editable = ('display_order',)
