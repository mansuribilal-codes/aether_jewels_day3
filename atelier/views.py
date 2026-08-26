from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from .models import (
    Category, Collection, Product, FlagshipLounge,
    ConsultationBooking, BespokeInquiry, JournalArticle, PressQuote
)
import json
import datetime


def home_view(request):
    """Cinematic Luxury Flagship Homepage."""
    masterpieces = Product.objects.filter(is_masterpiece=True)[:6]
    featured_products = Product.objects.filter(is_featured=True).exclude(is_masterpiece=True)[:8]
    collections = Collection.objects.filter(is_active=True)[:4]
    categories = Category.objects.filter(is_featured=True)[:6]
    press_quotes = PressQuote.objects.all()
    journal_articles = JournalArticle.objects.filter(is_featured=True)[:3]
    flagships = FlagshipLounge.objects.filter(is_active=True)

    context = {
        'masterpieces': masterpieces,
        'featured_products': featured_products,
        'collections': collections,
        'categories': categories,
        'press_quotes': press_quotes,
        'journal_articles': journal_articles,
        'flagships': flagships,
        'hero_product': masterpieces.first(),
        'total_products': Product.objects.count(),
    }
    return render(request, 'pages/home.html', context)


def collection_list_view(request):
    """High Jewellery Collections Directory."""
    collections = Collection.objects.filter(is_active=True)
    return render(request, 'pages/collections.html', {'collections': collections})


def collection_detail_view(request, slug):
    """Individual High Jewellery Collection Showcase."""
    collection = get_object_or_404(Collection, slug=slug, is_active=True)
    products = Product.objects.filter(collection=collection)
    return render(request, 'pages/collection_detail.html', {
        'collection': collection,
        'products': products
    })


def product_list_view(request):
    """Filterable High Jewellery Catalog."""
    products = Product.objects.all()
    categories = Category.objects.all()
    collections = Collection.objects.filter(is_active=True)

    # Filtering
    category_slug = request.GET.get('category')
    collection_slug = request.GET.get('collection')
    metal = request.GET.get('metal')
    gemstone = request.GET.get('gemstone')
    price_range = request.GET.get('price')
    query = request.GET.get('q')
    sort = request.GET.get('sort', 'featured')

    current_category = None
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    if collection_slug:
        products = products.filter(collection__slug=collection_slug)

    if metal:
        products = products.filter(metal_type=metal)

    if gemstone:
        products = products.filter(primary_gemstone__icontains=gemstone)

    if query:
        products = products.filter(
            Q(title__icontains=query) |
            Q(subtitle__icontains=query) |
            Q(description__icontains=query) |
            Q(primary_gemstone__icontains=query)
        )

    if price_range:
        if price_range == 'under_1cr':
            products = products.filter(price_inr__lt=10000000)
        elif price_range == '1cr_3cr':
            products = products.filter(price_inr__gte=10000000, price_inr__lte=30000000)
        elif price_range == 'above_3cr':
            products = products.filter(price_inr__gt=30000000)

    # Sorting
    if sort == 'price_low':
        products = products.order_by('price_inr')
    elif sort == 'price_high':
        products = products.order_by('-price_inr')
    elif sort == 'carat_high':
        products = products.order_by('-carat_weight')
    elif sort == 'newest':
        products = products.order_by('-created_at')
    else:  # featured default
        products = products.order_by('-is_masterpiece', '-is_featured', '-created_at')

    context = {
        'products': products,
        'categories': categories,
        'collections': collections,
        'current_category': current_category,
        'active_category': category_slug,
        'active_collection': collection_slug,
        'active_metal': metal,
        'active_gemstone': gemstone,
        'active_price': price_range,
        'active_sort': sort,
        'search_query': query or '',
        'total_count': products.count(),
    }
    return render(request, 'pages/product_list.html', context)


def product_detail_view(request, slug):
    """High Jewellery Masterpiece Detail with 3D Depth & Gemological Specs."""
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(
        Q(category=product.category) | Q(collection=product.collection)
    ).exclude(id=product.id)[:4]
    flagships = FlagshipLounge.objects.filter(is_active=True)

    context = {
        'product': product,
        'related_products': related_products,
        'flagships': flagships,
    }
    return render(request, 'pages/product_detail.html', context)


def bespoke_configurator_view(request):
    """Interactive 3D / Canvas Bespoke Celestial Atelier Tool - Protected for authenticated patrons."""
    if not request.user.is_authenticated:
        messages.info(
            request,
            "Please sign in to your VIP Celestial Account to configure and commission bespoke pieces."
        )
        return redirect(f"{reverse('atelier:login')}?next={request.path}")

    flagships = FlagshipLounge.objects.filter(is_active=True)
    return render(request, 'pages/bespoke_configurator.html', {
        'flagships': flagships
    })


