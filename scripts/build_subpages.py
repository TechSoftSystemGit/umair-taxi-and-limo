import os
import sys

# Import constants and components
from build_full_website import (
    BRAND_NAME, BRAND_TAGLINE, BASE_LOCATION, ADDRESS,
    EMAIL, PHONE, PHONE_TEL, WHATSAPP_LINK,
    get_header, get_footer
)

# -----------------------------------------------------------------------------
# 2. SERVICES OVERVIEW PAGE (services.html)
# -----------------------------------------------------------------------------
def build_services_page():
    header = get_header(depth=0)
    footer = get_footer(depth=0)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Transport Services · Airport Transfers, Local Taxi, Tours | Umair Taxi and Limo</title>
  <meta name="description" content="Explore our transport services: Cork &amp; Dublin Airport Transfers, Youghal Local Taxi, Ireland Tours, Golf Transfers, Corporate Travel, Hospital Runs, and Aircoach connections.">
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
        <span class="section-tag">Complete Service Portfolio</span>
        <h1 class="section-title">Our Transport Services</h1>
        <p class="section-desc">
          Based in <strong>Youghal, County Cork</strong>, we provide prompt, reliable passenger transportation across County Cork, Waterford, Dungarvan, and nationwide Ireland touring.
        </p>
      </div>

      <!-- Core 3 Services -->
      <div class="pillars-grid" style="margin-bottom: 40px;">
        <div class="pillar-card">
          <div>
            <div class="pillar-badge">✈️</div>
            <h2 class="pillar-title">Airport Transfers (Primary)</h2>
            <p class="pillar-desc">
              Punctual door-to-door airport runs to Cork Airport (ORK), Dublin Airport (DUB), and Shannon Airport. Live flight tracking, inside terminal meet &amp; greet, and luggage assistance.
            </p>
          </div>
          <div>
            <a href="services/airport-transfers.html" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
              Airport Details &rarr;
            </a>
          </div>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🚕</div>
            <h2 class="pillar-title">Local Taxi Service</h2>
            <p class="pillar-desc">
              Fast, friendly local taxi service based in Youghal. Covering Youghal town, Killeagh, Castlemartyr, Dungarvan, Midleton, train stations, medical appointments, and nights out.
            </p>
          </div>
          <div>
            <a href="services/local-taxi.html" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
              Local Taxi Details &rarr;
            </a>
          </div>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🗺️</div>
            <h2 class="pillar-title">Tours Across Ireland</h2>
            <p class="pillar-desc">
              Bespoke private day tours and multi-day sightseeing across Ireland. Discover Blarney Castle, Ring of Kerry, Waterford Crystal, Copper Coast, and scenic coastal treasures.
            </p>
          </div>
          <div>
            <a href="tours.html" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
              Explore Tours &rarr;
            </a>
          </div>
        </div>
      </div>

      <!-- 4 Supporting Services -->
      <div class="section-head" style="margin-top: 60px;">
        <span class="section-tag">Specialized Transport</span>
        <h2 class="section-title">Supporting Travel Services</h2>
      </div>

      <div class="services-4grid">
        <div class="service-box">
          <div class="service-emoji">⛳</div>
          <h3 class="service-box-title">Golf Tours</h3>
          <p class="service-box-desc">
            Comfortable transport with spacious room for golf bags to Old Head of Kinsale, Castlemartyr, Fota Island, Dungarvan Golf Club, and Waterford Castle.
          </p>
          <a href="services/golf-tours.html" class="pillar-link">Learn More &rarr;</a>
        </div>

        <div class="service-box">
          <div class="service-emoji">💼</div>
          <h3 class="service-box-title">Corporate Travel &amp; Events</h3>
          <p class="service-box-desc">
            Discreet, dependable travel for company executives, visiting clients, conference delegates, and corporate dinner transfers.
          </p>
          <a href="services/corporate-travel.html" class="pillar-link">Learn More &rarr;</a>
        </div>

        <div class="service-box">
          <div class="service-emoji">🏥</div>
          <h3 class="service-box-title">Hospital Runs</h3>
          <p class="service-box-desc">
            Gentle, punctual, and caring transport to Cork University Hospital (CUH), Mercy Hospital, South Infirmary, and University Hospital Waterford.
          </p>
          <a href="services/hospital-runs.html" class="pillar-link">Learn More &rarr;</a>
        </div>

        <div class="service-box">
          <div class="service-emoji">🚌</div>
          <h3 class="service-box-title">Aircoach &amp; Station Runs</h3>
          <p class="service-box-desc">
            Direct connections to Aircoach stops, Kent Train Station (Cork), Plunkett Station (Waterford), and ferry ports.
          </p>
          <a href="services/aircoach-transfers.html" class="pillar-link">Learn More &rarr;</a>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

# -----------------------------------------------------------------------------
# 3. AIRPORT TRANSFERS PAGE (services/airport-transfers.html)
# -----------------------------------------------------------------------------
def build_airport_transfers_page():
    header = get_header(depth=1)
    footer = get_footer(depth=1)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cork &amp; Dublin Airport Transfers · Youghal, Dungarvan, Waterford | Umair Taxi and Limo</title>
  <meta name="description" content="Primary airport transfer service based in Youghal. Dedicated transfers to Cork Airport (ORK), Dublin Airport (DUB), and Shannon. Flight tracking and terminal meet &amp; greet. Call 089 264 6246.">
  <link rel="icon" type="image/svg+xml" href="../assets/logo/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>

