import os

os.makedirs("services", exist_ok=True)
os.makedirs("tours", exist_ok=True)
os.makedirs("areas", exist_ok=True)

# -----------------------------------------------------------------------------
# CORE BRAND CONSTANTS
# -----------------------------------------------------------------------------
BRAND_NAME = "Umair Taxi and Limo"
BRAND_TAGLINE = "Airport Transfers · Local Taxi · Tours Across Ireland"
BASE_LOCATION = "Youghal, County Cork, Ireland"
ADDRESS = "Istanbul Bites, Upper Cork Hill, Youghal, Ireland"
EMAIL = "Rana4874@gmail.com"
PHONE = "089 264 6246"
PHONE_TEL = "+353892646246"
WHATSAPP_LINK = "https://wa.me/353892646246?text=Hello%20Umair%20Taxi%20and%20Limo,%20I%20would%20like%20to%20inquire%20about%20a%20booking."

# -----------------------------------------------------------------------------
# NAVIGATION DEFINITION
# -----------------------------------------------------------------------------
def get_header(depth=0):
    rel = "../" if depth == 1 else ""
    return f"""  <!-- Compact Sticky Header (Desktop 76px / Mobile 64px) -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="{rel}index.html" class="brand-link" aria-label="Umair Taxi and Limo Home">
        <img src="{rel}assets/logo/logo-horizontal-dark.svg" alt="Umair Taxi and Limo Youghal" class="brand-header-logo" width="220" height="42">
      </a>

      <!-- Desktop Navigation with Multi-level Dropdowns -->
      <nav aria-label="Main Navigation">
        <ul class="nav-menu">
          <li><a href="{rel}index.html" class="nav-link">Home</a></li>
          
          <!-- Services Dropdown -->
          <li class="nav-item-dropdown">
            <a href="{rel}services.html" class="nav-link">Services <span class="dropdown-chevron">&#9662;</span></a>
            <ul class="dropdown-menu">
              <li><a href="{rel}services/airport-transfers.html">✈️ Airport Transfers (Primary)</a></li>
              <li><a href="{rel}services/local-taxi.html">🚕 Local Taxi (Youghal &amp; Cork)</a></li>
              <li><a href="{rel}services/golf-tours.html">⛳ Golf Tours</a></li>
              <li><a href="{rel}services/corporate-travel.html">💼 Corporate Travel &amp; Events</a></li>
              <li><a href="{rel}services/hospital-runs.html">🏥 Hospital Runs</a></li>
              <li><a href="{rel}services/aircoach-transfers.html">🚌 Aircoach &amp; Station Runs</a></li>
              <li class="divider"></li>
              <li><a href="{rel}services.html">📋 View All Services</a></li>
            </ul>
          </li>

          <!-- Tours Dropdown -->
          <li class="nav-item-dropdown">
            <a href="{rel}tours.html" class="nav-link">Tours <span class="dropdown-chevron">&#9662;</span></a>
            <ul class="dropdown-menu">
              <li><a href="{rel}tours.html">🗺️ All Ireland Tours</a></li>
              <li><a href="{rel}tours.html#cork">🏰 Cork &amp; Blarney Tours</a></li>
              <li><a href="{rel}tours.html#waterford">🌊 Waterford &amp; Copper Coast</a></li>
              <li><a href="{rel}tours.html#youghal">⚓ Historic Youghal Tours</a></li>
              <li><a href="{rel}tours.html#dungarvan">🚲 Dungarvan &amp; Greenway</a></li>
              <li><a href="{rel}tours.html#west-cork">🌄 West Cork Scenic Tours</a></li>
              <li><a href="{rel}services/golf-tours.html">⛳ Golf Course Tours</a></li>
              <li class="divider"></li>
              <li><a href="{rel}tours.html#custom">✨ Custom Private Tours</a></li>
            </ul>
          </li>

          <!-- Service Areas Dropdown -->
          <li class="nav-item-dropdown">
            <a href="{rel}service-areas.html" class="nav-link">Areas <span class="dropdown-chevron">&#9662;</span></a>
            <ul class="dropdown-menu">
              <li><a href="{rel}service-areas.html#youghal">📍 Youghal (Primary Base)</a></li>
              <li><a href="{rel}service-areas.html#cork">✈️ Cork City &amp; Airport</a></li>
              <li><a href="{rel}service-areas.html#waterford">💎 Waterford City &amp; Co.</a></li>
              <li><a href="{rel}service-areas.html#dungarvan">⛵ Dungarvan &amp; Greenway</a></li>
              <li><a href="{rel}service-areas.html#co-cork">🏡 County Cork Region</a></li>
              <li><a href="{rel}service-areas.html#west-waterford">🌿 West Waterford Region</a></li>
              <li class="divider"></li>
              <li><a href="{rel}service-areas.html">🗺️ All Service Areas</a></li>
            </ul>
          </li>

          <li><a href="{rel}fleet.html" class="nav-link">Fleet</a></li>
          <li><a href="{rel}about.html" class="nav-link">About</a></li>
          <li><a href="{rel}contact.html" class="nav-link">Contact</a></li>
        </ul>
      </nav>

      <!-- Concise Header CTAs -->
      <div class="header-right">
        <a href="tel:{PHONE_TEL}" class="phone-quick-link" aria-label="Call Dispatch 089 264 6246">
          <span>📞</span>
          <span>{PHONE}</span>
        </a>

        <a href="tel:{PHONE_TEL}" class="mobile-phone-btn" aria-label="Call Dispatch">
          <span>📞</span>
        </a>

        <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="padding: 9px 18px; font-size: 13px;">
          WhatsApp
        </a>

        <button class="burger-btn" aria-label="Toggle mobile menu" onclick="toggleMobileNav()">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer -->
  <div class="mobile-drawer" id="mobileDrawer">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
      <span style="color: var(--gold-primary); font-weight: 700; font-size: 14px; letter-spacing: 0.1em;">MENU</span>
      <button onclick="toggleMobileNav()" style="background: none; border: none; color: #FFF; font-size: 24px; cursor: pointer;">&times;</button>
    </div>
    <ul class="mobile-drawer-links">
      <li><a href="{rel}index.html">🏠 Home</a></li>
      <li><a href="{rel}services.html">📋 All Services</a></li>
      <li style="padding-left: 14px;"><a href="{rel}services/airport-transfers.html">✈️ Airport Transfers</a></li>
      <li style="padding-left: 14px;"><a href="{rel}services/local-taxi.html">🚕 Local Taxi (Youghal)</a></li>
      <li style="padding-left: 14px;"><a href="{rel}services/golf-tours.html">⛳ Golf Tours</a></li>
      <li style="padding-left: 14px;"><a href="{rel}services/corporate-travel.html">💼 Corporate Travel</a></li>
      <li style="padding-left: 14px;"><a href="{rel}services/hospital-runs.html">🏥 Hospital Runs</a></li>
      <li style="padding-left: 14px;"><a href="{rel}services/aircoach-transfers.html">🚌 Aircoach Runs</a></li>
      <li><a href="{rel}tours.html">🗺️ Ireland Tours</a></li>
      <li><a href="{rel}service-areas.html">📍 Service Areas</a></li>
      <li><a href="{rel}fleet.html">🚘 Fleet</a></li>
      <li><a href="{rel}about.html">ℹ️ About Us</a></li>
      <li><a href="{rel}contact.html">📞 Contact</a></li>
    </ul>

    <div style="margin-top: 24px; display: flex; flex-direction: column; gap: 10px;">
      <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="width: 100%; justify-content: center;">
        💬 WhatsApp: {PHONE}
      </a>
      <a href="tel:{PHONE_TEL}" class="btn-outline" style="width: 100%; justify-content: center;">
        📞 Call: {PHONE}
      </a>
    </div>
  </div>"""

