from .models import Category, Collection, FlagshipLounge


def brand_context(request):
    """Global context available across all luxury templates."""
    try:
        categories = Category.objects.filter(is_featured=True)[:6]
        collections = Collection.objects.filter(is_active=True)[:4]
        flagships = FlagshipLounge.objects.filter(is_active=True)
    except Exception:
        categories = []
        collections = []
        flagships = []

    return {
        'BRAND_NAME': 'Aether Jewels',
        'BRAND_ATELIER': 'Celestial Atelier',
        'BRAND_TAGLINE': 'Purveyors of Celestial High Jewellery Since 1928',
        'CONCIERGE_PHONE': '+91 22 8920 4400',
        'CONCIERGE_WHATSAPP': '+91 98200 44000',
        'CONCIERGE_EMAIL': 'concierge@aetherjewels.com',
        'CURRENCIES': [
            {'code': 'INR', 'symbol': '₹', 'name': 'Indian Rupee (INR)', 'rate': 1.0},
            {'code': 'USD', 'symbol': '$', 'name': 'US Dollar (USD)', 'rate': 0.012},
            {'code': 'AED', 'symbol': 'AED', 'name': 'UAE Dirham (AED)', 'rate': 0.044},
            {'code': 'GBP', 'symbol': '£', 'name': 'British Pound (GBP)', 'rate': 0.0094},
            {'code': 'EUR', 'symbol': '€', 'name': 'Euro (EUR)', 'rate': 0.011},
        ],
        'NAV_CATEGORIES': categories,
        'NAV_COLLECTIONS': collections,
        'FLAGSHIPS': flagships,
    }