{header}

  <section class="section" style="padding-top: 50px;">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Primary Business Service</span>
        <h1 class="section-title">Airport Transfers Ireland</h1>
        <p class="section-desc">
          Stress-free, dependable transfers connecting <strong>Youghal, Cork, Dungarvan, and Waterford</strong> directly to all major Irish airport terminals.
        </p>
      </div>

      <!-- Quick Trip Enquiry Form -->
      <div class="enquiry-card-wrapper" style="margin: 0 auto 50px;">
        <div class="enquiry-card-header">
          <div class="enquiry-card-title">
            <span>✈️</span>
            <span>Request Airport Transfer Quote</span>
          </div>
          <div class="enquiry-card-subtitle">
            Instant WhatsApp Confirmation
          </div>
        </div>

        <form onsubmit="sendEnquiryWhatsApp(event)">
          <div class="enquiry-grid">
            <div class="form-field">
              <label for="enqPickup" class="field-label">📍 Pickup Location</label>
              <input type="text" id="enqPickup" class="field-control" placeholder="e.g. Youghal / Dungarvan / Hotel" required>
            </div>
            <div class="form-field">
              <label for="enqDropoff" class="field-label">🏁 Airport Terminal</label>
              <input type="text" id="enqDropoff" class="field-control" placeholder="e.g. Cork Airport (ORK) or Dublin" required>
            </div>
            <div class="form-field">
              <label for="enqDate" class="field-label">📅 Flight Date &amp; Time</label>
              <input type="text" id="enqDate" class="field-control" placeholder="e.g. 26 Nov, 08:30 (Flight EI 841)">
            </div>
            <div class="form-field">
              <label for="enqPax" class="field-label">👥 Passengers &amp; Bags</label>
              <select id="enqPax" class="field-control">
                <option value="1-4 Passengers">1–4 Passengers (Saloon Taxi)</option>
                <option value="5-8 Passengers">5–8 Passengers (MPV / Van)</option>
                <option value="Golf Bags / Extra Luggage">Extra Luggage / Golf Bags</option>
              </select>
            </div>
          </div>

          <div class="enquiry-actions">
            <span class="enquiry-note">
              ✅ Real-time flight tracking &bull; Inside terminal meet &amp; greet &bull; Zero waiting anxiety
            </span>
            <button type="submit" class="btn-gold" style="border: none; cursor: pointer;">
              Get Quote on WhatsApp
            </button>
          </div>
        </form>
      </div>

      <!-- Key Airport Hubs Covered -->
      <div class="section-head">
        <span class="section-tag">Key Hubs</span>
        <h2 class="section-title">Airports We Cover</h2>
      </div>

      <div class="pillars-grid" style="margin-bottom: 50px;">
        <div class="pillar-card">
          <div>
            <div class="pillar-badge">✈️</div>
            <h3 class="pillar-title">Cork Airport (ORK)</h3>
            <p class="pillar-desc">
              Our closest international airport, just 45 minutes from our Youghal base. Rapid dispatch for incoming European and UK flights, holidaymakers, and business travelers.
            </p>
          </div>
          <div>
            <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
              Book Cork Airport Run
            </a>
          </div>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🛫</div>
            <h3 class="pillar-title">Dublin Airport (DUB)</h3>
            <p class="pillar-desc">
              Long-distance airport transfers between County Cork / Waterford and Dublin Airport Terminal 1 &amp; Terminal 2. Avoid bus timetables and train connections.
            </p>
          </div>
          <div>
            <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
              Inquire Dublin Airport
            </a>
          </div>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🛬</div>
            <h3 class="pillar-title">Shannon Airport (SNN)</h3>
            <p class="pillar-desc">
              Direct point-to-point connections for transatlantic flights arriving into Shannon, serving travelers staying in East Cork, Waterford, and the South of Ireland.
            </p>
          </div>
          <div>
            <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
              Inquire Shannon Airport
            </a>
          </div>
        </div>
      </div>

      <!-- What Sets Our Airport Transfer Apart -->
      <div class="services-4grid">
        <div class="service-box">
          <div class="service-emoji">📡</div>
          <h3 class="service-box-title">Flight Tracking</h3>
          <p class="service-box-desc">
            We monitor your inbound flight in real time. If your plane arrives early or is delayed, your pickup time is automatically adjusted.
          </p>
        </div>

        <div class="service-box">
          <div class="service-emoji">🤝</div>
          <h3 class="service-box-title">Terminal Meet &amp; Greet</h3>
          <p class="service-box-desc">
            Your friendly driver greets you directly inside the arrivals hall holding a sign with your name, ready to assist with luggage.
          </p>
        </div>

        <div class="service-box">
          <div class="service-emoji">⏱️</div>
          <h3 class="service-box-title">Complimentary Waiting</h3>
          <p class="service-box-desc">
            Enjoy generous complimentary waiting time for passport control and baggage claim so you never have to rush.
          </p>
        </div>

        <div class="service-box">
          <div class="service-emoji">🛡️</div>
          <h3 class="service-box-title">Fixed Quoted Fares</h3>
          <p class="service-box-desc">
            The price agreed is the price you pay. All road tolls and parking charges are fully explained upfront.
          </p>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

# -----------------------------------------------------------------------------
# 4. LOCAL TAXI PAGE (services/local-taxi.html)
# -----------------------------------------------------------------------------
def build_local_taxi_page():
    header = get_header(depth=1)
    footer = get_footer(depth=1)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Local Taxi Service Youghal &amp; Surrounds | Umair Taxi and Limo</title>
  <meta name="description" content="Dependable 24/7 local taxi service based in Youghal, Co. Cork. Serving Youghal, Killeagh, Castlemartyr, Dungarvan, Midleton &amp; Cork. Fast local dispatch. Call 089 264 6246.">
  <link rel="icon" type="image/svg+xml" href="../assets/logo/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>

