import os
from build_full_website import (
    BRAND_NAME, BASE_LOCATION, ADDRESS,
    EMAIL, PHONE, PHONE_TEL, WHATSAPP_LINK,
    get_header, get_footer
)

# -----------------------------------------------------------------------------
# 1. FAQ PAGE (faq.html)
# -----------------------------------------------------------------------------
def build_faq_page():
    header = get_header(depth=0)
    footer = get_footer(depth=0)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Frequently Asked Questions · Umair Taxi and Limo Youghal</title>
  <meta name="description" content="Answers to common questions about our Youghal taxi dispatch, Cork Airport transfers, Ireland day tours, bookings, and payments. Call 089 264 6246.">
  <link rel="icon" type="image/svg+xml" href="assets/logo/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

{header}

  <section class="section" style="padding-top: 50px;">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Help &amp; Answers</span>
        <h1 class="section-title">Frequently Asked Questions</h1>
        <p class="section-desc">
          Everything you need to know about our taxi service, airport transfers, and private tours around Ireland.
        </p>
      </div>

      <div class="faq-list">
        <!-- Airport Transfers -->
        <div class="faq-card">
          <button class="faq-trigger" onclick="toggleFaqItem(this)">
            <span>✈️ Where does my driver meet me at Cork Airport?</span>
            <span class="faq-icon">&#9662;</span>
          </button>
          <div class="faq-content">
            Your driver meets you directly inside the terminal arrivals hall past the luggage carousel exit. Your driver will hold a nameboard and assist with your luggage.
          </div>
        </div>

        <div class="faq-card">
          <button class="faq-trigger" onclick="toggleFaqItem(this)">
            <span>📡 What if my flight is delayed or lands early?</span>
            <span class="faq-icon">&#9662;</span>
          </button>
          <div class="faq-content">
            We monitor your flight in real time using your flight number. Whether your flight lands early or gets delayed, we track it and will be waiting when you arrive.
          </div>
        </div>

        <!-- Local Taxi -->
        <div class="faq-card">
          <button class="faq-trigger" onclick="toggleFaqItem(this)">
            <span>🚕 Where is your local taxi service based?</span>
            <span class="faq-icon">&#9662;</span>
          </button>
          <div class="faq-content">
            We are based at <strong>Istanbul Bites, Upper Cork Hill, Youghal, Ireland</strong>. We cover Youghal town, Killeagh, Castlemartyr, Midleton, Dungarvan, and surrounding rural locations.
          </div>
        </div>

        <div class="faq-card">
          <button class="faq-trigger" onclick="toggleFaqItem(this)">
            <span>💬 How do I book a local taxi or airport transfer?</span>
            <span class="faq-icon">&#9662;</span>
          </button>
          <div class="faq-content">
            You can message us directly on WhatsApp at <strong>089 264 6246</strong> or call us. We confirm your pickup time, destination, and fare quote right away.
          </div>
        </div>

        <!-- Tours -->
        <div class="faq-card">
          <button class="faq-trigger" onclick="toggleFaqItem(this)">
            <span>🗺️ How do private Ireland tours work?</span>
            <span class="faq-icon">&#9662;</span>
          </button>
          <div class="faq-content">
            You have exclusive private hire of the vehicle and an experienced local driver. We provide scenic itineraries (Blarney Castle, Copper Coast, Ring of Kerry, Dungarvan Greenway, Historic Youghal) or you can customize your own stops.
          </div>
        </div>

        <!-- Payments -->
        <div class="faq-card">
          <button class="faq-trigger" onclick="toggleFaqItem(this)">
            <span>💳 What payment methods are accepted?</span>
            <span class="faq-icon">&#9662;</span>
          </button>
          <div class="faq-content">
            We accept all major debit/credit cards (Visa, Mastercard, Revolut), contactless mobile payments, and cash in vehicle.
          </div>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

