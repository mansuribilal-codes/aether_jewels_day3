from django.db import models
from django.utils.text import slugify
import uuid


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    tagline = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    hero_image = models.URLField(max_length=500, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['display_order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Collection(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    curator_note = models.TextField(blank=True)
    description = models.TextField(blank=True)
    cover_image = models.URLField(max_length=500, blank=True)
    ambient_video_url = models.URLField(max_length=500, blank=True)
    is_featured = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"
        ordering = ['-is_featured', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    METAL_CHOICES = [
        ('18k_champagne_gold', '18k Celestial Champagne Gold'),
        ('18k_rose_gold', '18k Starlight Rose Gold'),
        ('950_platinum', '950 Sovereign Platinum'),
        ('18k_black_rhodium', '18k Midnight Black Rhodium'),
        ('18k_dual_gold', '18k Dual Champagne & Platinum'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    sku = models.CharField(max_length=50, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    
    price_inr = models.DecimalField(max_digits=12, decimal_places=2, help_text="Price in Indian Rupees (INR)")
    is_price_on_request = models.BooleanField(default=False)
    
    carat_weight = models.DecimalField(max_digits=6, decimal_places=2, default=2.50)
    metal_type = models.CharField(max_length=60, choices=METAL_CHOICES, default='18k_champagne_gold')
    metal_description = models.CharField(max_length=150, default="18k Celestial Champagne Gold (750 Purity)")
    
    primary_gemstone = models.CharField(max_length=150, default="Golconda Type IIa Diamond")
    gemstone_origin = models.CharField(max_length=120, default="Historic Golconda, India")
    clarity_cut = models.CharField(max_length=150, default="Flawless / D Color / Celestial Brilliant")
    dimensions = models.CharField(max_length=150, blank=True, default="Masterpiece Proportions")
    certification = models.CharField(max_length=200, default="GIA Diamond Dossier & BIS 916 Hallmark")
    
    description = models.TextField()
    craftsmanship_story = models.TextField(blank=True)
    
    image_primary = models.URLField(max_length=500)
    image_secondary = models.URLField(max_length=500, blank=True)
    image_detail = models.URLField(max_length=500, blank=True)
    image_editorial = models.URLField(max_length=500, blank=True)
    
    is_featured = models.BooleanField(default=True)
    is_masterpiece = models.BooleanField(default=False, help_text="Featured in the Pinned Horizontal Scroll Showcase")
    in_stock = models.BooleanField(default=True)
    stock_count = models.PositiveIntegerField(default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-is_masterpiece', '-is_featured', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def formatted_price_inr(self):
        """Format Indian Currency with Indian comma grouping (Lakhs and Crores)."""
        if self.is_price_on_request:
            return "Price on Private Request"
        
        amount = int(self.price_inr)
        if amount >= 10000000:
            crores = amount / 10000000.0
            return f"₹ {crores:.2f} Cr"
        elif amount >= 100000:
            lakhs = amount / 100000.0
            return f"₹ {lakhs:.2f} Lakhs"
        else:
            return f"₹ {amount:,}"

    @property
    def full_formatted_inr(self):
        """Full ₹ format with standard Indian digits."""
        if self.is_price_on_request:
            return "Price on Request"
        s = str(int(self.price_inr))
        if len(s) <= 3:
            return f"₹ {s}"
        last_three = s[-3:]
        remaining = s[:-3]
        groups = []
        while len(remaining) > 2:
            groups.insert(0, remaining[-2:])
            remaining = remaining[:-2]
        if remaining:
            groups.insert(0, remaining)
        formatted = ",".join(groups) + "," + last_three
        return f"₹ {formatted}"


class FlagshipLounge(models.Model):
    city = models.CharField(max_length=80)
    lounge_name = models.CharField(max_length=150)
    address = models.TextField()
    phone = models.CharField(max_length=40, default="+91 22 8920 4400")
    email = models.EmailField(default="concierge@aetherjewels.com")
    hours = models.CharField(max_length=120, default="Private Appointment Only • 11:00 AM – 8:00 PM IST")
    image_url = models.URLField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Flagship Lounge"
        verbose_name_plural = "Flagship Lounges"
        ordering = ['display_order', 'city']

    def __str__(self):
        return f"{self.lounge_name} – {self.city}"


class ConsultationBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'In Concierge Review'),
        ('confirmed', 'Confirmed & Reserved'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    booking_id = models.CharField(max_length=30, unique=True, blank=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    city_lounge = models.CharField(max_length=100)
    preferred_date = models.DateField()
    preferred_time = models.CharField(max_length=100)
    jewellery_interest = models.CharField(max_length=120, default="Celestial High Jewellery")
    estimated_budget = models.CharField(max_length=80, blank=True)
    hospitality_preference = models.CharField(max_length=150, default="Vintage Champagne & Caviar")
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Consultation Booking"
        verbose_name_plural = "Consultation Bookings"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.booking_id} – {self.full_name} ({self.city_lounge})"

    def save(self, *args, **kwargs):
        if not self.booking_id:
            self.booking_id = f"AJ-VIP-{uuid.uuid4().hex[:6].upper()}"
        super().save(*args, **kwargs)


class BespokeInquiry(models.Model):
    inquiry_id = models.CharField(max_length=30, unique=True, blank=True)
    client_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    piece_type = models.CharField(max_length=100)
    gemstone = models.CharField(max_length=100)
    metal = models.CharField(max_length=100)
    carat_weight = models.DecimalField(max_digits=5, decimal_places=2, default=2.0)
    setting_style = models.CharField(max_length=100)
    estimated_price_inr = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    custom_engraving = models.CharField(max_length=150, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Bespoke Inquiry"
        verbose_name_plural = "Bespoke Inquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.inquiry_id} – {self.client_name} ({self.piece_type})"

    def save(self, *args, **kwargs):
        if not self.inquiry_id:
            self.inquiry_id = f"AJ-BESPOKE-{uuid.uuid4().hex[:6].upper()}"
        super().save(*args, **kwargs)


class JournalArticle(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    category = models.CharField(max_length=80, default="Haute Joaillerie Lore")
    author = models.CharField(max_length=100, default="Madame Vivienne Varma, Master Gemologist")
    read_time = models.CharField(max_length=30, default="5 min read")
    snippet = models.TextField()
    content = models.TextField()
    cover_image = models.URLField(max_length=500)
    published_date = models.DateField()
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Journal Article"
        verbose_name_plural = "Journal Articles"
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class PressQuote(models.Model):
    publication = models.CharField(max_length=100)
    quote = models.TextField()
    author_title = models.CharField(max_length=120, default="Haute Joaillerie Critic")
    badge_text = models.CharField(max_length=80, blank=True, default="Vogue Luxury Honors")
    year = models.CharField(max_length=10, default="2025")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Press Quote"
        verbose_name_plural = "Press Quotes"
        ordering = ['display_order']

    def __str__(self):
        return f"{self.publication} – {self.quote[:40]}..."