def consultation_view(request):
    """Private VIP Consultation Reservation Suite."""
    flagships = FlagshipLounge.objects.filter(is_active=True)
    return render(request, 'pages/consultation.html', {
        'flagships': flagships
    })


def heritage_view(request):
    """Celestial Atelier Legacy, Sourcing & Sovereign Craftsmanship."""
    return render(request, 'pages/heritage.html')


def journal_list_view(request):
    """The Celestial Gazette – High Jewellery Journal."""
    articles = JournalArticle.objects.all()
    featured_article = articles.filter(is_featured=True).first() or articles.first()
    other_articles = articles.exclude(id=featured_article.id) if featured_article else articles
    return render(request, 'pages/journal_list.html', {
        'featured_article': featured_article,
        'articles': other_articles
    })


def journal_detail_view(request, slug):
    """Journal Editorial Detail."""
    article = get_object_or_404(JournalArticle, slug=slug)
    recent_articles = JournalArticle.objects.exclude(id=article.id)[:3]
    return render(request, 'pages/journal_detail.html', {
        'article': article,
        'recent_articles': recent_articles
    })


def vault_wishlist_view(request):
    """Client's Private Celestial Vault / Saved Heirlooms."""
    flagships = FlagshipLounge.objects.filter(is_active=True)
    return render(request, 'pages/vault_wishlist.html', {
        'flagships': flagships
    })


def developer_view(request):
    """Dedicated Architect & Full Stack Developer Showcase."""
    developer_info = {
        'name': 'MOHAMMED BILAL MANSURI',
        'title': 'Full Stack Web Developer (Python / Django)',
        'phone': '+919723918213',
        'phone_display': '+91 97239 18213',
        'email': 'mansuribilal9792@gmail.com',
        'linkedin': 'linkedin.com/in/mohammed-bilal-mansuri-972013204',
        'linkedin_url': 'https://linkedin.com/in/mohammed-bilal-mansuri-972013204',
        'github': 'github.com/mansuribilal-codes',
        'github_url': 'https://github.com/mansuribilal-codes',
        'profile_image': 'https://sulead.in/static/img/Bilal_Mansuri.jpg',
    }
    return render(request, 'pages/developer.html', {'developer': developer_info})


# ==========================================
# USER AUTHENTICATION VIEWS
# ==========================================

def login_view(request):
    """VIP Patron Login."""
    if request.user.is_authenticated:
        return redirect(request.GET.get('next') or 'atelier:home')

    next_url = request.GET.get('next') or request.POST.get('next') or ''

    if request.method == 'POST':
        username_or_email = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        # Check if login is via email
        user = None
        if '@' in username_or_email:
            try:
                user_obj = User.objects.get(email__iexact=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None
        else:
            user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name or user.username}. Your Celestial Vault is active.")
            if next_url:
                return redirect(next_url)
            return redirect('atelier:home')
        else:
            messages.error(request, "Invalid patron credentials. Please verify your username or password.")

    return render(request, 'auth/login.html', {'next': next_url})


def register_view(request):
    """VIP Patron Membership Registration."""
    if request.user.is_authenticated:
        return redirect(request.GET.get('next') or 'atelier:home')

    next_url = request.GET.get('next') or request.POST.get('next') or ''

    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if not (username and email and password):
            messages.error(request, "Please fill in all required membership fields.")
        elif password != confirm_password:
            messages.error(request, "Passwords do not match. Please re-enter.")
        elif len(password) < 6:
            messages.error(request, "Password must be at least 6 characters long.")
        elif User.objects.filter(username__iexact=username).exists():
            messages.error(request, "This patron username is already reserved.")
        elif User.objects.filter(email__iexact=email).exists():
            messages.error(request, "An account with this confidential email already exists.")
        else:
            first_name = full_name.split()[0] if full_name else username
            last_name = " ".join(full_name.split()[1:]) if len(full_name.split()) > 1 else ""

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            login(request, user)
            messages.success(
                request,
                f"Welcome to Aether Jewels, {first_name}. Your VIP Patron Membership is established."
            )
            if next_url:
                return redirect(next_url)
            return redirect('atelier:bespoke')

    return render(request, 'auth/register.html', {'next': next_url})


def logout_view(request):
    """VIP Patron Logout."""
    logout(request)
    messages.info(request, "You have securely signed out of your Celestial Vault.")
    return redirect('atelier:home')