# -----------------------------------------------------------------------------
# 2. HOW IT WORKS PAGE (how-it-works.html)
# -----------------------------------------------------------------------------
def build_how_it_works_page():
    header = get_header(depth=0)
    footer = get_footer(depth=0)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>How It Works · 4 Easy Steps | Umair Taxi and Limo</title>
  <meta name="description" content="Booking your taxi, airport transfer, or Ireland tour is simple and stress-free. Send details, receive quick quote, get picked up on time. Call 089 264 6246.">
  <link rel="icon" type="image/svg+xml" href="assets/logo/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

{header}

  <section class="section" style="padding-top: 50px;">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Simple &amp; Reliable Process</span>
        <h1 class="section-title">How It Works</h1>
        <p class="section-desc">
          We take the stress out of travel. Follow our 4 simple steps to arrange your taxi, airport transfer, or Ireland tour.
        </p>
      </div>

      <div class="steps-grid" style="margin-bottom: 50px;">
        <div class="step-box">
          <div class="step-num">01</div>
          <h2 class="step-title">Send Details</h2>
          <p class="step-desc">
            Provide your pickup address, destination, date, time, and passenger count via WhatsApp (<strong>089 264 6246</strong>) or phone call.
          </p>
        </div>

        <div class="step-box">
          <div class="step-num">02</div>
          <h2 class="step-title">Get Guaranteed Quote</h2>
          <p class="step-desc">
            We confirm our availability and supply a clear, honest quote with zero hidden surcharges or surprise tolls.
          </p>
        </div>

        <div class="step-box">
          <div class="step-num">03</div>
          <h2 class="step-title">Driver Dispatched</h2>
          <p class="step-desc">
            Your licensed driver arrives on time at your door or inside the airport arrivals terminal holding a greeting sign.
          </p>
        </div>

        <div class="step-box">
          <div class="step-num">04</div>
          <h2 class="step-title">Travel in Comfort</h2>
          <p class="step-desc">
            Sit back in a clean, valeted vehicle. Pay smoothly upon arrival using card, contactless phone, or cash.
          </p>
        </div>
      </div>

      <div style="text-align: center;">
        <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold">
          💬 Book on WhatsApp Now
        </a>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

# -----------------------------------------------------------------------------
# 3. RATES / FARE GUIDE PAGE (rates.html)
# -----------------------------------------------------------------------------
def build_rates_page():
    header = get_header(depth=0)
    footer = get_footer(depth=0)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fare Estimates &amp; Route Inquiries | Umair Taxi and Limo</title>
  <meta name="description" content="Inquire about honest, transparent fares for Youghal local taxi, Cork Airport transfers, and Ireland tours. No hidden surcharges. Call 089 264 6246.">
  <link rel="icon" type="image/svg+xml" href="assets/logo/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