{header}

  <section class="section" style="padding-top: 50px;">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Local Youghal Community</span>
        <h1 class="section-title">Local Taxi Service</h1>
        <p class="section-desc">
          Proudly operating from <strong>Istanbul Bites, Upper Cork Hill, Youghal</strong>. Providing fast, friendly local taxi dispatch across Youghal and neighboring East Cork &amp; West Waterford towns.
        </p>
      </div>

      <div class="pillars-grid" style="margin-bottom: 50px;">
        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🚕</div>
            <h3 class="pillar-title">Youghal Town &amp; Beaches</h3>
            <p class="pillar-desc">
              Quick pickups across Youghal town center, Front Strand, Claycastle, Redbarn Beach, supermarkets, and local residences.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Call / WhatsApp Taxi
          </a>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🏡</div>
            <h3 class="pillar-title">East Cork Towns</h3>
            <p class="pillar-desc">
              Frequent taxi runs to Killeagh, Castlemartyr Resort, Midleton, Ballycotton, and surrounding rural communities.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Book East Cork Ride
          </a>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">⛵</div>
            <h3 class="pillar-title">Dungarvan &amp; West Waterford</h3>
            <p class="pillar-desc">
              Direct connection along the N25 to Dungarvan, Ardmore, Clashmore, and the Waterford Greenway trailhead.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Book Dungarvan Ride
          </a>
        </div>
      </div>

      <!-- Common Local Use Cases -->
      <div class="section-head">
        <span class="section-tag">Everyday Mobility</span>
        <h2 class="section-title">When To Call Our Local Taxi</h2>
      </div>

      <div class="services-4grid">
        <div class="service-box">
          <div class="service-emoji">🍽️</div>
          <h3 class="service-box-title">Restaurants &amp; Nights Out</h3>
          <p class="service-box-desc">
            Safe, reliable journeys home from Youghal restaurants, pubs, and wedding receptions in Castlemartyr.
          </p>
        </div>

        <div class="service-box">
          <div class="service-emoji">🏥</div>
          <h3 class="service-box-title">Doctor &amp; Hospital Visits</h3>
          <p class="service-box-desc">
            Door-to-door assistance for GP appointments, healthcare clinics, and regional hospital consultations.
          </p>
        </div>

        <div class="service-box">
          <div class="service-emoji">🚆</div>
          <h3 class="service-box-title">Train &amp; Bus Stations</h3>
          <p class="service-box-desc">
            Transfers to Midleton Train Station, Kent Station (Cork), and regional express bus connection points.
          </p>
        </div>

        <div class="service-box">
          <div class="service-emoji">🛍️</div>
          <h3 class="service-box-title">Shopping &amp; Errand Trips</h3>
          <p class="service-box-desc">
            Courteous drivers happy to help with grocery bags, parcel pick-ups, and daily errands around town.
          </p>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