def get_footer(depth=0):
    rel = "../" if depth == 1 else ""
    return f"""  <!-- Pre-Footer Call to Action Section -->
  <section class="pre-footer-cta">
    <div class="container">
      <div class="cta-card">
        <span class="section-tag">📍 Youghal · Cork · Waterford · Ireland</span>
        <h2 class="cta-heading">Ready to Book Your Journey?</h2>
        <p class="cta-desc">
          Whether you need a punctual Cork Airport transfer, a prompt local taxi in Youghal, or a bespoke private tour around Ireland, we are ready to assist you.
        </p>
        <div class="cta-btns">
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold">
            💬 WhatsApp Now
          </a>
          <a href="tel:{PHONE_TEL}" class="btn-outline">
            📞 Call: {PHONE}
          </a>
          <a href="{rel}tours.html" class="btn-outline">
            🗺️ View Tours
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Site Footer (Real Verified Business Details) -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a href="{rel}index.html">
            <img src="{rel}assets/logo/logo-horizontal-dark.svg" alt="Umair Taxi and Limo" class="footer-brand-logo">
          </a>
          <p class="footer-about-text">
            Dependable local taxi service, Cork &amp; Dublin airport transfers, and private tours all around Ireland. Proudly based in Youghal, County Cork. Fully licensed by the National Transport Authority (NTA Ireland).
          </p>
          <div style="font-size: 12px; color: var(--gold-light);">
            📍 Base: {BASE_LOCATION}
          </div>
        </div>

        <div>
          <h4 class="footer-h4">Our Services</h4>
          <ul class="footer-nav">
            <li><a href="{rel}services/airport-transfers.html">✈️ Airport Transfers</a></li>
            <li><a href="{rel}services/local-taxi.html">🚕 Local Taxi (Youghal)</a></li>
            <li><a href="{rel}services/golf-tours.html">⛳ Golf Course Tours</a></li>
            <li><a href="{rel}services/corporate-travel.html">💼 Corporate Events</a></li>
            <li><a href="{rel}services/hospital-runs.html">🏥 Hospital Appointments</a></li>
            <li><a href="{rel}services/aircoach-transfers.html">🚌 Aircoach Runs</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-h4">Key Service Areas</h4>
          <ul class="footer-nav">
            <li><a href="{rel}service-areas.html#youghal">📍 Youghal (Primary Base)</a></li>
            <li><a href="{rel}service-areas.html#cork">✈️ Cork Airport &amp; City</a></li>
            <li><a href="{rel}service-areas.html#waterford">💎 Waterford &amp; Copper Coast</a></li>
            <li><a href="{rel}service-areas.html#dungarvan">⛵ Dungarvan &amp; West Waterford</a></li>
            <li><a href="{rel}tours.html">🗺️ Tours Across Ireland</a></li>
            <li><a href="{rel}service-areas.html">📍 View All Areas</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-h4">Direct Contact</h4>
          <div class="footer-contact-row">
            <span>📞</span>
            <div>
              <strong>Phone:</strong><br>
              <a href="tel:{PHONE_TEL}" style="color: #FFF;">{PHONE}</a>
            </div>
          </div>
          <div class="footer-contact-row">
            <span>💬</span>
            <div>
              <strong>WhatsApp:</strong><br>
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" style="color: var(--gold-light);">089 264 6246 (Instant Reply)</a>
            </div>
          </div>
          <div class="footer-contact-row">
            <span>✉️</span>
            <div>
              <strong>Email:</strong><br>
              <a href="mailto:{EMAIL}" style="color: #FFF;">{EMAIL}</a>
            </div>
          </div>
          <div class="footer-contact-row">
            <span>📍</span>
            <div>
              <strong>Base Address:</strong><br>
              {ADDRESS}
            </div>
          </div>
        </div>
      </div>

      <div class="footer-bottom-bar">
        <div>&copy; 2026 {BRAND_NAME}. All rights reserved. Licensed Irish SPSV Operator.</div>
        <div>Muted Champagne Gold &bull; Obsidian Black &bull; Warm Ivory</div>
      </div>
    </div>
  </footer>

  <!-- Floating WhatsApp Pill -->
  <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="floating-whatsapp" aria-label="Chat on WhatsApp">
    <span>💬</span>
    <span>WhatsApp Us</span>
  </a>

  <!-- Mobile Toggle Script -->
  <script>
    function toggleMobileNav() {{
      const drawer = document.getElementById('mobileDrawer');
      drawer.classList.toggle('is-open');
    }}
    function toggleFaqItem(btn) {{
      const content = btn.nextElementSibling;
      const icon = btn.querySelector('.faq-icon');
      if (content.style.display === 'block') {{
        content.style.display = 'none';
        icon.style.transform = 'rotate(0deg)';
      }} else {{
        content.style.display = 'block';
        icon.style.transform = 'rotate(180deg)';
      }}
    }}
    function sendEnquiryWhatsApp(e) {{
      e.preventDefault();
      const pickup = document.getElementById('enqPickup') ? document.getElementById('enqPickup').value : '';
      const dropoff = document.getElementById('enqDropoff') ? document.getElementById('enqDropoff').value : '';
      const date = document.getElementById('enqDate') ? document.getElementById('enqDate').value : '';
      const pax = document.getElementById('enqPax') ? document.getElementById('enqPax').value : '';
      const msg = `Hello Umair Taxi and Limo, I would like a quote:%0A- Pickup: ${{pickup || 'Youghal'}}%0A- Destination: ${{dropoff || 'Cork Airport'}}%0A- Date/Time: ${{date || 'Upcoming'}}%0A- Passengers: ${{pax || '1-4'}}`;
      window.open(`https://wa.me/353892646246?text=${{msg}}`, '_blank');
    }}
  </script>"""