# ==========================================
# JSON API ENDPOINTS
# ==========================================

@csrf_exempt
@require_POST
def api_consultation_book(request):
    """AJAX endpoint to book a private VIP consultation."""
    try:
        data = json.loads(request.body.decode('utf-8'))
        full_name = data.get('full_name', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        city_lounge = data.get('city_lounge', '').strip()
        date_str = data.get('preferred_date', '').strip()
        preferred_time = data.get('preferred_time', '').strip()
        jewellery_interest = data.get('jewellery_interest', 'Celestial High Jewellery')
        estimated_budget = data.get('estimated_budget', '₹ 50 Lakhs+')
        hospitality_preference = data.get('hospitality_preference', 'Dom Pérignon Vintage Champagne')
        notes = data.get('notes', '')

        if not (full_name and email and phone and city_lounge and date_str):
            return JsonResponse({'success': False, 'error': 'Please provide all mandatory appointment details.'}, status=400)

        # Parse date
        try:
            preferred_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            preferred_date = datetime.date.today() + datetime.timedelta(days=2)

        booking = ConsultationBooking.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            city_lounge=city_lounge,
            preferred_date=preferred_date,
            preferred_time=preferred_time,
            jewellery_interest=jewellery_interest,
            estimated_budget=estimated_budget,
            hospitality_preference=hospitality_preference,
            notes=notes,
            status='pending'
        )

        return JsonResponse({
            'success': True,
            'booking_id': booking.booking_id,
            'message': f"Your private appointment reservation at {booking.city_lounge} has been received. Our Private Client Concierge will contact you via {booking.phone} within 2 hours to confirm your bespoke arrangements."
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


@csrf_exempt
@require_POST
def api_bespoke_inquire(request):
    """AJAX endpoint to submit a bespoke piece configuration inquiry."""
    if not request.user.is_authenticated:
        return JsonResponse({
            'success': False,
            'error': 'Please sign in to submit bespoke commission inquiries.',
            'redirect': f"{reverse('atelier:login')}?next={reverse('atelier:bespoke')}"
        }, status=401)

    try:
        data = json.loads(request.body.decode('utf-8'))
        client_name = data.get('client_name', '').strip() or request.user.get_full_name() or request.user.username
        email = data.get('email', '').strip() or request.user.email
        phone = data.get('phone', '').strip()
        piece_type = data.get('piece_type', 'Solitaire Ring')
        gemstone = data.get('gemstone', 'Golconda Flawless Diamond')
        metal = data.get('metal', '18k Celestial Champagne Gold')
        carat_weight = data.get('carat_weight', 3.0)
        setting_style = data.get('setting_style', 'Astral Halo')
        estimated_price_inr = data.get('estimated_price_inr', 0)
        custom_engraving = data.get('custom_engraving', '')
        notes = data.get('notes', '')

        if not (client_name and email and phone):
            return JsonResponse({'success': False, 'error': 'Please complete your name, email, and phone contact.'}, status=400)

        inquiry = BespokeInquiry.objects.create(
            client_name=client_name,
            email=email,
            phone=phone,
            piece_type=piece_type,
            gemstone=gemstone,
            metal=metal,
            carat_weight=float(carat_weight),
            setting_style=setting_style,
            estimated_price_inr=float(estimated_price_inr),
            custom_engraving=custom_engraving,
            notes=notes
        )

        return JsonResponse({
            'success': True,
            'inquiry_id': inquiry.inquiry_id,
            'message': f"Your Bespoke Atelier Commission Dossier (#{inquiry.inquiry_id}) has been transmitted directly to our Master Goldsmith. A private design rendezvous will be coordinated shortly."
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


@require_GET
def api_product_quickview(request, product_id):
    """AJAX endpoint returning product details for the luxury quick-view modal."""
    try:
        product = get_object_or_404(Product, id=product_id)
        data = {
            'id': product.id,
            'title': product.title,
            'subtitle': product.subtitle,
            'sku': product.sku,
            'price_inr': str(product.price_inr),
            'formatted_price': product.formatted_price_inr,
            'full_formatted_inr': product.full_formatted_inr,
            'carat_weight': str(product.carat_weight),
            'metal_description': product.metal_description,
            'primary_gemstone': product.primary_gemstone,
            'gemstone_origin': product.gemstone_origin,
            'clarity_cut': product.clarity_cut,
            'certification': product.certification,
            'description': product.description,
            'image_primary': product.image_primary,
            'image_secondary': product.image_secondary or product.image_primary,
            'url': f"/jewels/{product.slug}/",
        }
        return JsonResponse({'success': True, 'product': data})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=404)