# -----------------------------------------------------------------------------
# 5. TOURS HUB PAGE (tours.html)
# -----------------------------------------------------------------------------
def build_tours_page():
    header = get_header(depth=0)
    footer = get_footer(depth=0)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Explore Ireland With Us · Private Taxi Tours | Umair Taxi and Limo</title>
  <meta name="description" content="Discover Ireland's most breathtaking scenic routes with Umair Taxi and Limo. Blarney Castle, Ring of Kerry, Waterford Crystal, Copper Coast, and custom private tours. Call 089 264 6246.">
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
        <span class="section-tag">Explore Ireland With Us</span>
        <h1 class="section-title">Private Tours All Around Ireland</h1>
        <p class="section-desc">
          Inspired by Ireland's top taxi tour itineraries. Enjoy the freedom of a private vehicle, local driver-guide, and flexible pacing.
        </p>
      </div>

      <div class="tours-grid">
        <!-- Tour 1: Cork & Blarney -->
        <div class="tour-card" id="cork">
          <div class="tour-media">
            <img src="https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&q=80&w=800" alt="Blarney Castle & Gardens">
            <span class="tour-badge">County Cork</span>
          </div>
          <div class="tour-body">
            <div>
              <h2 class="tour-title">Blarney Castle &amp; Cork Highlights</h2>
              <p class="tour-desc">
                Kiss the world-famous Blarney Stone to receive the gift of eloquence, stroll through the Poison Garden, explore Cork's bustling English Market, and take in the maritime beauty of Kinsale.
              </p>
            </div>
            <div class="tour-footer">
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
                Inquire on WhatsApp
              </a>
            </div>
          </div>
        </div>

        <!-- Tour 2: Waterford & Copper Coast -->
        <div class="tour-card" id="waterford">
          <div class="tour-media">
            <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&q=80&w=800" alt="Copper Coast UNESCO Geopark">
            <span class="tour-badge">Waterford</span>
          </div>
          <div class="tour-body">
            <div>
              <h2 class="tour-title">Waterford &amp; Copper Coast Tour</h2>
              <p class="tour-desc">
                Drive along Ireland's dramatic Copper Coast UNESCO Geopark, visit secluded sea caves, and discover master craftsmanship at the House of Waterford Crystal in Ireland's oldest city.
              </p>
            </div>
            <div class="tour-footer">
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
                Inquire on WhatsApp
              </a>
            </div>
          </div>
        </div>

        <!-- Tour 3: Historic Youghal -->
        <div class="tour-card" id="youghal">
          <div class="tour-media">
            <img src="https://images.unsplash.com/photo-1590089415225-401ed6f9db8e?auto=format&fit=crop&q=80&w=800" alt="Historic Youghal">
            <span class="tour-badge">Base Location</span>
          </div>
          <div class="tour-body">
            <div>
              <h2 class="tour-title">Historic Youghal &amp; Blackwater</h2>
              <p class="tour-desc">
                Experience our hometown: medieval town walls, the iconic 1777 Clock Gate Tower, Sir Walter Raleigh's Myrtle Grove, and the tranquil river vistas of the Blackwater Valley.
              </p>
            </div>
            <div class="tour-footer">
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
                Inquire on WhatsApp
              </a>
            </div>
          </div>
        </div>

        <!-- Tour 4: Dungarvan & Greenway -->
        <div class="tour-card" id="dungarvan">
          <div class="tour-media">
            <img src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&q=80&w=800" alt="Dungarvan Harbour">
            <span class="tour-badge">Waterford Greenway</span>
          </div>
          <div class="tour-body">
            <div>
              <h2 class="tour-title">Dungarvan &amp; Waterford Greenway</h2>
              <p class="tour-desc">
                Picturesque harbour views, Dungarvan Castle, coastal seafood spots, and drop-offs/pickups along the famous 46km off-road Waterford Greenway walking and cycling path.
              </p>
            </div>
            <div class="tour-footer">
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
                Inquire on WhatsApp
              </a>
            </div>
          </div>
        </div>

        <!-- Tour 5: West Cork Scenic -->
        <div class="tour-card" id="west-cork">
          <div class="tour-media">
            <img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&q=80&w=800" alt="West Cork Landscape">
            <span class="tour-badge">Wild Atlantic Way</span>
          </div>
          <div class="tour-body">
            <div>
              <h2 class="tour-title">West Cork &amp; Wild Atlantic Way</h2>
              <p class="tour-desc">
                Venture west to Clonakilty, Rosscarbery, Baltimore, and Bantry Bay. Rugged Atlantic coastline, charming colorful villages, and artisan food markets.
              </p>
            </div>
            <div class="tour-footer">
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
                Inquire on WhatsApp
              </a>
            </div>
          </div>
        </div>

        <!-- Tour 6: Custom Private Tour -->
        <div class="tour-card" id="custom" style="border-color: var(--border-gold);">
          <div class="tour-media">
            <img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&q=80&w=800" alt="Custom Ireland Tour">
            <span class="tour-badge">Tailored For You</span>
          </div>
          <div class="tour-body">
            <div>
              <h2 class="tour-title">Custom Private Tours Across Ireland</h2>
              <p class="tour-desc">
                Dreaming of the Ring of Kerry, Cliffs of Moher, Rock of Cashel, or Jameson Midleton Distillery? We build a tailored itinerary suited to your group's schedule and wishes.
              </p>
            </div>
            <div class="tour-footer">
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
                Build Custom Tour
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

# -----------------------------------------------------------------------------
# 6. SERVICE AREAS PAGE (service-areas.html)
# -----------------------------------------------------------------------------
def build_service_areas_page():
    header = get_header(depth=0)
    footer = get_footer(depth=0)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Service Areas · Youghal Base, Cork, Waterford, Dungarvan | Umair Taxi and Limo</title>
  <meta name="description" content="Discover our service areas: Base in Youghal, Co. Cork. Serving Cork Airport, Cork City, Waterford, Dungarvan, County Cork, and tours nationwide. Call 089 264 6246.">
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
        <span class="section-tag">Geographic Coverage</span>
        <h1 class="section-title">Our Service Areas</h1>
        <p class="section-desc">
          Strategically based at <strong>Istanbul Bites, Upper Cork Hill, Youghal</strong> on the Cork-Waterford border along the N25, providing prompt response across the entire South East and South of Ireland.
        </p>
      </div>

      <div class="areas-grid">
        <!-- Area 1: Youghal Base -->
        <div class="area-box is-base" id="youghal">
          <div class="area-box-tag">⭐ Primary Base Location</div>
          <h2 class="area-box-name">Youghal, County Cork</h2>
          <p class="area-box-desc">
            Our central operations hub. Instant taxi dispatch across Youghal town, Front Strand, Claycastle, Redbarn, Killeagh, and Castlemartyr.
          </p>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 12px; padding: 6px 14px;">
            Book Youghal Taxi
          </a>
        </div>

        <!-- Area 2: Cork City & Airport -->
        <div class="area-box" id="cork">
          <div class="area-box-tag">✈️ High Priority Hub</div>
          <h2 class="area-box-name">Cork City &amp; Airport (ORK)</h2>
          <p class="area-box-desc">
            Direct airport transfers, Kent Railway Station links, hospital visits (CUH, South Infirmary, Mercy), and point-to-point connections to Cork City center.
          </p>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 12px; padding: 6px 14px;">
            Book Cork Transfer
          </a>
        </div>

        <!-- Area 3: Waterford City & County -->
        <div class="area-box" id="waterford">
          <div class="area-box-tag">💎 Regional Priority</div>
          <h2 class="area-box-name">Waterford City &amp; County</h2>
          <p class="area-box-desc">
            Serving University Hospital Waterford, Waterford Institute of Technology, Plunkett Train Station, and Viking Triangle historic attractions.
          </p>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 12px; padding: 6px 14px;">
            Book Waterford Run
          </a>
        </div>

        <!-- Area 4: Dungarvan & Greenway -->
        <div class="area-box" id="dungarvan">
          <div class="area-box-tag">⛵ Coastal Hub</div>
          <h2 class="area-box-name">Dungarvan &amp; West Waterford</h2>
          <p class="area-box-desc">
            Only 25 minutes from Youghal. Transport for Waterford Greenway cyclists, Clonea Strand, Dungarvan Harbour, and Ardmore round tower.
          </p>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 12px; padding: 6px 14px;">
            Book Dungarvan Ride
          </a>
        </div>

        <!-- Area 5: County Cork -->
        <div class="area-box" id="co-cork">
          <div class="area-box-tag">🏡 East &amp; Mid Cork</div>
          <h2 class="area-box-name">County Cork Region</h2>
          <p class="area-box-desc">
            Connecting Midleton, Cobh Titanic Experience, Carrigtwohill, Fota Island Resort, and surrounding rural towns.
          </p>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 12px; padding: 6px 14px;">
            Inquire County Cork
          </a>
        </div>

        <!-- Area 6: West Waterford -->
        <div class="area-box" id="west-waterford">
          <div class="area-box-tag">🌿 West Waterford Region</div>
          <h2 class="area-box-name">West Waterford Region</h2>
          <p class="area-box-desc">
            Serving Clashmore, Villierstown, Cappoquin, Lismore Castle, and the picturesque Blackwater Valley routes.
          </p>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 12px; padding: 6px 14px;">
            Inquire West Waterford
          </a>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

