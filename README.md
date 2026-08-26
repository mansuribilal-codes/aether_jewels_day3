# AETHER JEWELS – CELESTIAL ATELIER
### Ultra-Luxury Digital Flagship for Sovereign High Jewellery

[![Django](https://img.shields.io/badge/Django-5.1.5-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![GSAP](https://img.shields.io/badge/GSAP-3.12.5%20ScrollTrigger-88CE02?style=for-the-badge&logo=greensock&logoColor=white)](https://greensock.com/gsap/)
[![Aesthetic](https://img.shields.io/badge/Aesthetic-Obsidian%20%26%20Champagne%20Gold-D4AF37?style=for-the-badge)](https://aetherjewels.com)

---

## 🌟 Brand Vision & Architecture

**Aether Jewels – Celestial Atelier** is an ultra-luxury digital flagship tailored for High-Net-Worth Individuals (HNWIs) in India and globally. The digital flagship embodies a celestial, cinematic, and intimate atmosphere designed to purvey sovereign, museum-grade high jewellery relics forged with astronomical Type IIa Golconda diamonds, unheated Kashmir sapphires, and Colombian Muzo emeralds.

---

## ✨ Signature Features

1. **Cinematic Hero Section**:
   - Celestial typography with gold foil gradient shimmer.
   - Floating centerpiece high jewellery visual with pulsing starlight stardust aura.
   - Dynamic canvas with interactive stardust and shooting meteor trails.

2. **Pinned Horizontal Scroll Showcase (GSAP + ScrollTrigger)**:
   - High Jewellery marquee suites presented through a smooth horizontal scroll journey.
   - Live Indian currency formatting (₹ Crores & Lakhs) with instant multi-currency conversion ($ USD, € EUR, AED, £ GBP).

3. **Interactive 3D / Canvas Bespoke Atelier Configurator**:
   - Real-time 3D gemstone facet and light dispersion simulator.
   - Customize Piece Type, Gemstone (Golconda Diamond, Kashmir Sapphire, Muzo Emerald, Burmese Ruby, Black Opal), Precious Metal (18k Champagne Gold, 950 Sovereign Platinum, 18k Rose Gold, Midnight Black Rhodium), Setting, and Carats.
   - Dynamic valuation calculation and direct bespoke commission dispatch to the Master Goldsmith.

4. **Private VIP Consultation Booking Suite**:
   - Reserve private appointments across flagship salons:
     - **Mumbai**: *The Bandra Celestial Suite, Pali Hill*
     - **New Delhi**: *The Chanakya Sovereign Lounge, Chanakyapuri*
     - **Jaipur**: *The Rambagh Palace Atelier, Bhawani Singh Road*
     - **Bangalore**: *Lavelle Road Sanctuary*
     - **Global**: *Encrypted 4K Video Salon*
   - Sommelier hospitality choices (Dom Pérignon Vintage Champagne, Makaibari Silver Needle Tea, Kashmiri Saffron Kahwa).
   - Instant AJAX confirmation with confidential VIP reservation ID.

5. **3D Tilt Product Cards & Quick-View Modal**:
   - Interactive mouse perspective tilt, secondary angle preview on hover, GIA & BIS 916 hallmark badges.
   - Instant quick-view drawer fetching gemological dossiers via AJAX.

6. **Craftsmanship & Provenance Storytelling**:
   - 4-step scroll journey: *Cosmic Gemstone Sourcing* ➔ *800-Hour Hand Forging* ➔ *40x Micro-Pavé Starlight Alignment* ➔ *Dual GIA & BIS 916 Hallmarking*.

7. **Cosmic Soundscape (Web Audio API)**:
   - Floating ambient synthesizer producing a smooth harmonic drone (432Hz ambient chord) and crystal chimes on tactile interactions.

8. **Private Client Vault**:
   - Client-side saved wishlist with badge counter in navigation and direct viewing tray scheduling.

---

## 🏛️ Project Directory Structure

```
Day3_1/
│── manage.py
│── requirements.txt
│── test_site.py
│── aether_jewels/
│   │── __init__.py
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│   └── asgi.py
│── atelier/
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── models.py
│   │── views.py
│   │── urls.py
│   │── context_processors.py
│   │── migrations/
│   │   └── 0001_initial.py
│   └── management/
│       └── commands/
│           │── __init__.py
│           └── seed_data.py
│── templates/
│   │── base.html
│   │── includes/
│   │   │── navbar.html
│   │   │── footer.html
│   │   │── cursor.html
│   │   │── concierge_modal.html
│   │   └── quick_view_modal.html
│   └── pages/
│       │── home.html
│       │── collections.html
│       │── collection_detail.html
│       │── product_list.html
│       │── product_detail.html
│       │── bespoke_configurator.html
│       │── consultation.html
│       │── heritage.html
│       │── journal_list.html
│       │── journal_detail.html
│       └── vault_wishlist.html
└── static/
    │── css/
    │   │── luxury_core.css
    │   │── components.css
    │   │── animations.css
    │   │── configurator.css
    │   └── responsive.css
    └── js/
        │── celestial_canvas.js
        │── soundscape.js
        │── currency_converter.js
        │── vault.js
        │── gsap_experience.js
        │── bespoke_atelier.js
        └── main.js
```

---

## 🚀 Setup & Execution Guide

### 1. Install Dependencies
Ensure Python 3.10+ is installed on your system. Run:
```bash
pip install -r requirements.txt
```

### 2. Apply Migrations & Seed Sovereign Data
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py seed_data
```
*The `seed_data` command will automatically populate 12+ celestial high jewellery masterpieces (e.g. ₹4.85 Cr Astral Nova Cascade, ₹2.20 Cr Kashmir Sapphire Ring), 4 collections, 6 categories, 5 flagship lounges, journal articles, and press reviews.*

### 3. Run Development Server
```bash
python manage.py runserver
```
Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser.

### 4. Create an Admin Superuser (Optional)
```bash
python manage.py createsuperuser
```
Access the Sovereign Control Suite at `http://127.0.0.1:8000/admin/`.

---

## 💎 CDNs & External Resources Used

- **Animations**: GSAP 3.12.5 & ScrollTrigger 3.12.5 (`https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/`)
- **Iconography**: Remix Icon 4.2.0 (`https://cdn.jsdelivr.net/npm/remixicon@4.2.0/`)
- **Typography**: Google Fonts (*Cinzel*, *Cormorant Garamond*, *Playfair Display*, *Montserrat*)
- **Soundscape**: Web Audio API Synthesizer (Zero external audio file latency)
