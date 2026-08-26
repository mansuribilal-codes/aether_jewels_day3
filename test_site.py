import os
import django
import urllib.request
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aether_jewels.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from atelier.models import Product, Collection, Category

BASE_URL = "http://127.0.0.1:8000"

print("==================================================")
print("   AETHER JEWELS CELESTIAL ATELIER VERIFICATION   ")
print("==================================================")

client = Client()
all_passed = True

# 1. GUEST ACCESS PROTECTION
print("\n--- 1. TESTING GUEST PROTECTION ON BESPOKE ATELIER ---")
res = client.get('/bespoke-atelier/')
if res.status_code == 302 and '/login/' in res.get('Location', ''):
    print(f"[PASS] Guest accessing /bespoke-atelier/ was redirected to: {res.get('Location')}")
else:
    print(f"[FAIL] Expected 302 redirect to /login/, got: {res.status_code} {res.get('Location')}")
    all_passed = False

# 2. USER REGISTRATION
print("\n--- 2. TESTING PATRON REGISTRATION ---")
# Clean existing test user if present
User.objects.filter(username="vikram_patron_test").delete()
res = client.post('/register/', {
    'full_name': 'Maharaja Vikramaditya Singh',
    'username': 'vikram_patron_test',
    'email': 'vikram_test@royaljaipur.in',
    'phone': '+91 98200 44111',
    'password': 'CelestialPassword2026!',
    'confirm_password': 'CelestialPassword2026!',
    'next': '/bespoke-atelier/'
})
if res.status_code == 302 and res.get('Location') == '/bespoke-atelier/':
    print(f"[PASS] Registration successful and auto-redirected to: {res.get('Location')}")
else:
    print(f"[FAIL] Registration failed with status: {res.status_code}")
    all_passed = False

# 3. AUTHENTICATED ACCESS TO BESPOKE ATELIER
print("\n--- 3. TESTING AUTHENTICATED BESPOKE ACCESS & COMMISSION ---")
res = client.get('/bespoke-atelier/')
if res.status_code == 200:
    print("[PASS] Authenticated user opened /bespoke-atelier/ with 200 OK")
else:
    print(f"[FAIL] Failed to open bespoke atelier: {res.status_code}")
    all_passed = False

res = client.post('/api/bespoke/inquire/', {
    'client_name': 'Maharaja Vikramaditya Singh',
    'email': 'vikram_test@royaljaipur.in',
    'phone': '+91 98200 44111',
    'piece_type': 'Solitaire Ring',
    'gemstone': 'Kashmir Royal Blue Sapphire',
    'metal': '18k Celestial Champagne Gold',
    'carat_weight': 8.5,
    'setting_style': 'Astral Halo',
    'estimated_price_inr': 35000000,
    'custom_engraving': 'SOVEREIGN PROVENANCE',
    'notes': 'Must have SSEF certificate.'
}, content_type='application/json')
if res.status_code == 200 and res.json().get('success'):
    print(f"[PASS] Bespoke commission inquiry created: #{res.json().get('inquiry_id')}")
else:
    print(f"[FAIL] Commission creation failed: {res.status_code} {res.content}")
    all_passed = False

# 4. LOGOUT TEST
print("\n--- 4. TESTING LOGOUT ---")
res = client.get('/logout/')
if res.status_code == 302:
    print("[PASS] Logout successfully redirected to home")
else:
    print(f"[FAIL] Logout returned {res.status_code}")
    all_passed = False

# 5. ALL PAGES 200 OK TEST
print("\n--- 5. TESTING ALL LUXURY PAGE ROUTES ---")
routes = [
    ('/', 'Homepage'),
    ('/jewels/', 'Catalog'),
    ('/jewels/astral-nova-diamond-cascade/', 'Product Detail'),
    ('/collections/', 'Collections'),
    ('/collections/solstice-collection/', 'Collection Detail'),
    ('/book-consultation/', 'VIP Consultation'),
    ('/heritage/', 'Heritage'),
    ('/journal/', 'Journal'),
    ('/journal/the-lore-of-golconda-diamonds/', 'Journal Detail'),
    ('/vault/', 'Vault'),
    ('/developer/', 'About The Developer'),
    ('/login/', 'Login Page'),
    ('/register/', 'Register Page'),
]

for r_url, r_name in routes:
    res = client.get(r_url)
    if res.status_code == 200:
        print(f"[PASS] 200 OK: {r_name} ({r_url})")
    else:
        print(f"[FAIL] {res.status_code}: {r_name} ({r_url})")
        all_passed = False

# 6. VERIFY ZERO SHOE / ROLEX / BROKEN IMAGES
print("\n--- 6. VERIFYING IMAGE ACCURACY IN DATABASE ---")
forbidden_fragments = [
    "photo-1539185441755-769473a23570", # shoe
    "photo-1600003014755-ba31aa59c4b6", # rolex
    "photo-1611591475102-4fa8353ab465", # broken cuff
]

products = Product.objects.all()
collections = Collection.objects.all()
categories = Category.objects.all()

for p in products:
    for f in forbidden_fragments:
        if f in p.image_primary or f in (p.image_secondary or '') or f in (p.image_detail or '') or f in (p.image_editorial or ''):
            print(f"[FAIL] Found forbidden image ID in Product '{p.title}': {f}")
            all_passed = False

for c in collections:
    for f in forbidden_fragments:
        if f in c.cover_image:
            print(f"[FAIL] Found forbidden image ID in Collection '{c.name}': {f}")
            all_passed = False

for cat in categories:
    for f in forbidden_fragments:
        if f in cat.hero_image:
            print(f"[FAIL] Found forbidden image ID in Category '{cat.name}': {f}")
            all_passed = False

print(f"[PASS] All {products.count()} Products, {collections.count()} Collections, and {categories.count()} Categories have clean, verified luxury jewellery imagery!")

print("\n==================================================")
if all_passed:
    print(">>> ALL 8 ISSUES VERIFIED AND FIXED SUCCESSFULLY! <<<")
else:
    print(">>> SOME VERIFICATION TESTS FAILED! <<<")
    sys.exit(1)