# -----------------------------------------------------------------------------
# 7. FLEET PAGE (fleet.html)
# -----------------------------------------------------------------------------
def build_fleet_page():
    header = get_header(depth=0)
    footer = get_footer(depth=0)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Our Fleet · Clean, Comfortable Saloons &amp; MPVs | Umair Taxi and Limo</title>
  <meta name="description" content="Explore our vehicle fleet: Saloon Taxis for 1-4 passengers, spacious MPVs for 5-8 passengers and golf bags, and large group vehicles for Ireland tours. Call 089 264 6246.">
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
        <span class="section-tag">Comfort &amp; Reliability</span>
        <h1 class="section-title">Our Vehicle Fleet</h1>
        <p class="section-desc">
          Every vehicle in our fleet is fully licensed, insured, sanitized, and maintained to the highest safety standards by the National Transport Authority (NTA Ireland).
        </p>
      </div>

      <div class="fleet-grid">
        <!-- Fleet 1: Saloon Taxi -->
        <div class="fleet-card">
          <div class="fleet-media">
            <img src="https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&q=80&w=800" alt="Comfortable Saloon Taxi">
          </div>
          <div class="fleet-body">
            <div>
              <div class="fleet-cat-badge">🚕 Everyday Comfort</div>
              <h2 class="fleet-name">Saloon Taxi</h2>
              <div class="fleet-meta-row">
                <span>👥 1–4 Passengers</span>
                <span>🧳 2 Large Bags</span>
                <span>❄️ A/C Climate</span>
              </div>
              <p class="fleet-desc">
                Ideal for local Youghal errands, Cork Airport transfers, doctor consultations, train station drops, and individual business trips.
              </p>
            </div>
            <div>
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="width: 100%; justify-content: center;">
                Book Saloon Taxi
              </a>
            </div>
          </div>
        </div>

        <!-- Fleet 2: MPV / People Carrier -->
        <div class="fleet-card" style="border-color: var(--border-gold);">
          <div class="fleet-media">
            <img src="https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?auto=format&fit=crop&q=80&w=800" alt="Spacious Tour MPV">
          </div>
          <div class="fleet-body">
            <div>
              <div class="fleet-cat-badge">🚐 Families &amp; Golfers</div>
              <h2 class="fleet-name">MPV / People Carrier</h2>
              <div class="fleet-meta-row">
                <span>👥 5–8 Passengers</span>
                <span>🧳 6–8 Large Bags</span>
                <span>⛳ Golf Clubs OK</span>
              </div>
              <p class="fleet-desc">
                Spacious seating and huge luggage capacity. Perfect for family airport arrivals, golf luggage, and full-day private tours across Ireland.
              </p>
            </div>
            <div>
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="width: 100%; justify-content: center;">
                Book MPV
              </a>
            </div>
          </div>
        </div>

        <!-- Fleet 3: Large Group Vehicle -->
        <div class="fleet-card">
          <div class="fleet-media">
            <img src="https://images.unsplash.com/photo-1570125909232-eb263c188f7e?auto=format&fit=crop&q=80&w=800" alt="Group Vehicle">
          </div>
          <div class="fleet-body">
            <div>
              <div class="fleet-cat-badge">🚌 Group Transport</div>
              <h2 class="fleet-name">Large Group Vehicle</h2>
              <div class="fleet-meta-row">
                <span>👥 8+ Passengers</span>
                <span>🧳 Full Luggage</span>
                <span>✨ Dedicated Hire</span>
              </div>
              <p class="fleet-desc">
                Dedicated group transport for wedding parties, corporate events, family reunions, and extended multi-day Ireland tour itineraries.
              </p>
            </div>
            <div>
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="width: 100%; justify-content: center;">
                Inquire Group Hire
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