print("Helper definitions loaded successfully.")

# -----------------------------------------------------------------------------
# 1. HOMEPAGE GENERATOR (index.html)
# -----------------------------------------------------------------------------
def build_index():
    header = get_header(depth=0)
    footer = get_footer(depth=0)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Umair Taxi and Limo · Airport Transfers, Local Taxi &amp; Ireland Tours | Youghal, Cork</title>
  <meta name="description" content="Based in Youghal, Co. Cork. Prompt 24/7 local taxi dispatch, dedicated transfers to Cork Airport (ORK) &amp; Dublin Airport, and bespoke private tours across Ireland. Call 089 264 6246.">
  <link rel="icon" type="image/svg+xml" href="assets/logo/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

{header}

  <!-- Hero Section with LusiDriver-inspired UX & Booking Module -->
  <section class="hero-section">
    <div class="hero-bg-media">
      <!-- High quality Irish coastal landscape (County Cork & West Waterford) -->
      <img src="https://images.unsplash.com/photo-1590089415225-401ed6f9db8e?auto=format&fit=crop&q=80&w=1920" 
           alt="Scenic Irish Coastal Highway Youghal Cork" loading="eager">
    </div>
    <div class="hero-bg-overlay"></div>

    <div class="container hero-container">
      <div class="hero-header-box">
        <div class="hero-base-badge">
          📍 Base: Youghal, Co. Cork &bull; Cork Airport &bull; Tours All Around Ireland
        </div>
        <h1 class="hero-h1">
          Your Trusted Taxi, Airport Transfers<br>
          <span>&amp; Ireland Tours</span>
        </h1>
        <p class="hero-subhead">
          Proudly based at <strong>Upper Cork Hill, Youghal</strong>. Dedicated to punctual airport pickups at <strong>Cork Airport (ORK)</strong>, dependable local taxi runs across Youghal, Dungarvan &amp; Cork, and unforgettable private tours across Ireland.
        </p>

        <div class="hero-ctas-row">
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold">
            💬 WhatsApp: {PHONE}
          </a>
          <a href="tel:{PHONE_TEL}" class="btn-outline">
            📞 Call Dispatch: {PHONE}
          </a>
          <a href="tours.html" class="btn-outline">
            🗺️ Explore Tours
          </a>
        </div>
      </div>

      <!-- Quick Trip Enquiry Module (LusiDriver Structure) -->
      <div class="enquiry-card-wrapper">
        <div class="enquiry-card-header">
          <div class="enquiry-card-title">
            <span>✈️</span>
            <span>Quick Trip Enquiry &amp; Fare Quote</span>
          </div>
          <div class="enquiry-card-subtitle">
            Instant Reply via WhatsApp
          </div>
        </div>

        <form onsubmit="sendEnquiryWhatsApp(event)">
          <div class="enquiry-grid">
            <div class="form-field">
              <label for="enqPickup" class="field-label">📍 Pickup Location</label>
              <input type="text" id="enqPickup" class="field-control" placeholder="e.g. Youghal, Cork Airport, Dungarvan" required>
            </div>
            <div class="form-field">
              <label for="enqDropoff" class="field-label">🏁 Destination</label>
              <input type="text" id="enqDropoff" class="field-control" placeholder="e.g. Cork Airport, Dublin, Hotel, Tour" required>
            </div>
            <div class="form-field">
              <label for="enqDate" class="field-label">📅 Date &amp; Time</label>
              <input type="text" id="enqDate" class="field-control" placeholder="e.g. Today 14:30 or 25 Nov">
            </div>
            <div class="form-field">
              <label for="enqPax" class="field-label">👥 Passengers &amp; Bags</label>
              <select id="enqPax" class="field-control">
                <option value="1-4 Passengers (Saloon)">1–4 Passengers (Saloon Taxi)</option>
                <option value="5-8 Passengers (MPV)">5–8 Passengers (Tour MPV)</option>
                <option value="Group 8+ (Large Vehicle)">Group 8+ (Large Vehicle)</option>
                <option value="Golf Bags / Luggage">Golf Tour / Bulky Luggage</option>
              </select>
            </div>
          </div>

          <div class="enquiry-actions">
            <span class="enquiry-note">
              ✅ Guaranteed quote &bull; Zero peak surge &bull; Licensed local Irish driver
            </span>
            <div style="display: flex; gap: 10px; flex-wrap: wrap;">
              <button type="submit" class="btn-gold" style="border: none; cursor: pointer;">
                Get Quote on WhatsApp
              </button>
              <a href="tel:{PHONE_TEL}" class="btn-outline">
                Call {PHONE}
              </a>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>

  <!-- 3 Core Business Pillars -->
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Core Specializations</span>
        <h2 class="section-title">What We Do Best</h2>
        <p class="section-desc">
          Focused on dependable airport connections, rapid local taxi availability, and custom scenic touring across Ireland.
        </p>
      </div>

      <div class="pillars-grid">
        <!-- Pillar 1: Airport Transfers (MAIN SERVICE) -->
        <div class="pillar-card">
          <div>
            <div class="pillar-badge">✈️</div>
            <h3 class="pillar-title">Airport Transfers</h3>
            <p class="pillar-desc">
              Our primary service. Dedicated door-to-door runs between <strong>Cork Airport (ORK)</strong>, <strong>Dublin Airport (DUB)</strong>, and Youghal, Waterford, Dungarvan &amp; surrounding towns. Flight monitoring and terminal meet &amp; greet included.
            </p>
          </div>
          <div>
            <a href="services/airport-transfers.html" class="pillar-link">Airport Transfers &rarr;</a>
          </div>
        </div>

        <!-- Pillar 2: Local Taxi Service -->
        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🚕</div>
            <h3 class="pillar-title">Local Taxi Service</h3>
            <p class="pillar-desc">
              Prompt, reliable local taxi service based in <strong>Youghal</strong>. Available for trips around town, Killeagh, Castlemartyr, Midleton, Dungarvan, train stations, restaurants, medical visits, and evenings out.
            </p>
          </div>
          <div>
            <a href="services/local-taxi.html" class="pillar-link">Local Taxi Details &rarr;</a>
          </div>
        </div>

        <!-- Pillar 3: Tours Across Ireland -->
        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🗺️</div>
            <h3 class="pillar-title">Tours Across Ireland</h3>
            <p class="pillar-desc">
              Inspired by Ireland's premier scenic touring routes. Explore Blarney Castle, the Copper Coast, Ring of Kerry, Waterford Crystal, Jameson Midleton, and the Wild Atlantic Way with an experienced local driver.
            </p>
          </div>
          <div>
            <a href="tours.html" class="pillar-link">Explore Ireland Tours &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Supporting Services Section -->
  <section class="section section-alt">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Supporting Services</span>
        <h2 class="section-title">Tailored Transport For Every Journey</h2>
        <p class="section-desc">From championship golf links to punctual hospital appointments and coach connections.</p>
      </div>

      <div class="services-4grid">
        <div class="service-box">
          <div class="service-emoji">⛳</div>
          <h3 class="service-box-title">Golf Tours</h3>
          <p class="service-box-desc">
            Comfortable transport with spacious boot room for golf clubs to Old Head of Kinsale, Castlemartyr, Fota Island &amp; Dungarvan.
          </p>
          <a href="services/golf-tours.html" class="pillar-link">View Golf Tours &rarr;</a>
        </div>

        <div class="service-box">
          <div class="service-emoji">💼</div>
          <h3 class="service-box-title">Corporate Travel &amp; Events</h3>
          <p class="service-box-desc">
            Punctual, professional transport for business meetings, conferences, visiting delegations, and regional corporate events.
          </p>
          <a href="services/corporate-travel.html" class="pillar-link">Corporate Travel &rarr;</a>
        </div>

        <div class="service-box">
          <div class="service-emoji">🏥</div>
          <h3 class="service-box-title">Hospital Runs</h3>
          <p class="service-box-desc">
            Careful, courteous, and stress-free transport to Cork University Hospital (CUH), Mercy Hospital, and University Hospital Waterford.
          </p>
          <a href="services/hospital-runs.html" class="pillar-link">Hospital Runs &rarr;</a>
        </div>

        <div class="service-box">
          <div class="service-emoji">🚌</div>
          <h3 class="service-box-title">Aircoach &amp; Station Runs</h3>
          <p class="service-box-desc">
            Smooth transfers to connecting Aircoach stops, Kent Train Station (Cork), Plunkett Station (Waterford), and ferry ports.
          </p>
          <a href="services/aircoach-transfers.html" class="pillar-link">Aircoach Transfers &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- "Explore Ireland With Us" Tours Section -->
  <section class="section" id="tours">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Explore Ireland With Us</span>
        <h2 class="section-title">Private Tours Around Ireland</h2>
        <p class="section-desc">
          Enjoy the freedom of a private vehicle and local driver. No crowded coaches, no rigid itineraries. Set your own pace.
        </p>
      </div>

      <div class="tours-grid">
        <!-- Tour 1: Cork & Blarney -->
        <div class="tour-card">
          <div class="tour-media">
            <img src="https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&q=80&w=800" alt="Blarney Castle & Cork Highlights">
            <span class="tour-badge">County Cork</span>
          </div>
          <div class="tour-body">
            <div>
              <h3 class="tour-title">Cork &amp; Blarney Castle Tour</h3>
              <p class="tour-desc">
                Visit the historic Blarney Castle &amp; Gardens, kiss the Blarney Stone, explore the English Market in Cork City, and discover colourful Kinsale harbour.
              </p>
            </div>
            <div class="tour-footer">
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 12px; padding: 7px 14px;">
                Inquire on WhatsApp
              </a>
              <a href="tours.html#cork" class="pillar-link">Learn More &rarr;</a>
            </div>
          </div>
        </div>

        <!-- Tour 2: Waterford & Copper Coast -->
        <div class="tour-card">
          <div class="tour-media">
            <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&q=80&w=800" alt="Waterford & Copper Coast">
            <span class="tour-badge">Waterford</span>
          </div>
          <div class="tour-body">
            <div>
              <h3 class="tour-title">Waterford &amp; Copper Coast</h3>
              <p class="tour-desc">
                Marvel at the dramatic cliffs and hidden coves of the UNESCO Copper Coast Geopark, and tour the world-renowned House of Waterford Crystal.
              </p>
            </div>
            <div class="tour-footer">
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 12px; padding: 7px 14px;">
                Inquire on WhatsApp
              </a>
              <a href="tours.html#waterford" class="pillar-link">Learn More &rarr;</a>
            </div>
          </div>
        </div>

        <!-- Tour 3: Historic Youghal & Blackwater -->
        <div class="tour-card">
          <div class="tour-media">
            <img src="https://images.unsplash.com/photo-1590089415225-401ed6f9db8e?auto=format&fit=crop&q=80&w=800" alt="Historic Youghal Coastal Heritage">
            <span class="tour-badge">Base Spotlight</span>
          </div>
          <div class="tour-body">
            <div>
              <h3 class="tour-title">Historic Youghal &amp; Blackwater Valley</h3>
              <p class="tour-desc">
                Explore our hometown of Youghal with the famous Clock Gate Tower, St. Mary's Collegiate Church, pristine blue-flag beaches, and scenic Blackwater valley.
              </p>
            </div>
            <div class="tour-footer">
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 12px; padding: 7px 14px;">
                Inquire on WhatsApp
              </a>
              <a href="tours.html#youghal" class="pillar-link">Learn More &rarr;</a>
            </div>
          </div>
        </div>
      </div>

      <div style="text-align: center; margin-top: 36px;">
        <a href="tours.html" class="btn-outline">
          🗺️ View All Ireland Tours &amp; Custom Itineraries
        </a>
      </div>
    </div>
  </section>

  <!-- Generic Realistic Fleet Section (No fake luxury claims) -->
  <section class="section section-alt" id="fleet">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Clean &amp; Dependable Fleet</span>
        <h2 class="section-title">Comfortable Vehicles for Every Journey</h2>
        <p class="section-desc">
          Clean, valeted, smoke-free vehicles driven by licensed local professionals.
        </p>
      </div>

      <div class="fleet-grid">
        <!-- Fleet 1: Saloon Taxi -->
        <div class="fleet-card">
          <div class="fleet-media">
            <img src="https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&q=80&w=800" alt="Saloon Taxi">
          </div>
          <div class="fleet-body">
            <div>
              <div class="fleet-cat-badge">🚕 Everyday Comfort</div>
              <h3 class="fleet-name">Saloon Taxi</h3>
              <div class="fleet-meta-row">
                <span>👥 1–4 Passengers</span>
                <span>🧳 2 Large Bags</span>
                <span>❄️ Climate Control</span>
              </div>
              <p class="fleet-desc">
                Ideal for local Youghal errands, Cork Airport drop-offs, hospital appointments, and private point-to-point travel.
              </p>
            </div>
            <div style="margin-top: 14px;">
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="width: 100%; justify-content: center;">
                Book Saloon
              </a>
            </div>
          </div>
        </div>

        <!-- Fleet 2: MPV / People Carrier -->
        <div class="fleet-card" style="border-color: var(--border-gold);">
          <div class="fleet-media">
            <img src="https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?auto=format&fit=crop&q=80&w=800" alt="MPV People Carrier">
          </div>
          <div class="fleet-body">
            <div>
              <div class="fleet-cat-badge">🚐 Families &amp; Golfers</div>
              <h3 class="fleet-name">MPV / People Carrier</h3>
              <div class="fleet-meta-row">
                <span>👥 5–8 Passengers</span>
                <span>🧳 6–8 Large Bags</span>
                <span>⛳ Golf Clubs OK</span>
              </div>
              <p class="fleet-desc">
                High-capacity vehicle perfect for family airport journeys, golf outings, luggage-heavy trips, and scenic tours across Ireland.
              </p>
            </div>
            <div style="margin-top: 14px;">
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="width: 100%; justify-content: center;">
                Book MPV
              </a>
            </div>
          </div>
        </div>

        <!-- Fleet 3: Large Group Vehicle -->
        <div class="fleet-card">
          <div class="fleet-media">
            <img src="https://images.unsplash.com/photo-1570125909232-eb263c188f7e?auto=format&fit=crop&q=80&w=800" alt="Large Group Vehicle">
          </div>
          <div class="fleet-body">
            <div>
              <div class="fleet-cat-badge">🚌 Group Outings</div>
              <h3 class="fleet-name">Large Group Vehicle</h3>
              <div class="fleet-meta-row">
                <span>👥 Large Groups</span>
                <span>🧳 Ample Luggage</span>
                <span>✨ Private Hire</span>
              </div>
              <p class="fleet-desc">
                Comfortable, unified group travel for corporate events, wedding guest transfers, and customized extended Ireland tour parties.
              </p>
            </div>
            <div style="margin-top: 14px;">
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="width: 100%; justify-content: center;">
                Inquire Group
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 4-Step Reference Process (LusiDriver Inspiration) -->
  <section class="section">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">How It Works</span>
        <h2 class="section-title">Straightforward &amp; Stress-Free</h2>
        <p class="section-desc">Booking your taxi, airport transfer, or Ireland tour is quick and transparent.</p>
      </div>

      <div class="steps-grid">
        <div class="step-box">
          <div class="step-num">01</div>
          <h3 class="step-title">Send Details</h3>
          <p class="step-desc">Tell us your pickup location, destination, date, and passenger count via WhatsApp or direct phone call.</p>
        </div>

        <div class="step-box">
          <div class="step-num">02</div>
          <h3 class="step-title">Get Quote</h3>
          <p class="step-desc">We give you a prompt, transparent price quote with zero hidden surcharges or surprise extras.</p>
        </div>

        <div class="step-box">
          <div class="step-num">03</div>
          <h3 class="step-title">Driver Dispatched</h3>
          <p class="step-desc">Your driver arrives on time at your door, hotel lobby, or inside the airport arrivals terminal.</p>
        </div>

        <div class="step-box">
          <div class="step-num">04</div>
          <h3 class="step-title">Travel in Comfort</h3>
          <p class="step-desc">Relax and enjoy a safe, smooth journey. Pay easily with contactless card, cash, or mobile payment.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Service Areas Spotlight -->
  <section class="section section-alt" id="areas">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Service Coverage</span>
        <h2 class="section-title">Where We Operate</h2>
        <p class="section-desc">Based in Youghal with regional coverage across Cork, Waterford, Dungarvan, and nationwide tours.</p>
      </div>

      <div class="areas-grid">
        <!-- Base: Youghal -->
        <div class="area-box is-base">
          <div class="area-box-tag">⭐ Primary Base Location</div>
          <h3 class="area-box-name">Youghal, County Cork</h3>
          <p class="area-box-desc">
            Our home base at Upper Cork Hill. Immediate local taxi dispatch for Youghal, Killeagh, Castlemartyr, Redbarn, and surrounding coastal parishes.
          </p>
          <a href="service-areas.html#youghal" class="pillar-link">Youghal Taxi Details &rarr;</a>
        </div>

        <!-- Cork -->
        <div class="area-box">
          <div class="area-box-tag">✈️ High Priority Connection</div>
          <h3 class="area-box-name">Cork City &amp; Airport (ORK)</h3>
          <p class="area-box-desc">
            Frequent daily airport transfers, hospital runs (CUH, Mercy), Kent Train Station connections, and city center pickups.
          </p>
          <a href="service-areas.html#cork" class="pillar-link">Cork Transfers &rarr;</a>
        </div>

        <!-- Waterford -->
        <div class="area-box">
          <div class="area-box-tag">💎 Regional Priority</div>
          <h3 class="area-box-name">Waterford City &amp; County</h3>
          <p class="area-box-desc">
            Connections between Youghal, University Hospital Waterford, Waterford City center, Plunkett Station, and House of Waterford Crystal.
          </p>
          <a href="service-areas.html#waterford" class="pillar-link">Waterford Runs &rarr;</a>
        </div>

        <!-- Dungarvan -->
        <div class="area-box">
          <div class="area-box-tag">⛵ Coastal Hub</div>
          <h3 class="area-box-name">Dungarvan &amp; West Waterford</h3>
          <p class="area-box-desc">
            Fast 25-minute connection along the N25. Serving Waterford Greenway cyclists, Clonea Strand, Dungarvan Harbour, and golf links.
          </p>
          <a href="service-areas.html#dungarvan" class="pillar-link">Dungarvan Taxi &rarr;</a>
        </div>

        <!-- County Cork -->
        <div class="area-box">
          <div class="area-box-tag">🏡 East &amp; Mid Cork</div>
          <h3 class="area-box-name">County Cork Region</h3>
          <p class="area-box-desc">
            Serving Midleton, Cobh, Carrigtwohill, Fota Island, and connecting rural communities across County Cork.
          </p>
          <a href="service-areas.html#co-cork" class="pillar-link">County Cork Coverage &rarr;</a>
        </div>

        <!-- Ireland Tours -->
        <div class="area-box">
          <div class="area-box-tag">🗺️ Nationwide</div>
          <h3 class="area-box-name">Tours Across Ireland</h3>
          <p class="area-box-desc">
            Day tours and scenic multi-stop private itineraries anywhere in Ireland — Ring of Kerry, Dingle, Cliffs of Moher, Dublin, and beyond.
          </p>
          <a href="tours.html" class="pillar-link">Explore Tour Options &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Section (Clean & Informative, No VAT mentions) -->
  <section class="section" id="faq">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Frequently Asked Questions</span>
        <h2 class="section-title">Helpful Answers For Your Trip</h2>
        <p class="section-desc">Clear information on bookings, airport meet and greets, tours, and payments.</p>
      </div>

      <div class="faq-list">
        <div class="faq-card">
          <button class="faq-trigger" onclick="toggleFaqItem(this)">
            <span>📍 Where is Umair Taxi and Limo based?</span>
            <span class="faq-icon">&#9662;</span>
          </button>
          <div class="faq-content">
            We are proudly based at <strong>Istanbul Bites, Upper Cork Hill, Youghal, Ireland</strong>. From here, we serve Youghal, Dungarvan, Midleton, Cork City, Cork Airport (ORK), Waterford, and destinations nationwide across Ireland.
          </div>
        </div>

        <div class="faq-card">
          <button class="faq-trigger" onclick="toggleFaqItem(this)">
            <span>✈️ How do airport pickups work at Cork Airport?</span>
            <span class="faq-icon">&#9662;</span>
          </button>
          <div class="faq-content">
            For airport transfers, we monitor your flight number in real time. Even if your flight is early or delayed, your driver will be waiting inside the terminal arrivals hall holding a sign with your name, ready to help you with your luggage.
          </div>
        </div>

        <div class="faq-card">
          <button class="faq-trigger" onclick="toggleFaqItem(this)">
            <span>💬 How do I book a taxi or airport transfer?</span>
            <span class="faq-icon">&#9662;</span>
          </button>
          <div class="faq-content">
            The easiest way is to message us on WhatsApp at <strong>089 264 6246</strong> or call us directly. We will confirm your pickup time, destination, and fare quote immediately.
          </div>
        </div>

        <div class="faq-card">
          <button class="faq-trigger" onclick="toggleFaqItem(this)">
            <span>🗺️ Can we customize our Ireland day tour itinerary?</span>
            <span class="faq-icon">&#9662;</span>
          </button>
          <div class="faq-content">
            Absolutely! You have exclusive hire of the vehicle and your local driver. You can follow our recommended scenic routes (Blarney, Copper Coast, Kinsale, Ring of Kerry) or design your own stops, lunch spots, and photo pauses at your own leisure.
          </div>
        </div>

        <div class="faq-card">
          <button class="faq-trigger" onclick="toggleFaqItem(this)">
            <span>💳 What payment methods do you accept?</span>
            <span class="faq-icon">&#9662;</span>
          </button>
          <div class="faq-content">
            We accept all major debit/credit cards (Visa, Mastercard, Revolut), contactless phone payments, and cash in vehicle upon arrival.
          </div>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(build_index())

print("index.html written successfully.")