{header}

  <section class="section" style="padding-top: 50px;">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Honest &amp; Upfront</span>
        <h1 class="section-title">Fare Estimates &amp; Route Quotes</h1>
        <p class="section-desc">
          We believe in complete pricing transparency. Because every trip varies by exact location, passenger luggage, and timing, we provide rapid, custom guaranteed quotes via WhatsApp.
        </p>
      </div>

      <!-- Quick Trip Enquiry Form -->
      <div class="enquiry-card-wrapper" style="margin-bottom: 50px;">
        <div class="enquiry-card-header">
          <div class="enquiry-card-title">
            <span>💶</span>
            <span>Get an Exact Fare Quote</span>
          </div>
          <div class="enquiry-card-subtitle">
            Direct &bull; Fast &bull; Guaranteed
          </div>
        </div>

        <form onsubmit="sendEnquiryWhatsApp(event)">
          <div class="enquiry-grid">
            <div class="form-field">
              <label for="enqPickup" class="field-label">📍 Pickup</label>
              <input type="text" id="enqPickup" class="field-control" placeholder="e.g. Youghal / Dungarvan" required>
            </div>
            <div class="form-field">
              <label for="enqDropoff" class="field-label">🏁 Destination</label>
              <input type="text" id="enqDropoff" class="field-control" placeholder="e.g. Cork Airport / Dublin" required>
            </div>
            <div class="form-field">
              <label for="enqDate" class="field-label">📅 Date &amp; Time</label>
              <input type="text" id="enqDate" class="field-control" placeholder="e.g. Today / 28 Nov">
            </div>
            <div class="form-field">
              <label for="enqPax" class="field-label">👥 Passengers</label>
              <select id="enqPax" class="field-control">
                <option value="1-4 Saloon">1–4 Passengers (Saloon)</option>
                <option value="5-8 MPV">5–8 Passengers (MPV)</option>
                <option value="Group 8+">Group 8+ (Large Vehicle)</option>
              </select>
            </div>
          </div>

          <div class="enquiry-actions">
            <span class="enquiry-note">
              ✅ All quotes include road tolls &amp; waiting time &bull; Zero surprise extras
            </span>
            <button type="submit" class="btn-gold" style="border: none; cursor: pointer;">
              Inquire Quote on WhatsApp
            </button>
          </div>
        </form>
      </div>

      <!-- Popular Route Guidelines (Estimated travel times) -->
      <div class="section-head">
        <span class="section-tag">Key Routes</span>
        <h2 class="section-title">Popular Journey Times from Youghal Base</h2>
      </div>

      <div class="pillars-grid">
        <div class="pillar-card">
          <div>
            <div class="pillar-badge">✈️</div>
            <h3 class="pillar-title">Youghal &harr; Cork Airport (ORK)</h3>
            <p class="pillar-desc">
              ~54 km &bull; Approx. 45–50 minutes via N25. Direct terminal pickup and drop-off.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Get Quote
          </a>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🏙️</div>
            <h3 class="pillar-title">Youghal &harr; Cork City Centre</h3>
            <p class="pillar-desc">
              ~48 km &bull; Approx. 40 minutes via N25. Ideal for shopping, hospital visits &amp; rail links.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Get Quote
          </a>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">⛵</div>
            <h3 class="pillar-title">Youghal &harr; Dungarvan</h3>
            <p class="pillar-desc">
              ~28 km &bull; Approx. 25 minutes along the scenic coast. Waterford Greenway connections.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Get Quote
          </a>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

# -----------------------------------------------------------------------------
# 4. REDIRECT WRAPPERS FOR OLD SERVICE URLS
# -----------------------------------------------------------------------------
def make_redirect_page(target_url, title):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url={target_url}">
  <title>Redirecting to {title} | Umair Taxi and Limo</title>
  <link rel="canonical" href="{target_url}">
</head>
<body style="background: #080808; color: #FFF; font-family: sans-serif; text-align: center; padding: 60px 20px;">
  <h2>Redirecting to {title}...</h2>
  <p>If you are not redirected automatically, <a href="{target_url}" style="color: #C5A059;">click here</a>.</p>
</body>
</html>"""

# Write files
with open("faq.html", "w", encoding="utf-8") as f:
    f.write(build_faq_page())
print("faq.html written.")

with open("how-it-works.html", "w", encoding="utf-8") as f:
    f.write(build_how_it_works_page())
print("how-it-works.html written.")

with open("rates.html", "w", encoding="utf-8") as f:
    f.write(build_rates_page())
print("rates.html written.")

# Redirect legacy service files to new canonical URLs
legacy_redirects = [
    ("services/hotel-golf-transfers.html", "golf-tours.html", "Golf Tours"),
    ("services/corporate-chauffeur.html", "corporate-travel.html", "Corporate Travel"),
    ("services/city-to-city.html", "local-taxi.html", "Local Taxi"),
    ("services/ireland-tours.html", "../tours.html", "Tours Across Ireland")
]

for file_path, target_url, title in legacy_redirects:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(make_redirect_page(target_url, title))
    print(f"{file_path} redirected to {target_url}.")

print("All remaining pages updated successfully.")