# -----------------------------------------------------------------------------
# 8. ABOUT PAGE (about.html)
# -----------------------------------------------------------------------------
def build_about_page():
    header = get_header(depth=0)
    footer = get_footer(depth=0)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About Us · Umair Taxi and Limo | Based in Youghal, Ireland</title>
  <meta name="description" content="Learn about Umair Taxi and Limo. Proudly based at Istanbul Bites, Upper Cork Hill, Youghal. Dependable airport transfers, local taxi, and private Ireland tours. Call 089 264 6246.">
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
        <span class="section-tag">Our Story &amp; Values</span>
        <h1 class="section-title">About Umair Taxi and Limo</h1>
        <p class="section-desc">
          Rooted in Youghal, serving County Cork, Waterford, and travelers from around the world.
        </p>
      </div>

      <div style="max-width: 820px; margin: 0 auto; line-height: 1.8; color: #D1D5DB; font-size: 15px;">
        <p style="margin-bottom: 20px;">
          <strong>Umair Taxi and Limo</strong> is a dedicated passenger transport service based at <strong>Istanbul Bites, Upper Cork Hill, Youghal, Ireland</strong>. We were founded on three simple principles: <em>absolute punctuality, honest communication, and genuine local courtesy</em>.
        </p>

        <p style="margin-bottom: 20px;">
          While our company name includes "Limo", our primary mission is being your most dependable <strong>Airport Transfer specialist</strong>, your prompt <strong>Local Taxi service</strong>, and your trusted guide for <strong>Private Tours across Ireland</strong>. We do not hide behind aloof luxury terminology or inflated tariffs — we offer clean, comfortable vehicles driven by licensed local professionals who know the roads and care about your journey.
        </p>

        <div class="pillars-grid" style="margin: 36px 0;">
          <div class="pillar-card">
            <div>
              <div class="pillar-badge">📍</div>
              <h3 class="pillar-title">Local Pride</h3>
              <p class="pillar-desc">
                Proud to call Youghal home. We serve our neighbors, local businesses, visitors, and hospital patients with genuine care.
              </p>
            </div>
          </div>

          <div class="pillar-card">
            <div>
              <div class="pillar-badge">🛡️</div>
              <h3 class="pillar-title">NTA Licensed</h3>
              <p class="pillar-desc">
                Fully compliant with National Transport Authority (NTA Ireland) standards, commercial passenger insurance, and vetted drivers.
              </p>
            </div>
          </div>

          <div class="pillar-card">
            <div>
              <div class="pillar-badge">💬</div>
              <h3 class="pillar-title">Direct Contact</h3>
              <p class="pillar-desc">
                No endless automated phone menus or faceless call centers. Speak directly with us on WhatsApp or phone at <strong>089 264 6246</strong>.
              </p>
            </div>
          </div>
        </div>

        <p style="text-align: center; margin-top: 30px;">
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold">
            💬 Contact Us on WhatsApp
          </a>
        </p>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

# -----------------------------------------------------------------------------
# 9. CONTACT PAGE (contact.html)
# -----------------------------------------------------------------------------
def build_contact_page():
    header = get_header(depth=0)
    footer = get_footer(depth=0)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Us · 089 264 6246 | Umair Taxi and Limo Youghal</title>
  <meta name="description" content="Contact Umair Taxi and Limo. Phone &amp; WhatsApp: 089 264 6246. Email: Rana4874@gmail.com. Address: Istanbul Bites, Upper Cork Hill, Youghal, Ireland. Fast response.">
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
        <span class="section-tag">Direct Communication</span>
        <h1 class="section-title">Get in Touch</h1>
        <p class="section-desc">
          Ready to book your taxi, airport transfer, or Ireland tour? Reach out directly via WhatsApp, phone, or email.
        </p>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px; max-width: 960px; margin: 0 auto;">
        <!-- Left: Verified Contact Details Card -->
        <div style="background: var(--bg-surface); border: 1px solid var(--border-gold); border-radius: var(--radius-md); padding: 32px 28px;">
          <h2 style="font-family: var(--font-serif); font-size: 22px; color: #FFF; margin-bottom: 20px;">
            Contact Details
          </h2>

          <div class="footer-contact-row" style="margin-bottom: 20px;">
            <span style="font-size: 22px;">📞</span>
            <div>
              <strong style="font-size: 14px;">Telephone:</strong><br>
              <a href="tel:{PHONE_TEL}" style="color: var(--gold-light); font-size: 16px; font-weight: 700;">{PHONE}</a>
            </div>
          </div>

          <div class="footer-contact-row" style="margin-bottom: 20px;">
            <span style="font-size: 22px;">💬</span>
            <div>
              <strong style="font-size: 14px;">WhatsApp (Instant Reply):</strong><br>
              <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" style="color: #25D366; font-size: 16px; font-weight: 700;">
                089 264 6246
              </a>
            </div>
          </div>

          <div class="footer-contact-row" style="margin-bottom: 20px;">
            <span style="font-size: 22px;">✉️</span>
            <div>
              <strong style="font-size: 14px;">Email:</strong><br>
              <a href="mailto:{EMAIL}" style="color: #FFF; font-size: 15px;">{EMAIL}</a>
            </div>
          </div>

          <div class="footer-contact-row" style="margin-bottom: 20px;">
            <span style="font-size: 22px;">📍</span>
            <div>
              <strong style="font-size: 14px;">Operating Base:</strong><br>
              <span style="color: #D1D5DB; font-size: 14px;">
                {ADDRESS}
              </span>
            </div>
          </div>

          <div style="margin-top: 28px; padding-top: 18px; border-top: 1px solid var(--border-subtle); font-size: 12.5px; color: var(--text-muted);">
            ✅ Available for pre-booked airport runs, local dispatch, and nationwide tours.
          </div>
        </div>

        <!-- Right: Message Form -->
        <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 32px 28px;">
          <h2 style="font-family: var(--font-serif); font-size: 22px; color: #FFF; margin-bottom: 16px;">
            Send a Booking Message
          </h2>

          <form onsubmit="sendEnquiryWhatsApp(event)">
            <div class="form-field" style="margin-bottom: 14px;">
              <label for="enqPickup" class="field-label">📍 Pickup Location</label>
              <input type="text" id="enqPickup" class="field-control" placeholder="e.g. Youghal, Cork Airport, Dungarvan" required>
            </div>

            <div class="form-field" style="margin-bottom: 14px;">
              <label for="enqDropoff" class="field-label">🏁 Destination</label>
              <input type="text" id="enqDropoff" class="field-control" placeholder="e.g. Cork Airport, Dublin, Hotel" required>
            </div>

            <div class="form-field" style="margin-bottom: 14px;">
              <label for="enqDate" class="field-label">📅 Date &amp; Time</label>
              <input type="text" id="enqDate" class="field-control" placeholder="e.g. Tomorrow 10:00 AM">
            </div>

            <div class="form-field" style="margin-bottom: 20px;">
              <label for="enqPax" class="field-label">👥 Passenger Details</label>
              <select id="enqPax" class="field-control">
                <option value="1-4 Passengers">1–4 Passengers (Saloon Taxi)</option>
                <option value="5-8 Passengers">5–8 Passengers (Tour MPV)</option>
                <option value="Golf Tour / Bulky Bags">Golf Tour / Bulky Luggage</option>
              </select>
            </div>

            <button type="submit" class="btn-gold" style="width: 100%; justify-content: center; border: none; cursor: pointer; padding: 12px;">
              💬 Send Details on WhatsApp
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

