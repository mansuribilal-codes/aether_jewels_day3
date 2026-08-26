from django.core.management.base import BaseCommand
from django.utils import timezone
from atelier.models import (
    Category, Collection, Product, FlagshipLounge,
    JournalArticle, PressQuote, ConsultationBooking, BespokeInquiry
)
from decimal import Decimal
import datetime


class Command(BaseCommand):
    help = "Seeds the database with celestial high jewellery products, collections, flagships, and journals."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Purging existing data to seed fresh Celestial Atelier masterpieces..."))
        Product.objects.all().delete()
        Collection.objects.all().delete()
        Category.objects.all().delete()
        FlagshipLounge.objects.all().delete()
        JournalArticle.objects.all().delete()
        PressQuote.objects.all().delete()

        # 1. CATEGORIES
        cat_high_jewellery = Category.objects.create(
            name="High Jewellery Suites",
            slug="high-jewellery-suites",
            tagline="Sovereign one-of-a-kind masterpieces forged with astronomical gemstones.",
            description="Monumental suites featuring Golconda diamonds, unheated Kashmir sapphires, and Muzo emeralds set in custom 950 platinum and champagne gold.",
            hero_image="https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=1600&q=85",
            display_order=1,
            is_featured=True
        )

        cat_solitaires = Category.objects.create(
            name="Celestial Solitaire Rings",
            slug="solitaire-rings",
            tagline="Cosmic solitaires capturing the eternal light of distant constellations.",
            description="Hand-sculpted engagement rings and standalone solitaires set with certified D-Flawless celestial cut diamonds.",
            hero_image="https://images.unsplash.com/photo-1605100804763-247f67b3557e?auto=format&fit=crop&w=1600&q=85",
            display_order=2,
            is_featured=True
        )

        cat_necklaces = Category.objects.create(
            name="Astral Necklaces & Chokers",
            slug="necklaces-chokers",
            tagline="Cascades of starlight gracefully contouring sovereign collarbones.",
            description="Intricate multi-row diamond cascades, Mughal-inspired basra pearl collars, and emerald torrents.",
            hero_image="https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=1600&q=85",
            display_order=3,
            is_featured=True
        )

        cat_earrings = Category.objects.create(
            name="Starlight Earrings",
            slug="starlight-earrings",
            tagline="Celestial chandeliers and luminous drops that catch every photon.",
            description="Sculptural chandelier earrings, detachable shoulder-grazers, and astronomical halo studs.",
            hero_image="https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&w=1600&q=85",
            display_order=4,
            is_featured=True
        )

        cat_cuffs = Category.objects.create(
            name="Royal Cuffs & Bangles",
            slug="cuffs-bangles",
            tagline="Sovereign wrist architecture with flexible celestial hinges.",
            description="Rigid cuffs and articulated open-ended bangles set with concentric halos of pigeon blood rubies and diamonds.",
            hero_image="https://images.unsplash.com/photo-1602751584552-8ba73aad10e1?auto=format&fit=crop&w=1600&q=85",
            display_order=5,
            is_featured=True
        )

        cat_mens = Category.objects.create(
            name="Men's Celestial Sovereign",
            slug="mens-celestial",
            tagline="Regal brooches, signet rings, and astrological talisman cufflinks.",
            description="Curated high jewellery for men: Golconda kalgis, raw meteorite cufflinks, and deep sapphire signets.",
            hero_image="https://images.unsplash.com/photo-1617038260897-41a1f14a8ca0?auto=format&fit=crop&w=1600&q=85",
            display_order=6,
            is_featured=True
        )

        # 2. COLLECTIONS
        col_solstice = Collection.objects.create(
            name="The Solstice High Jewellery",
            slug="solstice-collection",
            subtitle="The alignment of planetary fire and royal gemological heritage.",
            curator_note="Conceived over three solar cycles, The Solstice Collection honors the zenith of the sun with rare Ceylon yellow sapphires and Golconda diamonds.",
            description="An ode to cosmic illumination, featuring articulated golden rays and radiant cut solitaires.",
            cover_image="https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=1600&q=85",
            ambient_video_url="https://assets.mixkit.co/videos/42416/42416-720.mp4",
            is_featured=True
        )

        col_nebula = Collection.objects.create(
            name="Nebula Genesis",
            slug="nebula-genesis",
            subtitle="Deep galactic dust forged into Burmese rubies and midnight black rhodium.",
            curator_note="Inspired by stellar nurseries where newborn stars ignite, showcasing unheated Pigeon Blood rubies and black diamond micro-pavé.",
            description="Dynamic, asymmetrical silhouettes reminiscent of spiraling galaxies and cosmic nebulae.",
            cover_image="https://images.unsplash.com/photo-1573408301185-9146fe634ad0?auto=format&fit=crop&w=1600&q=85",
            ambient_video_url="https://assets.mixkit.co/videos/42417/42417-720.mp4",
            is_featured=True
        )

        col_astral = Collection.objects.create(
            name="Astral Luminary Masterpieces",
            slug="astral-luminary",
            subtitle="The pinnacle of pure starlight in 950 Sovereign Platinum.",
            curator_note="A limited capsule of sovereign pieces reserved for private international auctions and private royal commissions.",
            description="Ultra-pure Type IIa diamonds possessing an optical transparency found in only 1.8% of the world's natural diamonds.",
            cover_image="https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=1600&q=85",
            ambient_video_url="https://assets.mixkit.co/videos/42416/42416-720.mp4",
            is_featured=True
        )

        col_eclipse = Collection.objects.create(
            name="The Eclipse Sovereign Series",
            slug="the-eclipse-series",
            subtitle="The majestic dance of celestial darkness and blinding golden halos.",
            curator_note="Black Tahitian pearls, midnight onyx, and 18k Champagne gold crafted for evening galas and diplomatic soirees.",
            description="Bold contrast architecture exploring astronomical syzygy and total solar eclipses.",
            cover_image="https://images.unsplash.com/photo-1596944924616-7b38e7cfac36?auto=format&fit=crop&w=1600&q=85",
            is_featured=True
        )

        # 3. PRODUCTS (High Jewellery Masterpieces & Catalog)
        products_data = [
            # 1. High Jewellery Suite - Necklace
            {
                "title": "The Astral Nova Diamond Cascade",
                "slug": "astral-nova-diamond-cascade",
                "sku": "AJ-AST-001",
                "subtitle": "52.40 Carat Golconda-Type IIa Diamond Masterpiece in 950 Platinum",
                "category": cat_high_jewellery,
                "collection": col_astral,
                "price_inr": Decimal("48500000.00"),  # ₹ 4.85 Crore
                "carat_weight": Decimal("52.40"),
                "metal_type": "950_platinum",
                "metal_description": "950 Sovereign Platinum with 18k White Starlight Gold accents",
                "primary_gemstone": "Type IIa Golconda Natural Diamonds (D-Flawless)",
                "gemstone_origin": "Historic Golconda Mines / Certified Natural",
                "clarity_cut": "D Color / Flawless Clarity / Triple Excellent Celestial Brilliant & Pear Cuts",
                "dimensions": "Collar Circumference: 41.5cm / Central Cascade Drop: 7.2cm",
                "certification": "GIA Dossier #22184920 + Sovereign Heritage Hallmark",
                "description": "An astronomical marvel of high jewellery architecture. The Astral Nova Cascade comprises 128 individual marquise, pear, and brilliant-cut Type IIa diamonds, culminating in a magnificent 12.10 carat D-Flawless pear-shaped central drop that breathes with every movement.",
                "craftsmanship_story": "Over 820 hours of master goldsmithing at our Mumbai & Jaipur ateliers. Each stone was hand-faceted under 40x micro-magnification using historic starlight alignment angles to maximize internal light refraction.",
                "image_primary": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=1200&q=85",
                "image_secondary": "https://images.unsplash.com/photo-1599643477877-530eb83abc8e?auto=format&fit=crop&w=1200&q=85",
                "image_detail": "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=1200&q=85",
                "image_editorial": "https://images.unsplash.com/photo-1596944924616-7b38e7cfac36?auto=format&fit=crop&w=1200&q=85",
                "is_featured": True,
                "is_masterpiece": True,
                "stock_count": 1,
            },
            # 2. Solitaire Ring - Sapphire
            {
                "title": "The Celestial Solstice Kashmir Sapphire Ring",
                "slug": "celestial-solstice-kashmir-sapphire-ring",
                "sku": "AJ-SOL-002",
                "subtitle": "14.20 Carat Unheated Royal Velvet Kashmir Sapphire in 18k Champagne Gold",
                "category": cat_solitaires,
                "collection": col_solstice,
                "price_inr": Decimal("22000000.00"),  # ₹ 2.20 Crore
                "carat_weight": Decimal("14.20"),
                "metal_type": "18k_champagne_gold",
                "metal_description": "18k Bespoke Champagne Gold (750 Purity) with Platinum Prongs",
                "primary_gemstone": "Untreated Royal Blue Kashmir Sapphire",
                "gemstone_origin": "Padder Mines, Kashmir Valley (Circa 1910 Sourcing)",
                "clarity_cut": "Cushion Modified Brilliant / Unheated / Exceptional Velvet Hue",
                "dimensions": "Band Width: 3.4mm / Crown Elevation: 8.9mm / Ring Size: Custom Bespoke",
                "certification": "SSEF Swiss Gemmological Institute #118492 & Gubelin Gem Lab Certificate",
                "description": "Possessing the legendary velvety blue saturation only ever born in the high altitudes of Kashmir, this 14.20-carat untreated sapphire is cradled by twin shield-cut diamonds in our signature celestial sunburst basket.",
                "craftsmanship_story": "The basket was hand-chiseled from a single ingot of 18k Champagne Gold, designed to allow starlight to penetrate the pavilion from 360 degrees without metal interference.",
                "image_primary": "https://images.unsplash.com/photo-1605100804763-247f67b3557e?auto=format&fit=crop&w=1200&q=85",
                "image_secondary": "https://images.unsplash.com/photo-1603561591411-07134e71a2a9?auto=format&fit=crop&w=1200&q=85",
                "image_detail": "https://images.unsplash.com/photo-1598560917505-59a3ad559071?auto=format&fit=crop&w=1200&q=85",
                "image_editorial": "https://images.unsplash.com/photo-1573408301185-9146fe634ad0?auto=format&fit=crop&w=1200&q=85",
                "is_featured": True,
                "is_masterpiece": True,
                "stock_count": 1,
            },
            # 3. Necklace - Emerald Choker
            {
                "title": "The Starlight Constellation Emerald Choker",
                "slug": "starlight-constellation-emerald-choker",
                "sku": "AJ-EME-003",
                "subtitle": "48.60 Carat Colombian Muzo Emeralds & Rose-Cut Diamond Collar",
                "category": cat_necklaces,
                "collection": col_solstice,
                "price_inr": Decimal("36000000.00"),  # ₹ 3.60 Crore
                "carat_weight": Decimal("48.60"),
                "metal_type": "18k_dual_gold",
                "metal_description": "18k Celestial Champagne Gold & 950 Sovereign Platinum",
                "primary_gemstone": "Colombian Muzo Minor-Oil Emeralds (18 Matched Octagons)",
                "gemstone_origin": "Muzo Valley, Colombia",
                "clarity_cut": "Octagonal Step Cut / Vivid Green 'Jardin' / Minor Cedarwood Oil",
                "dimensions": "Choker Length: 38cm Flexible Articulation / Width: 22mm",
                "certification": "Gubelin Gemological Laboratory Report #994021 + BIS 916 Hallmark",
                "description": "Eighteen impeccably color-matched Muzo emeralds forming an ethereal constellation around the neck, interspersed with antique rose-cut diamonds and flexible mesh links that settle like liquid starlight on the skin.",
                "craftsmanship_story": "Collecting 18 matched octagonal emeralds of this vivid saturation required seven years of private sourcing across international private collections.",
                "image_primary": "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=1200&q=85",
                "image_secondary": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=1200&q=85",
                "image_detail": "https://images.unsplash.com/photo-1599643477877-530eb83abc8e?auto=format&fit=crop&w=1200&q=85",
                "image_editorial": "https://images.unsplash.com/photo-1596944924616-7b38e7cfac36?auto=format&fit=crop&w=1200&q=85",
                "is_featured": True,
                "is_masterpiece": True,
                "stock_count": 1,
            },
            # 4. Cuff / Bracelet - Ruby & Gold
            {
                "title": "The Nebula Eclipse Pigeon Blood Ruby Cuff",
                "slug": "nebula-eclipse-ruby-cuff",
                "sku": "AJ-NEB-004",
                "subtitle": "18.50 Carat Unheated Mogok Burmese Rubies in Black Rhodium Gold",
                "category": cat_cuffs,
                "collection": col_nebula,
                "price_inr": Decimal("19500000.00"),  # ₹ 1.95 Crore
                "carat_weight": Decimal("18.50"),
                "metal_type": "18k_black_rhodium",
                "metal_description": "18k Gold coated with Midnight Black Rhodium & 18k Rose Gold accents",
                "primary_gemstone": "Unheated Burmese 'Pigeon Blood' Rubies",
                "gemstone_origin": "Mogok Valley, Upper Myanmar",
                "clarity_cut": "Oval & Cushion Mixed Cuts / Strong Natural UV Fluorescence",
                "dimensions": "Inner Circumference: 16.5cm with Spring Hidden Safety Clasp",
                "certification": "GRS Swiss Gemresearch Report #2024-0982 & GIA Certificate",
                "description": "An avant-garde sculpted cuff echoing the violent beauty of stellar explosions. Deep crimson Pigeon Blood rubies seem to burst through dark titanium-black rhodium gold, framed by concentric halos of micro-pavé rose cut diamonds.",
                "craftsmanship_story": "Constructed with an internal ergonomic titanium spring mechanism that opens seamlessly with gentle pressure and locks with an audible celestial click.",
                "image_primary": "https://images.unsplash.com/photo-1573408301185-9146fe634ad0?auto=format&fit=crop&w=1200&q=85",
                "image_secondary": "https://images.unsplash.com/photo-1602751584552-8ba73aad10e1?auto=format&fit=crop&w=1200&q=85",
                "image_detail": "https://images.unsplash.com/photo-1611652022419-a9419f74343d?auto=format&fit=crop&w=1200&q=85",
                "image_editorial": "https://images.unsplash.com/photo-1598560917505-59a3ad559071?auto=format&fit=crop&w=1200&q=85",
                "is_featured": True,
                "is_masterpiece": True,
                "stock_count": 1,
            },
            # 5. Earrings - Diamond Chandelier
            {
                "title": "The Aurora Borealis Diamond Chandelier Earrings",
                "slug": "aurora-borealis-diamond-earrings",
                "sku": "AJ-AUR-005",
                "subtitle": "26.80 Carat Flawless Pear & Marquise Diamond Cascades",
                "category": cat_earrings,
                "collection": col_astral,
                "price_inr": Decimal("27500000.00"),  # ₹ 2.75 Crore
                "carat_weight": Decimal("26.80"),
                "metal_type": "950_platinum",
                "metal_description": "950 Featherlight High-Tensile Sovereign Platinum",
                "primary_gemstone": "Natural Type IIa Flawless White Diamonds",
                "gemstone_origin": "Botswana Orapa Vaults / Certified Conflict-Free",
                "clarity_cut": "E-F Color / VVS1 Clarity / Modified Briolette & Rose Cuts",
                "dimensions": "Length: 7.8cm / Width at Base: 2.4cm / Total Pair Weight: 32g",
                "certification": "Dual GIA Master Reports #4401823 & #4401824",
                "description": "Floating chandeliers that dance with zero resistance. As the wearer turns, each dangling briolette diamond captures light from independent angles, creating an auroral halo of white and prismatic fire.",
                "craftsmanship_story": "Micro-articulated with knife-edge platinum wire connections that make the metal framework entirely invisible when worn.",
                "image_primary": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&w=1200&q=85",
                "image_secondary": "https://images.unsplash.com/photo-1635767798638-3e25273a8236?auto=format&fit=crop&w=1200&q=85",
                "image_detail": "https://images.unsplash.com/photo-1630019852942-f89202989a59?auto=format&fit=crop&w=1200&q=85",
                "image_editorial": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=1200&q=85",
                "is_featured": True,
                "is_masterpiece": True,
                "stock_count": 1,
            },
            # 6. Solitaire Ring - Antique Cushion
            {
                "title": "The Supernova Golconda Solitaire (8.40ct)",
                "slug": "supernova-golconda-solitaire",
                "sku": "AJ-SOL-006",
                "subtitle": "8.40 Carat D-Flawless Type IIa Golconda Solitaire in 18k Champagne Gold",
                "category": cat_solitaires,
                "collection": col_astral,
                "price_inr": Decimal("32000000.00"),  # ₹ 3.20 Crore
                "carat_weight": Decimal("8.40"),
                "metal_type": "18k_champagne_gold",
                "metal_description": "18k Celestial Champagne Gold (750) with Platinum Astral Prongs",
                "primary_gemstone": "Type IIa Golconda Diamond (D-Flawless)",
                "gemstone_origin": "Historic Golconda Riverbeds, India",
                "clarity_cut": "D Color / Flawless Clarity / Antique Cushion Old Mine Cut",
                "dimensions": "Crown Spread: 13.8mm x 12.9mm / Custom Sizing Available",
                "certification": "GIA Master Dossier Type IIa Special Appendix #981023",
                "description": "An extraordinary 8.40-carat antique cushion solitaire boasting complete optical transparency and zero nitrogen impurities. Mounted upon our signature astral gallery, allowing unhindered starlight absorption.",
                "craftsmanship_story": "Set with 6 talon prongs hand-sculpted in pure 950 Platinum, blending seamlessly into an 18k Champagne Gold sovereign shank lined with secret micro-pavé stars.",
                "image_primary": "https://images.unsplash.com/photo-1603561591411-07134e71a2a9?auto=format&fit=crop&w=1200&q=85",
                "image_secondary": "https://images.unsplash.com/photo-1598560917505-59a3ad559071?auto=format&fit=crop&w=1200&q=85",
                "image_detail": "https://images.unsplash.com/photo-1605100804763-247f67b3557e?auto=format&fit=crop&w=1200&q=85",
                "image_editorial": "https://images.unsplash.com/photo-1588444837495-c6cfeb53f32d?auto=format&fit=crop&w=1200&q=85",
                "is_featured": True,
                "is_masterpiece": False,
                "stock_count": 1,
            },
            # 7. Necklace - Obsidian Torc
            {
                "title": "The Eclipse Obsidian & Diamond Sovereign Torc",
                "slug": "eclipse-obsidian-diamond-torc",
                "sku": "AJ-ECL-007",
                "subtitle": "Carved Obsidian, 18.20ct Pavé Diamonds & 18k Champagne Gold",
                "category": cat_necklaces,
                "collection": col_eclipse,
                "price_inr": Decimal("14500000.00"),  # ₹ 1.45 Crore
                "carat_weight": Decimal("18.20"),
                "metal_type": "18k_champagne_gold",
                "metal_description": "18k Celestial Champagne Gold (750) & Carved Natural Obsidian",
                "primary_gemstone": "Natural Obsidian Crystal & Brilliant White Diamonds",
                "gemstone_origin": "Volcanic Obsidian & Antwerp Diamonds",
                "clarity_cut": "E Color / VVS2 Clarity / Brilliant Round Micro-Pavé",
                "dimensions": "Torc Inner Diameter: 12.8cm Ergonomic Open Front Neckpiece",
                "certification": "IGI High Jewellery Certificate #AJ-2025-0091",
                "description": "A daring convergence of natural volcanic obsidian crystal carved by hand in Jaipur, enveloped in spiral ribbing of 18k Champagne gold and 18.20 carats of micro-pavé stardust diamonds.",
                "craftsmanship_story": "Each block of obsidian required 120 hours of delicate diamond-wheel carving to achieve the ergonomic neck curvature without structural fracture.",
                "image_primary": "https://images.unsplash.com/photo-1596944924616-7b38e7cfac36?auto=format&fit=crop&w=1200&q=85",
                "image_secondary": "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=1200&q=85",
                "image_detail": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=1200&q=85",
                "image_editorial": "https://images.unsplash.com/photo-1599643477877-530eb83abc8e?auto=format&fit=crop&w=1200&q=85",
                "is_featured": True,
                "is_masterpiece": False,
                "stock_count": 1,
            },
            # 8. Men's Celestial - Brooch & Kalgi
            {
                "title": "The Sovereign Celestial Kalgi & Brooch",
                "slug": "sovereign-celestial-kalgi-brooch",
                "sku": "AJ-MEN-008",
                "subtitle": "Basra Pearls, 12ct Uncut Polki Diamonds & Colombian Emerald Drop",
                "category": cat_mens,
                "collection": col_solstice,
                "price_inr": Decimal("18000000.00"),  # ₹ 1.80 Crore
                "carat_weight": Decimal("32.50"),
                "metal_type": "18k_champagne_gold",
                "metal_description": "22k/18k Sovereign Gold with Meenakari Enameling on Reverse",
                "primary_gemstone": "Natural Basra Pearls, Syndicate Polki Diamonds & Carved Muzo Emerald",
                "gemstone_origin": "Basra Gulf & Muzo Mines, Colombia",
                "clarity_cut": "Traditional Syndicate Jadau Polki & Carved Mughal Emerald",
                "dimensions": "Height: 11.2cm / Width: 4.8cm / Transformable to Lapel Brooch",
                "certification": "Sovereign Heritage Certificate & BIS Hallmark",
                "description": "An imperial turban jewel (Kalgi) transformable into an evening lapel brooch. Set with sovereign Syndicate Polki diamonds and suspended with an antique Mughal-carved Muzo emerald drop weighing 21 carats.",
                "craftsmanship_story": "Features hand-painted celestial blue Meenakari enamel on the reverse side depicting constellations, created by master enamelers in old Jaipur.",
                "image_primary": "https://images.unsplash.com/photo-1617038260897-41a1f14a8ca0?auto=format&fit=crop&w=1200&q=85",
                "image_secondary": "https://images.unsplash.com/photo-1543294001-f7cd5d7fb516?auto=format&fit=crop&w=1200&q=85",
                "image_detail": "https://images.unsplash.com/photo-1589674781759-c21c37956a44?auto=format&fit=crop&w=1200&q=85",
                "image_editorial": "https://images.unsplash.com/photo-1602751584552-8ba73aad10e1?auto=format&fit=crop&w=1200&q=85",
                "is_featured": True,
                "is_masterpiece": False,
                "stock_count": 1,
            },
            # 9. Solitaire Ring - Round Brilliant
            {
                "title": "The Starlight Constellation Solitaire Ring (4.20ct)",
                "slug": "starlight-constellation-solitaire-ring",
                "sku": "AJ-SOL-009",
                "subtitle": "4.20 Carat E-VVS1 Round Celestial Ideal Cut in 950 Platinum",
                "category": cat_solitaires,
                "collection": col_astral,
                "price_inr": Decimal("9500000.00"),  # ₹ 95 Lakhs
                "carat_weight": Decimal("4.20"),
                "metal_type": "950_platinum",
                "metal_description": "950 Sovereign Platinum with Secret Stardust Pavé Undergallery",
                "primary_gemstone": "Natural Diamond (E Color / VVS1 Clarity)",
                "gemstone_origin": "Canada Diavik Vaults / GIA Certified",
                "clarity_cut": "E Color / VVS1 Clarity / Celestial 108-Facet Proprietary Starlight Cut",
                "dimensions": "Crown Diameter: 10.6mm / Shank Width: 2.2mm",
                "certification": "GIA Master Certificate #12093847 & Laser Inscription",
                "description": "Featuring our proprietary 108-facet Celestial Cut, this 4.20ct diamond displays an internal 8-pointed star pattern with extraordinary light return even in low-lit candlelight chambers.",
                "craftsmanship_story": "Hand-set by our master setter in Mumbai with micro-bead prongs that disappear against the diamond's girdle.",
                "image_primary": "https://images.unsplash.com/photo-1598560917505-59a3ad559071?auto=format&fit=crop&w=1200&q=85",
                "image_secondary": "https://images.unsplash.com/photo-1605100804763-247f67b3557e?auto=format&fit=crop&w=1200&q=85",
                "image_detail": "https://images.unsplash.com/photo-1603561591411-07134e71a2a9?auto=format&fit=crop&w=1200&q=85",
                "image_editorial": "https://images.unsplash.com/photo-1588444837495-c6cfeb53f32d?auto=format&fit=crop&w=1200&q=85",
                "is_featured": True,
                "is_masterpiece": False,
                "stock_count": 2,
            },
            # 10. Earrings - Rose Gold Drops
            {
                "title": "The Celestial Comet Diamond Drop Earrings",
                "slug": "celestial-comet-diamond-drop-earrings",
                "sku": "AJ-EAR-010",
                "subtitle": "11.50 Carat Starlight Diamond Drops in 18k Rose Gold",
                "category": cat_earrings,
                "collection": col_solstice,
                "price_inr": Decimal("8800000.00"),  # ₹ 88 Lakhs
                "carat_weight": Decimal("11.50"),
                "metal_type": "18k_rose_gold",
                "metal_description": "18k Starlight Rose Gold (750) with Warm Champagne Nuances",
                "primary_gemstone": "Natural Fancy Light Pink & White Diamonds",
                "gemstone_origin": "Argyle & South Africa Mines",
                "clarity_cut": "VVS2 Clarity / Pear & Oval Brilliant Cascades",
                "dimensions": "Length: 5.4cm / French Lock Back Mechanism",
                "certification": "GIA Double Certification & Sovereign Hallmark",
                "description": "Evoking the luminous tail of a comet sweeping through twilight. Hand-set with graduated fancy light pink and white diamonds, cascading with graceful fluidity.",
                "craftsmanship_story": "Cast in our proprietary 18k Starlight Rose Gold alloy which resists oxidation and maintains a warm celestial glow indefinitely.",
                "image_primary": "https://images.unsplash.com/photo-1630019852942-f89202989a59?auto=format&fit=crop&w=1200&q=85",
                "image_secondary": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&w=1200&q=85",
                "image_detail": "https://images.unsplash.com/photo-1635767798638-3e25273a8236?auto=format&fit=crop&w=1200&q=85",
                "image_editorial": "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=1200&q=85",
                "is_featured": True,
                "is_masterpiece": False,
                "stock_count": 1,
            },
            # 11. Bangle / Cuff - Diamond Bangle
            {
                "title": "The Astral Halo Sovereign Bangle",
                "slug": "astral-halo-sovereign-bangle",
                "sku": "AJ-BAN-011",
                "subtitle": "16.40 Carat Oval Diamonds & 18k Champagne Gold Articulated Bangle",
                "category": cat_cuffs,
                "collection": col_astral,
                "price_inr": Decimal("16500000.00"),  # ₹ 1.65 Crore
                "carat_weight": Decimal("16.40"),
                "metal_type": "18k_champagne_gold",
                "metal_description": "18k Celestial Champagne Gold (750) with Hidden Dual Clasp",
                "primary_gemstone": "Natural Oval Brilliant Cut Diamonds (14 Matched)",
                "gemstone_origin": "Botswana Mines / Certified Natural",
                "clarity_cut": "D-E Color / VVS1 Clarity / Oval Brilliant",
                "dimensions": "Inner Oval Diameter: 58mm x 50mm (Medium Wrist)",
                "certification": "IGI Diamond Master Report & BIS 916 Hallmark",
                "description": "Fourteen rare oval brilliant-cut diamonds linked by hand in seamless champagne gold bezel bezels, creating an unbroken band of cosmic fire around the wrist.",
                "craftsmanship_story": "Engineered with dual concealed push-buttons and a magnetic safety hinge calibrated to withstand royal gala wear.",
                "image_primary": "https://images.unsplash.com/photo-1602751584552-8ba73aad10e1?auto=format&fit=crop&w=1200&q=85",
                "image_secondary": "https://images.unsplash.com/photo-1611652022419-a9419f74343d?auto=format&fit=crop&w=1200&q=85",
                "image_detail": "https://images.unsplash.com/photo-1573408301185-9146fe634ad0?auto=format&fit=crop&w=1200&q=85",
                "image_editorial": "https://images.unsplash.com/photo-1598560917505-59a3ad559071?auto=format&fit=crop&w=1200&q=85",
                "is_featured": True,
                "is_masterpiece": False,
                "stock_count": 2,
            },
            # 12. Men's Celestial - Signet Ring
            {
                "title": "The Imperial Midnight Signet Ring",
                "slug": "imperial-midnight-signet-ring",
                "sku": "AJ-MEN-012",
                "subtitle": "5.80ct Star Sapphire & Hand-Engraved 18k Champagne Gold",
                "category": cat_mens,
                "collection": col_nebula,
                "price_inr": Decimal("5800000.00"),  # ₹ 58 Lakhs
                "carat_weight": Decimal("5.80"),
                "metal_type": "18k_champagne_gold",
                "metal_description": "Solid Heavy 18k Champagne Gold (28 Grams)",
                "primary_gemstone": "Natural 6-Ray Black Star Sapphire",
                "gemstone_origin": "Sri Lanka High Mines / Untreated",
                "clarity_cut": "Cabochon Oval with Sharp Defined Asterism Star",
                "dimensions": "Crown Face: 18mm x 15mm / Heavy Solid Comfort Fit",
                "certification": "GIA Gemological Identification Report #6601934",
                "description": "A commanding men's sovereign signet ring featuring a natural asteriated black star sapphire that reveals a floating 6-ray starlight star when touched by direct sunlight or candlelight.",
                "craftsmanship_story": "Hand-engraved on both flanks with the celestial coordinates of the North Star by our Jaipur master engraver.",
                "image_primary": "https://images.unsplash.com/photo-1589674781759-c21c37956a44?auto=format&fit=crop&w=1200&q=85",
                "image_secondary": "https://images.unsplash.com/photo-1603561591411-07134e71a2a9?auto=format&fit=crop&w=1200&q=85",
                "image_detail": "https://images.unsplash.com/photo-1588444837495-c6cfeb53f32d?auto=format&fit=crop&w=1200&q=85",
                "image_editorial": "https://images.unsplash.com/photo-1605100804763-247f67b3557e?auto=format&fit=crop&w=1200&q=85",
                "is_featured": True,
                "is_masterpiece": False,
                "stock_count": 1,
            }
        ]

        for p in products_data:
            Product.objects.create(**p)

        # 4. FLAGSHIP LOUNGES
        flagships_data = [
            {
                "city": "Mumbai",
                "lounge_name": "The Bandra Celestial Suite",
                "address": "4th Floor, Sovereign Tower, Pali Hill, Bandra West, Mumbai 400050",
                "phone": "+91 22 8920 4400",
                "email": "mumbai.concierge@aetherjewels.com",
                "hours": "By Appointment Only • 11:00 AM – 8:00 PM IST",
                "image_url": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1000&q=85",
                "is_active": True,
                "display_order": 1
            },
            {
                "city": "New Delhi",
                "lounge_name": "The Chanakya Sovereign Lounge",
                "address": "Level 3, The Chanakya, Yashwant Place, Chanakyapuri, New Delhi 110021",
                "phone": "+91 11 4455 8800",
                "email": "delhi.concierge@aetherjewels.com",
                "hours": "By Appointment Only • 11:00 AM – 8:00 PM IST",
                "image_url": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1000&q=85",
                "is_active": True,
                "display_order": 2
            },
            {
                "city": "Jaipur",
                "lounge_name": "The Rambagh Palace Atelier",
                "address": "The Heritage Pavilion, Bhawani Singh Road, Rambagh, Jaipur 302005",
                "phone": "+91 141 238 5700",
                "email": "jaipur.concierge@aetherjewels.com",
                "hours": "By Appointment Only • 10:30 AM – 7:30 PM IST",
                "image_url": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=85",
                "is_active": True,
                "display_order": 3
            },
            {
                "city": "Bangalore",
                "lounge_name": "Lavelle Road Sanctuary",
                "address": "Penthouse 9, Sovereign Crest, Lavelle Road, Bangalore 560001",
                "phone": "+91 80 4910 2200",
                "email": "bangalore.concierge@aetherjewels.com",
                "hours": "By Appointment Only • 11:00 AM – 8:00 PM IST",
                "image_url": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=1000&q=85",
                "is_active": True,
                "display_order": 4
            },
            {
                "city": "Virtual Global",
                "lounge_name": "Encrypted High-Security Video Salon",
                "address": "Private 4K Optical Macro Stream & Real-time Gemological Spectrometry",
                "phone": "+91 22 8920 4400 (Concierge Direct)",
                "email": "virtual.concierge@aetherjewels.com",
                "hours": "24/7 Global Timezones • Concierge Scheduled",
                "image_url": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=1000&q=85",
                "is_active": True,
                "display_order": 5
            }
        ]

        for f in flagships_data:
            FlagshipLounge.objects.create(**f)

        # 5. JOURNAL ARTICLES
        articles_data = [
            {
                "title": "The Lore of Golconda: India's Sovereign Diamonds and Their Celestial Fire",
                "slug": "the-lore-of-golconda-diamonds",
                "category": "Haute Joaillerie Lore",
                "author": "Madame Vivienne Varma, Master Gemologist",
                "read_time": "6 min read",
                "snippet": "Why Golconda Type IIa diamonds remain the most chemically pure and visually luminous treasures in gemological history.",
                "content": "<p>Long before modern kimberlite pipes were discovered across southern continents, the legendary riverbeds of the Golconda kingdom in Southern India yielded stones of an otherworldly caliber. Characterized by a total absence of nitrogen in their crystalline matrix, Type IIa diamonds possess a watery, luminous transparency termed <em>'first water'</em>.</p><p>At Aether Jewels, our gemological scouts trace historical roughs and sovereign family vaults to acquire and recut these celestial relics, marrying ancient provenance with 21st-century starlight optical faceting.</p>",
                "cover_image": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=1200&q=85",
                "published_date": datetime.date(2026, 1, 15),
                "is_featured": True
            },
            {
                "title": "Untreated Kashmir Royal Sapphires: Blue Velvet from the Great Himalayan Rift",
                "slug": "untreated-kashmir-royal-sapphires",
                "category": "Gemstone Mastery",
                "author": "Dr. Aarav Singhania, Head of High Gemology",
                "read_time": "5 min read",
                "snippet": "Exploring the microscopic rutile silk that gives Kashmir sapphires their unmatched velvety glow under candlelight.",
                "content": "<p>Discovered in the 1880s following a remote landslide in the Zanskar range of Kashmir, these sapphires became the benchmark against which all blue corundum is measured. Unlike heated stones that lose their internal soul, untreated Kashmir sapphires contain extremely fine dustings of titanium dioxide (rutile) that gently scatter light.</p><p>We examine the arduous verification process at Gubelin and SSEF labs that certifies our pieces as sovereign heirlooms.</p>",
                "cover_image": "https://images.unsplash.com/photo-1605100804763-247f67b3557e?auto=format&fit=crop&w=1200&q=85",
                "published_date": datetime.date(2026, 2, 2),
                "is_featured": True
            },
            {
                "title": "Atelier Craft: 800 Hours of Micro-Pavé and Starlight Alignment",
                "slug": "atelier-craft-800-hours-micro-pave",
                "category": "The Atelier",
                "author": "Master Goldsmith Rajesh Parekh",
                "read_time": "4 min read",
                "snippet": "A glimpse into our Mumbai and Jaipur high jewellery benches where four generations of sovereign techniques converge.",
                "content": "<p>Every master creation at Aether Jewels begins with a hand-painted gouache rendering on midnight black parchment. Once approved by the patron, the jewel is hand-forged from recycled 950 sovereign platinum and 18k champagne gold ingots.</p><p>No 3D printing can replicate the tension, elasticity, and tactile warmth that hand-forged metal offers against high-carat precious gemstones.</p>",
                "cover_image": "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=1200&q=85",
                "published_date": datetime.date(2026, 2, 18),
                "is_featured": True
            }
        ]

        for a in articles_data:
            JournalArticle.objects.create(**a)

        # 6. PRESS QUOTES
        press_data = [
            {
                "publication": "Vogue India",
                "quote": "Aether Jewels redefines Indian high jewellery on the global stage with astronomical poise and museum-grade mastery.",
                "author_title": "Haute Joaillerie Editor",
                "badge_text": "High Jewellery Atelier of the Year",
                "year": "2025",
                "display_order": 1
            },
            {
                "publication": "Harper's Bazaar",
                "quote": "The confluence of sovereign Vedic heritage and modern celestial architecture. Aether's creations belong in royal collections.",
                "author_title": "Luxury & Heirlooms Critic",
                "badge_text": "Couture Design Honor",
                "year": "2025",
                "display_order": 2
            },
            {
                "publication": "Robb Report",
                "quote": "India's most coveted private high jewellery salon. The bespoke configurator and private viewing lounges set a worldwide benchmark.",
                "author_title": "Global Connoisseur Desk",
                "badge_text": "Best of Luxury Flagship",
                "year": "2026",
                "display_order": 3
            },
            {
                "publication": "Architectural Digest",
                "quote": "Bespoke wearable sculptures forged under celestial alignments. Every millimeter is an acoustic and optical triumph.",
                "author_title": "Design & Craft Special",
                "badge_text": "Sovereign Craft Excellence",
                "year": "2025",
                "display_order": 4
            }
        ]

        for pq in press_data:
            PressQuote.objects.create(**pq)

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {Product.objects.count()} high jewellery masterpieces, {Collection.objects.count()} collections, {Category.objects.count()} categories, and {FlagshipLounge.objects.count()} flagship lounges!"))