# -----------------------------------------------------------------------------
# 10. SUPPORTING SERVICE PAGES: Golf, Corporate, Hospital, Aircoach
# -----------------------------------------------------------------------------
def build_golf_tours_page():
    header = get_header(depth=1)
    footer = get_footer(depth=1)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Golf Tours &amp; Resort Transfers | Umair Taxi and Limo</title>
  <meta name="description" content="Dedicated golf course transfers across South &amp; East Ireland. Old Head of Kinsale, Castlemartyr Resort, Fota Island, Dungarvan Golf Club. Spacious vehicles for golf bags. Call 089 264 6246.">
  <link rel="icon" type="image/svg+xml" href="../assets/logo/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>

{header}

  <section class="section" style="padding-top: 50px;">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Championship Golf Transport</span>
        <h1 class="section-title">Golf Tours &amp; Transfers</h1>
        <p class="section-desc">
          Comfortable travel with spacious luggage capacity for golf bags and travel cases across Ireland's premier links and parkland courses.
        </p>
      </div>

      <div class="pillars-grid" style="margin-bottom: 40px;">
        <div class="pillar-card">
          <div>
            <div class="pillar-badge">⛳</div>
            <h2 class="pillar-title">Old Head of Kinsale</h2>
            <p class="pillar-desc">
              World-renowned cliff-top links course. Relax on the journey and let us handle golf equipment transport.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Book Old Head Run
          </a>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">⛳</div>
            <h2 class="pillar-title">Castlemartyr &amp; Fota Island</h2>
            <p class="pillar-desc">
              Minutes from our Youghal base. Direct resort and course transfers for hotel guests and golf groups.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Book Resort Run
          </a>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">⛳</div>
            <h2 class="pillar-title">Dungarvan &amp; Waterford Castle</h2>
            <p class="pillar-desc">
              Top coastal golfing along West Waterford and Ireland's only island golf resort in Waterford.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Book Waterford Golf
          </a>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

def build_corporate_travel_page():
    header = get_header(depth=1)
    footer = get_footer(depth=1)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Corporate Events &amp; Business Travel | Umair Taxi and Limo</title>
  <meta name="description" content="Dependable corporate travel and event transfers in Cork, Waterford, and Youghal. Punctual, discreet, invoice-ready transportation. Call 089 264 6246.">
  <link rel="icon" type="image/svg+xml" href="../assets/logo/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>

{header}

  <section class="section" style="padding-top: 50px;">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Professional Transportation</span>
        <h1 class="section-title">Corporate Travel &amp; Events</h1>
        <p class="section-desc">
          Punctual, discreet passenger transport for executives, client delegations, conferences, and corporate events across Munster.
        </p>
      </div>

      <div class="pillars-grid">
        <div class="pillar-card">
          <div>
            <div class="pillar-badge">💼</div>
            <h2 class="pillar-title">Meeting &amp; Conference Travel</h2>
            <p class="pillar-desc">
              Reliable airport pickups and hotel-to-office shuttles in Cork City, Midleton, and Waterford business parks.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Inquire Corporate
          </a>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🤝</div>
            <h2 class="pillar-title">Visiting Delegations</h2>
            <p class="pillar-desc">
              Dedicated group MPV transport ensuring international visitors and executives travel together comfortably.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Inquire Group Run
          </a>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🧾</div>
            <h2 class="pillar-title">Corporate Accounts &amp; Invoicing</h2>
            <p class="pillar-desc">
              Clear digital receipts, prompt customer service, and flexible arrangements for regular corporate bookings.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Contact Accounts
          </a>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

def build_hospital_runs_page():
    header = get_header(depth=1)
    footer = get_footer(depth=1)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hospital Runs &amp; Medical Appointments | Umair Taxi and Limo</title>
  <meta name="description" content="Compassionate, punctual hospital transport to Cork University Hospital (CUH), Mercy Hospital, South Infirmary, and University Hospital Waterford. Call 089 264 6246.">
  <link rel="icon" type="image/svg+xml" href="../assets/logo/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>

{header}

  <section class="section" style="padding-top: 50px;">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Caring &amp; Reliable Transport</span>
        <h1 class="section-title">Hospital Runs &amp; Medical Visits</h1>
        <p class="section-desc">
          Stress-free, patient, and punctual door-to-door transport for outpatient appointments, medical procedures, and hospital discharges.
        </p>
      </div>

      <div class="pillars-grid">
        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🏥</div>
            <h2 class="pillar-title">Cork University Hospital (CUH)</h2>
            <p class="pillar-desc">
              Direct transport from Youghal and East Cork. Avoid hospital parking stress and arrive calmly for your appointment.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Book CUH Transfer
          </a>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🏥</div>
            <h2 class="pillar-title">University Hospital Waterford</h2>
            <p class="pillar-desc">
              Direct connection from Youghal and West Waterford along the N25 directly to Ardkeen, Waterford.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Book Waterford Hospital Run
          </a>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🏥</div>
            <h2 class="pillar-title">Mercy &amp; South Infirmary</h2>
            <p class="pillar-desc">
              City center hospital visits with door-to-door drop off and scheduled return pickup when you are ready.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Book Cork Clinic Run
          </a>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

def build_aircoach_transfers_page():
    header = get_header(depth=1)
    footer = get_footer(depth=1)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aircoach &amp; Station Connections | Umair Taxi and Limo</title>
  <meta name="description" content="Prompt connections to Aircoach stops, Kent Train Station (Cork), Plunkett Station (Waterford), and ferry terminals. Based in Youghal. Call 089 264 6246.">
  <link rel="icon" type="image/svg+xml" href="../assets/logo/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>

{header}

  <section class="section" style="padding-top: 50px;">
    <div class="container">
      <div class="section-head">
        <span class="section-tag">Seamless Connections</span>
        <h1 class="section-title">Aircoach &amp; Station Runs</h1>
        <p class="section-desc">
          Connecting rural and coastal residences with express coaches, intercity railways, and maritime ferry ports.
        </p>
      </div>

      <div class="pillars-grid">
        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🚌</div>
            <h2 class="pillar-title">Aircoach Connections</h2>
            <p class="pillar-desc">
              Drop-offs and pickups at Aircoach stops connecting Cork, Dublin, and Dublin Airport.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Book Aircoach Link
          </a>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🚆</div>
            <h2 class="pillar-title">Kent Station (Cork) &amp; Midleton</h2>
            <p class="pillar-desc">
              Punctual connections for Iarnród Éireann trains to Dublin Heuston, Killarney, and regional rail lines.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Book Train Link
          </a>
        </div>

        <div class="pillar-card">
          <div>
            <div class="pillar-badge">🚢</div>
            <h2 class="pillar-title">Ringaskiddy &amp; Rosslare Ferry</h2>
            <p class="pillar-desc">
              Direct transfer to Brittany Ferries terminal at Ringaskiddy (Cork) and Rosslare Europort for France &amp; UK sailings.
            </p>
          </div>
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn-gold" style="font-size: 13px; padding: 8px 16px;">
            Book Ferry Port Run
          </a>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>"""

# -----------------------------------------------------------------------------
# 11. SITEMAP & ROBOTS.TXT GENERATOR
# -----------------------------------------------------------------------------
def build_seo_assets():
    sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://umairtaxilimo.ie/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://umairtaxilimo.ie/services.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://umairtaxilimo.ie/services/airport-transfers.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
  </url>
  <url>
    <loc>https://umairtaxilimo.ie/services/local-taxi.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://umairtaxilimo.ie/tours.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://umairtaxilimo.ie/service-areas.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>
  <url>
    <loc>https://umairtaxilimo.ie/fleet.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://umairtaxilimo.ie/about.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://umairtaxilimo.ie/contact.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""

    robots = """User-agent: *
Allow: /
Sitemap: https://umairtaxilimo.ie/sitemap.xml"""

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(robots)
    print("sitemap.xml and robots.txt written.")

# -----------------------------------------------------------------------------
# WRITE ALL SUBPAGES
# -----------------------------------------------------------------------------
with open("services.html", "w", encoding="utf-8") as f:
    f.write(build_services_page())
print("services.html written.")

with open("services/airport-transfers.html", "w", encoding="utf-8") as f:
    f.write(build_airport_transfers_page())
print("services/airport-transfers.html written.")

with open("services/local-taxi.html", "w", encoding="utf-8") as f:
    f.write(build_local_taxi_page())
print("services/local-taxi.html written.")

with open("services/golf-tours.html", "w", encoding="utf-8") as f:
    f.write(build_golf_tours_page())
print("services/golf-tours.html written.")

with open("services/corporate-travel.html", "w", encoding="utf-8") as f:
    f.write(build_corporate_travel_page())
print("services/corporate-travel.html written.")

with open("services/hospital-runs.html", "w", encoding="utf-8") as f:
    f.write(build_hospital_runs_page())
print("services/hospital-runs.html written.")

with open("services/aircoach-transfers.html", "w", encoding="utf-8") as f:
    f.write(build_aircoach_transfers_page())
print("services/aircoach-transfers.html written.")

with open("tours.html", "w", encoding="utf-8") as f:
    f.write(build_tours_page())
print("tours.html written.")

with open("service-areas.html", "w", encoding="utf-8") as f:
    f.write(build_service_areas_page())
print("service-areas.html written.")

with open("fleet.html", "w", encoding="utf-8") as f:
    f.write(build_fleet_page())
print("fleet.html written.")

with open("about.html", "w", encoding="utf-8") as f:
    f.write(build_about_page())
print("about.html written.")

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(build_contact_page())
print("contact.html written.")

build_seo_assets()
print("All subpages generated successfully.")
